import cffi
from _cffi_backend import _CDataBase as CFFIObj
from typing import Any


class MAPLBridge:
    def __init__(self) -> None:
        # FFI & C library setup
        self.ffi = cffi.FFI()
        self.mapl_c_bridge = self.ffi.dlopen(
            "/home/fgdeconi/work/git/fp/geos/install_DEBUG/lib/libMAPLpyish.so"
        )

        # We use CFFI ABI mode, so we need to describe each function cdef
        # to the system

        # ESMF_AttributeGet
        self.ffi.cdef(
            "int MAPLPy_ESMF_AttributeGet_1D_int(void* esmf_state_c_ptr, char* name_c_ptr, int name_len);"
        )

        # MAPLpy_GetPointer_via_ESMFAttr
        self.ffi.cdef(
            "void* MAPLpy_GetPointer_via_ESMFAttr(void* esmf_state_c_ptr, char* name_c_ptr, int name_len);"
        )

        # MAPLPy_ESMF_MethodExecute
        self.ffi.cdef(
            "void MAPLPy_ESMF_MethodExecute(void* esmf_state_c_ptr, char* label_c_ptr, int label_len);"
        )

    def __del__(self):
        self.ffi.dlclose(self.mapl_c_bridge)

    def ESMF_AttributeGet(self, state: CFFIObj, name: str) -> Any:
        # TODO: depending on value type, redirect to correct bridge function
        return self.mapl_c_bridge.MAPLPy_ESMF_AttributeGet_1D_int(  # type: ignore
            state,
            self.ffi.new("char[]", name.encode()),
            len(name),
        )

    def ESMF_MethodExecute(self, state: CFFIObj, label: str) -> Any:
        self.mapl_c_bridge.MAPLPy_ESMF_MethodExecute(  # type: ignore
            state,
            self.ffi.new("char[]", label.encode()),
            len(label),
        )

    def MAPL_GetPointer_via_ESMFAttr(
        self,
        state: CFFIObj,
        name: str,
    ) -> Any:
        # TODO: depending on value type, redirect to correct bridge function
        return self.mapl_c_bridge.MAPLpy_GetPointer_via_ESMFAttr(  # type: ignore
            state,
            self.ffi.new("char[]", name.encode()),
            len(name),
        )
