import os
from typing import Dict, List

import numpy as np
from mpi4py import MPI

from ndsl.dsl.gt4py_utils import is_gpu_backend
from ndsl.dsl.typing import Float
from ndsl.optional_imports import cupy as cp
from pyMoist.interface.cuda_profiler import CUDAProfiler, TimedCUDAProfiler
from pyMoist.interface.f_py_conversion import FortranPythonConversion
from pyMoist.interface.flags import flags_fv_to_python
from pyMoist.interface.wrapper import GEOSPyMoistWrapper, MemorySpace
from MAPLpyish.api import MAPLBridge
from _cffi_backend import _CDataBase as CFFIObj


class PYMOIST_WRAPPER:
    def __init__(self) -> None:
        self.ready = False

    def init(
        self,
        fv_flags: CFFIObj,
        aero_state: CFFIObj,
        backend: str = "dace:cpu",
    ) -> None:
        self.rank = MPI.COMM_WORLD.Get_rank()
        self.backend = backend
        self.flags = flags_fv_to_python(fv_flags)
        self.aero_state = aero_state
        print(f"Moist Flags:\n{self.flags}")
        # For Fortran<->NumPy conversion
        if is_gpu_backend(self.backend):
            numpy_module = cp
            self.fortran_mem_space = MemorySpace.DEVICE
        else:
            numpy_module = np
            self.fortran_mem_space = MemorySpace.HOST
        self.f_py = FortranPythonConversion(
            self.flags.npx,
            self.flags.npy,
            self.flags.npz,
            numpy_module,
        )

        self.MAPL_bridge = MAPLBridge()

        # Setup pyFV3's dynamical core
        self.pymoist = GEOSPyMoistWrapper(self.flags, backend)

        self._timings: Dict[str, List[float]] = {}
        self.ready = True

    def finalize(self):
        import json

        with open("pymoist_timings.json", "w") as f:
            json.dump(self._timings, f, indent=4)

    def aer_activation(
        self,
        f_aero_dgn: CFFIObj,
        f_aero_num: CFFIObj,
        f_aero_hygroscopicity: CFFIObj,
        f_aero_sigma: CFFIObj,
        f_frland: CFFIObj,
        f_nn_ocean: np.float32,
        f_nn_land: np.float32,
        f_t: CFFIObj,
        f_plo: CFFIObj,
        f_qicn: CFFIObj,
        f_qils: CFFIObj,
        f_qlcn: CFFIObj,
        f_qlls: CFFIObj,
        f_vvel: CFFIObj,
        f_tke: CFFIObj,
        f_nacti: CFFIObj,
        f_nwfa: CFFIObj,
        f_nactl: CFFIObj,
    ):
        n_modes = self.MAPL_bridge.ESMF_AttributeGet(
            self.aero_state, name="number_of_aerosol_modes"
        )
        self.MAPL_bridge.ESMF_MethodExecute(
            self.aero_state, label="aerosol_activation_properties"
        )
        f_aero_sigma_from_MAPL = self.f_py._ffi.cast(
            "float*",
            self.MAPL_bridge.MAPL_GetPointer_via_ESMFAttr(
                self.aero_state,
                "width_of_aerosol_mode",
            ),
        )
        print(f">>>> NMODES: {n_modes}")
        print(f">>>> AERO_NUM p: {f_aero_sigma_from_MAPL}")
        new_sigma_mode_14 = self.f_py.fortran_to_python(
            f_aero_sigma_from_MAPL,
            [
                self.flags.npx,
                self.flags.npy,
                self.flags.npz,
            ],
        )
        print(f">>>> AERO_NUM c: {new_sigma_mode_14}")
        CUDAProfiler.start_cuda_profiler()
        with TimedCUDAProfiler("Fortran -> Python", self._timings):
            aero_dgn = self.f_py.fortran_to_python(
                f_aero_dgn,
                [
                    self.flags.npx,
                    self.flags.npy,
                    self.flags.npz,
                    self.flags.n_modes,
                ],
            )
            aero_num = self.f_py.fortran_to_python(
                f_aero_num,
                [
                    self.flags.npx,
                    self.flags.npy,
                    self.flags.npz,
                    self.flags.n_modes,
                ],
            )
            aero_hygroscopicity = self.f_py.fortran_to_python(
                f_aero_hygroscopicity,
                [
                    self.flags.npx,
                    self.flags.npy,
                    self.flags.npz,
                    self.flags.n_modes,
                ],
            )
            aero_sigma = self.f_py.fortran_to_python(
                f_aero_sigma,
                [
                    self.flags.npx,
                    self.flags.npy,
                    self.flags.npz,
                    self.flags.n_modes,
                ],
            )
            print(
                f">>>> AERO_NUM Vs AERO_NUM: {np.all(new_sigma_mode_14 == aero_sigma[:,:,:,13])}"
            )
            frland = self.f_py.fortran_to_python(
                f_frland, [self.flags.npx, self.flags.npy]
            )

            t = self.f_py.fortran_to_python(f_t)
            plo = self.f_py.fortran_to_python(f_plo)
            qicn = self.f_py.fortran_to_python(f_qicn)
            qils = self.f_py.fortran_to_python(f_qils)
            qlcn = self.f_py.fortran_to_python(f_qlcn)
            qlls = self.f_py.fortran_to_python(f_qlls)
            vvel = self.f_py.fortran_to_python(f_vvel)
            tke = self.f_py.fortran_to_python(f_tke)
            nacti = self.f_py.fortran_to_python(f_nacti)
            nwfa = self.f_py.fortran_to_python(f_nwfa)
            nactl = self.f_py.fortran_to_python(f_nactl)
            self.f_py.device_sync()

        # Run Aer Activation
        with TimedCUDAProfiler("Aer Activation numerics", self._timings):
            self.pymoist.aer_activation(
                aero_dgn=aero_dgn,
                aero_num=aero_num,
                aero_hygroscopicity=aero_hygroscopicity,
                aero_sigma=aero_sigma,
                frland=frland,
                nn_ocean=Float(f_nn_ocean),
                nn_land=Float(f_nn_land),
                t=t,
                plo=plo,
                qicn=qicn,
                qils=qils,
                qlcn=qlcn,
                qlls=qlls,
                vvel=vvel,
                tke=tke,
                nwfa=nwfa,
                nacti=nacti,
                nactl=nactl,
            )

        # Convert NumPy arrays back to Fortran
        with TimedCUDAProfiler("Python -> Fortran", self._timings):
            self.f_py.python_to_fortran(aero_dgn, f_aero_dgn)
            self.f_py.python_to_fortran(aero_num, f_aero_num)
            self.f_py.python_to_fortran(aero_hygroscopicity, f_aero_hygroscopicity)
            self.f_py.python_to_fortran(aero_sigma, f_aero_sigma)
            self.f_py.python_to_fortran(frland, f_frland)
            self.f_py.python_to_fortran(t, f_t)
            self.f_py.python_to_fortran(plo, f_plo)
            self.f_py.python_to_fortran(qicn, f_qicn)
            self.f_py.python_to_fortran(qils, f_qils)
            self.f_py.python_to_fortran(qlcn, f_qlcn)
            self.f_py.python_to_fortran(qlls, f_qlls)
            self.f_py.python_to_fortran(vvel, f_vvel)
            self.f_py.python_to_fortran(tke, f_tke)
            self.f_py.python_to_fortran(nacti, f_nacti)
            self.f_py.python_to_fortran(nwfa, f_nwfa)
            self.f_py.python_to_fortran(nactl, f_nactl)


