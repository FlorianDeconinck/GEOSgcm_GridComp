module C_BRIDGE_TO_MAPL
    
    use ESMF
    USE MAPL
    use iso_c_binding

    implicit NONE
    
    private
    public :: MAPLPy_ESMF_AttributeGet_1D_int

    CONTAINS

    function MAPLPy_ESMF_AttributeGet_1D_int(esmf_state_c_ptr, name_c_ptr, name_len) result(return_value) bind(c, name="MAPLPy_ESMF_AttributeGet_1D_int")
        implicit none

        ! Read in name
        type(c_ptr), intent(in), value :: name_c_ptr
        integer(c_int), intent(in), value :: name_len
        character(len=name_len,kind=c_char), pointer :: varname

        ! Read in STATE
        type(c_ptr), intent(in) :: esmf_state_c_ptr
        type(ESMF_State), pointer :: state

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

end module C_BRIDGE_TO_MAPL