import dataclasses

from ndsl import Quantity, State
from ndsl.constants import X_DIM, Y_DIM, Z_DIM, Z_INTERFACE_DIM
from ndsl.dsl.typing import Float, Int


@dataclasses.dataclass
class ShallowConvectionState(State):
    # Inputs:
    kpbl_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Height of PBL",
            "units": "m",
            "intent": "in",
            "dtype": Int,
        }
    )
    tke_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "Turbulent kinetic energy at the interfaces",
            "units": "m2/s2",
            "intent": "in",
            "dtype": Float,
        }
    )
    rkfre: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Resolution dependent vertical velocity variance as fraction of tke",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )
    frland: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Land fraction",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )
    pifc0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "Environmental pressure at the interfaces",
            "units": "Pa",
            "intent": "in",
            "dtype": Float,
        }
    )
    zifc0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "Environmental height at the interfaces",
            "units": "m",
            "intent": "in",
            "dtype": Float,
        }
    )
    pmid0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental pressure at the layer mid-point",
            "units": "Pa",
            "intent": "in",
            "dtype": Float,
        }
    )
    zmid0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental height at the layer mid-point",
            "units": "m",
            "intent": "in",
            "dtype": Float,
        }
    )
    dp0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental layer pressure thickness. > 0",
            "units": "Pa",
            "intent": "in",
            "dtype": Float,
        }
    )
    u0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental zonal wind",
            "units": "m/s",
            "intent": "in",
            "dtype": Float,
        }
    )
    v0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental meridional wind",
            "units": "m/s",
            "intent": "in",
            "dtype": Float,
        }
    )
    qv0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental water vapor specific humidity",
            "units": "kg/kg",
            "intent": "in",
            "dtype": Float,
        }
    )
    ql0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental liquid water specific humidity",
            "units": "kg/kg",
            "intent": "in",
            "dtype": Float,
        }
    )
    qi0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental ice specific humidity",
            "units": "kg/kg",
            "intent": "in",
            "dtype": Float,
        }
    )
    t0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Environmental temperature",
            "units": "K",
            "intent": "in",
            "dtype": Float,
        }
    )
    shfx: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Surface sensible heat",
            "units": "J",
            "intent": "in",
            "dtype": Float,
        }
    )
    evap: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Surface evaporation",
            "units": "kg/m^2/s",
            "intent": "in",
            "dtype": Float,
        }
    )
    cush: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Convective scale height",
            "units": "m",
            "intent": "in",
            "dtype": Float,
        }
    )
    cnvtr: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Convective tracer (reduce to 2D?)",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )
    CNV_Tracers: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM, "ntracers"],
            "desc": "Convective tracers",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )
    exnmid0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Exner function at the layer mid-point",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )
    exnifc0_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "Exner function at the interfaces",
            "units": "?",
            "intent": "in",
            "dtype": Float,
        }
    )

    # Outputs:
    umf_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "Updraft mass flux at interfaces",
            "units": "[kg/m2/s]",
            "intent": "out",
            "dtype": Float,
        }
    )
    dcm_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Detrained cloudy air mass",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qtflx_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "?",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    slflx_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "? ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    uflx_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "? ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    vflx_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_INTERFACE_DIM],
            "desc": "? ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qvten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of water vapor specific humidity",
            "units": "[kg/kg/s]",
            "intent": "out",
            "dtype": Float,
        }
    )
    qlten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of liquid water specific humidity",
            "units": "[kg/kg/s]",
            "intent": "out",
            "dtype": Float,
        }
    )
    qiten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of ice specific humidity [kg/kg/s] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    tten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of temperature",
            "units": "[K/s]",
            "intent": "out",
            "dtype": Float,
        }
    )
    uten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of zonal wind",
            "units": "m/s2",
            "intent": "out",
            "dtype": Float,
        }
    )
    vten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of meridional wind",
            "units": "m/s2",
            "intent": "out",
            "dtype": Float,
        }
    )
    qrten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of rain water specific humidity",
            "units": "kg/kg/s",
            "intent": "out",
            "dtype": Float,
        }
    )
    qsten_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Tendency of snow specific humidity",
            "units": "kg/kg/s",
            "intent": "out",
            "dtype": Float,
        }
    )
    cufrc_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Shallow cumulus cloud fraction at the layer mid-point",
            "units": "fraction",
            "intent": "out",
            "dtype": Float,
        }
    )
    fer_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Fractional lateral entrainment rate",
            "units": "1/Pa",
            "intent": "out",
            "dtype": Float,
        }
    )
    fdr_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "Fractional lateral detrainment rate",
            "units": "1/Pa",
            "intent": "out",
            "dtype": Float,
        }
    )
    ndrop_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    nice_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qldet_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qlsub_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qidet_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qisub_inv: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM, Z_DIM],
            "desc": "[?] ",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    tpert_out: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Temperature perturbation",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
    qpert_out: Quantity = dataclasses.field(
        metadata={
            "dims": [X_DIM, Y_DIM],
            "desc": "Humidity perturbation",
            "units": "?",
            "intent": "out",
            "dtype": Float,
        }
    )
