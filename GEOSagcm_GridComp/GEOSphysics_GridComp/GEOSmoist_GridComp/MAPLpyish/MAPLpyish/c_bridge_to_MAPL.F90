#include "MAPL_Generic.h"
#include "MAPL_Exceptions.h"

module C_BRIDGE_TO_MAPL
    
    use ESMF
    USE MAPL
    use iso_c_binding

    implicit NONE
    
    private
    public :: MAPLPy_ESMF_AttributeGet_1D_int

    CONTAINS

    function MAPLPy_ESMF_AttributeGet_1D_int(esmf_state_c_ptr, name_c_ptr, name_len) result(return_value) bind(c, name="MAPLPy_ESMF_AttributeGet_1D_int")
        ! Read in STATE
        type(c_ptr), intent(in) :: esmf_state_c_ptr
        type(ESMF_State), pointer :: state

        ! Read in name
        type(c_ptr), intent(in), value :: name_c_ptr
        integer(c_int), intent(in), value :: name_len
        character(len=name_len,kind=c_char), pointer :: varname

        ! Return value
        integer :: return_value

        WRITE (*,*) 'ENTERED MAPLPy_ESMF_AttributeGet_1D_int'

        ! Turn the C string into a Fortran string
        call c_f_pointer(name_c_ptr, varname)

        ! Turn the ESMF State C pointer to a Fortran pointer
        call c_f_pointer(esmf_state_c_ptr, state)

        ! Call function
        call ESMF_AttributeGet(state, name=varname, value=return_value)  ! Need RC=Status and handling
    
    end function MAPLPy_ESMF_AttributeGet_1D_int

    subroutine MAPLPy_ESMF_MethodExecute(esmf_state_c_ptr, label_c_ptr, label_len) bind(c, name="MAPLPy_ESMF_MethodExecute")
        ! Read in STATE
        type(c_ptr), intent(in) :: esmf_state_c_ptr
        type(ESMF_State), pointer :: state

        ! Read in name
        type(c_ptr), intent(in), value :: label_c_ptr
        integer(c_int), intent(in), value :: label_len
        character(len=label_len,kind=c_char), pointer :: label

        ! Turn the C string into a Fortran string
        call c_f_pointer(label_c_ptr, label)

        ! Turn the ESMF State C pointer to a Fortran pointer
        call c_f_pointer(esmf_state_c_ptr, state)

        call ESMF_MethodExecute(state, label=label)

    end subroutine MAPLPy_ESMF_MethodExecute

    function MAPLpy_GetPointer_via_ESMFAttr(esmf_state_c_ptr, name_c_ptr, name_len) result(c_data_ptr) bind(c, name="MAPLpy_GetPointer_via_ESMFAttr")
        ! Read in STATE
        type(c_ptr), intent(in) :: esmf_state_c_ptr
        type(ESMF_State), pointer :: state

        ! Read in name
        type(c_ptr), intent(in), value :: name_c_ptr
        integer(c_int), intent(in), value :: name_len
        character(len=name_len,kind=c_char), pointer :: name

        ! Results
        character(len=ESMF_MAXSTR) :: field_name_from_esmf
        real, pointer, dimension(:,:,:) :: f_ptr
        type(c_ptr) :: c_data_ptr

        ! Turn the C string into a Fortran string
        call c_f_pointer(name_c_ptr, name)

        ! Turn the ESMF State C pointer to a Fortran pointer
        call c_f_pointer(esmf_state_c_ptr, state)        

        call ESMF_AttributeGet(state, name=name, value=field_name_from_esmf)
        call MAPL_GetPointer(state, f_ptr, trim(field_name_from_esmf))
        c_data_ptr=c_loc(f_ptr)
    
    end function    

end module C_BRIDGE_TO_MAPL