WRAPPER = PYMOIST_WRAPPER()


def pyMoist_run_AerActivation(
    aero_dgn: CFFIObj,
    aero_num: CFFIObj,
    aero_hygroscopicity: CFFIObj,
    aero_sigma: CFFIObj,
    frland: CFFIObj,
    nn_ocean: np.float32,
    nn_land: np.float32,
    t: CFFIObj,
    plo: CFFIObj,
    qicn: CFFIObj,
    qils: CFFIObj,
    qlcn: CFFIObj,
    qlls: CFFIObj,
    vvel: CFFIObj,
    tke: CFFIObj,
    nacti: CFFIObj,
    nwfa: CFFIObj,
    nactl: CFFIObj,
):
    if not WRAPPER.ready:
        raise RuntimeError("[GEOS WRAPPER] Bad init, did you call init?")
    WRAPPER.aer_activation(
        aero_dgn,
        aero_num,
        aero_hygroscopicity,
        aero_sigma,
        frland,
        nn_ocean,
        nn_land,
        t,
        plo,
        qicn,
        qils,
        qlcn,
        qlls,
        vvel,
        tke,
        nacti,
        nwfa,
        nactl,
    )


def pyMoist_finalize():
    if WRAPPER.ready:
        WRAPPER.finalize()


def pyMoist_init(fv_flags: CFFIObj, aero_state: CFFIObj):
    # Read in the backend
    BACKEND = os.environ.get("GEOS_PYFV3_BACKEND", "dace:cpu")
    if WRAPPER.ready:
        raise RuntimeError("[PYMOIST WRAPPER] Double init")
    WRAPPER.init(
        fv_flags=fv_flags,
        aero_state=aero_state,
        backend=BACKEND,
    )
