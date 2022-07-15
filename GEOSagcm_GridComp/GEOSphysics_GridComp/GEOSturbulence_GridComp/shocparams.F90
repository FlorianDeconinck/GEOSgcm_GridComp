module SHOCPARAMS

 implicit none

 type SHOCPARAMS_TYPE
    integer :: LENOPT
    integer :: BUOYOPT
    real    :: LAMBDA
    real    :: TSCALE
    real    :: VONK
    real    :: CKVAL
    real    :: CEFAC
    real    :: CESFAC
    real    :: LENFAC
    real    :: KRADFAC
    real    :: CLDLEN
 endtype SHOCPARAMS_TYPE

end module SHOCPARAMS
