from dataclasses import dataclass

from ndsl.dsl.typing import Bool, Float, Int

from pyMoist.convection.GF_2020.cumulus_parameterization.constants import PRESSURE_GRADIENT_CONSTANT


@dataclass
class GF2020CumulusParameterizationConfig:
    # plume dependent (one for each plume)
    DOWNDRAFT_MAX_HEIGHT_LAND_SHALLOW: Float
    DOWNDRAFT_MAX_HEIGHT_LAND_MID: Float
    DOWNDRAFT_MAX_HEIGHT_LAND_DEEP: Float
    DOWNDRAFT_MAX_HEIGHT_OCEAN_SHALLOW: Float
    DOWNDRAFT_MAX_HEIGHT_OCEAN_MID: Float
    DOWNDRAFT_MAX_HEIGHT_OCEAN_DEEP: Float
    UPDRAFT_MAX_HEIGHT_LAND_SHALLOW: Float
    UPDRAFT_MAX_HEIGHT_LAND_MID: Float
    UPDRAFT_MAX_HEIGHT_LAND_DEEP: Float
    UPDRAFT_MAX_HEIGHT_OCEAN_SHALLOW: Float
    UPDRAFT_MAX_HEIGHT_OCEAN_MID: Float
    UPDRAFT_MAX_HEIGHT_OCEAN_DEEP: Float
    MINIMUM_EVAP_FRACTION_LAND_SHALLOW: Float
    MINIMUM_EVAP_FRACTION_LAND_MID: Float
    MINIMUM_EVAP_FRACTION_LAND_DEEP: Float
    MINIMUM_EVAP_FRACTION_OCEAN_SHALLOW: Float
    MINIMUM_EVAP_FRACTION_OCEAN_MID: Float
    MINIMUM_EVAP_FRACTION_OCEAN_DEEP: Float
    MAXIMUM_EVAP_FRACTION_LAND_SHALLOW: Float
    MAXIMUM_EVAP_FRACTION_LAND_MID: Float
    MAXIMUM_EVAP_FRACTION_LAND_DEEP: Float
    MAXIMUM_EVAP_FRACTION_OCEAN_SHALLOW: Float
    MAXIMUM_EVAP_FRACTION_OCEAN_MID: Float
    MAXIMUM_EVAP_FRACTION_OCEAN_DEEP: Float
    CLOUD_BASE_MASS_FLUX_FACTOR_SHALLOW: Float
    CLOUD_BASE_MASS_FLUX_FACTOR_MID: Float
    CLOUD_BASE_MASS_FLUX_FACTOR_DEEP: Float
    USE_EXCESS_SHALLOW: Int
    USE_EXCESS_MID: Int
    USE_EXCESS_DEEP: Int
    AVERAGE_LAYER_DEPTH_SHALLOW: Float
    AVERAGE_LAYER_DEPTH_MID: Float
    AVERAGE_LAYER_DEPTH_DEEP: Float
    ENABLE_SHALLOW: Int
    ENABLE_MID: Int
    ENABLE_DEEP: Int
    ENTRAINMENT_RATE_SHALLOW: Float
    ENTRAINMENT_RATE_MID: Float
    ENTRAINMENT_RATE_DEEP: Float
    C0_SHAL: Float
    C0_MID: Float
    C0_DEEP: Float
    TAU_MID: Float
    TAU_DEEP: Float
    CLOSURE_CHOICE_SHALLOW: Int
    CLOSURE_CHOICE_MID: Int
    CLOSURE_CHOICE_DEEP: Int
    # plume independent
    SHALLOW_MID_DEEP: Bool
    ZERO_DIFF: Int
    MOIST_TRIGGER: Int
    LAMBDA_DEEP: Float
    LAMBDA_SHALLOW_DOWN: Float
    CAP_MAXS: Float
    OUTPUT_SOUNDING: Int
    USE_SCALE_DEP: Int
    SATURATION_CALCULATION_CHOICE: Int
    CLOUD_LEVEL_GRID: Int
    FRAC_MODIS: Int
    BOUNDARY_CONDITION_METHOD: Int
    OVERSHOOT: Float
    USE_MEMORY: Int
    DOWNDRAFT: Int
    USE_WETBULB: Int
    DIURNAL_CYCLE: Int
    USE_LINEAR_SUBCLOUD_MOISTURE_FLUXES: Int
    CRITICAL_MIXING_RATIO_OVER_OCEAN: Float
    CRITICAL_MIXING_RATIO_OVER_LAND: Float
    BETA_SHALLOW: Float
    EVAP_FIX: Int
    SGS_W_TIMESCALE: Int
    VERTICAL_DISCRETIZATION_OPTION: Int
    ALP1: Float
    USE_FCT: Int
    MIN_ENTRAINMENT_RATE: Float
    USE_SMOOTH_TENDENCIES: Int
    USE_RAIN_EVAP_BELOW_CLOUD_BASE: Int
    USE_CLOUD_DISSIPATION: Float
    LIGHTNING_DIAGNOSTICS: Int
    USE_TRACER_SCAVENGE: Int
    USE_TRACER_EVAPORATION: Int
    USE_FLUX_FORM: Int
    MAX_TEMP_VAPOR_TENDENCY: Float


# @dataclass
# class PlumeSpecificConstants:
#     self.PLUME_INDEX = 2
#     self.DOWNDRAFT_MAX_HEIGHT_LAND = (
#         cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_LAND_DEEP
#     )
#     self.DOWNDRAFT_MAX_HEIGHT_OCEAN = (
#         cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_OCEAN_DEEP
#     )
#     self.UPDRAFT_MAX_HEIGHT_LAND = (
#         cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_LAND_DEEP
#     )
#     self.UPDRAFT_MAX_HEIGHT_OCEAN = (
#         cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_OCEAN_DEEP
#     )
#     self.MINIMUM_EVAP_FRACTION_LAND = (
#         cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_LAND_DEEP
#     )
#     self.MINIMUM_EVAP_FRACTION_OCEAN = (
#         cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_OCEAN_DEEP
#     )
#     self.MAXIMUM_EVAP_FRACTION_LAND = (
#         cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_LAND_DEEP
#     )
#     self.MAXIMUM_EVAP_FRACTION_OCEAN = (
#         cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_OCEAN_DEEP
#     )
#     self.CLOUD_BASE_MASS_FLUX_FACTOR = (
#         cumulus_parameterization_config.CLOUD_BASE_MASS_FLUX_FACTOR_DEEP
#     )
#     self.USE_EXCESS = cumulus_parameterization_config.USE_EXCESS_DEEP
#     self.ENTRAINMENT_RATE = cumulus_parameterization_config.ENTRAINMENT_RATE_DEEP
#     self.ENABLE_PLUME = cumulus_parameterization_config.ENABLE_DEEP
#     self.AVERAGE_LAYER_DEPTH = cumulus_parameterization_config.AVERAGE_LAYER_DEPTH_DEEP

#     # maximum depth (mb) of capping inversion (larger cap = no convection)
#     if (
#         cumulus_parameterization_config.ZERO_DIFF == 1
#         or cumulus_parameterization_config.MOIST_TRIGGER == 0
#     ):
#         self.CAP_MAX_INC = Float(20.0)
#     else:
#         self.CAP_MAX_INC = Float(90.0)

#     # lambda_U parameter for momentum transport
#     if PRESSURE_GRADIENT_CONSTANT != 0.0:
#         self.LAMBDA_DEEP = Float(0.0)
#         self.LAMBDA_DOWN = Float(0.0)
#     else:
#         self.LAMBDA_DEEP = cumulus_parameterization_config.LAMBDA_DEEP
#         self.LAMBDA_DOWN = cumulus_parameterization_config.LAMBDA_SHALLOW_DOWN

#     # minimum depth (m) clouds must have
#     self.MINIMUM_DEPTH = Float(1000.0)

#     # max height(m) above ground where updraft air can originate
#     self.MAX_UPDRAFT_ORIGIN_HEIGHT = Float(4000.0)

#     # height(m) above which no downdrafts are allowed to originate
#     self.MAX_DOWNDRAFT_ORIGIN_HEIGHt = Float(3000.0)

#     # depth(m) over which downdraft detrains all its mass
#     self.DETRAINMENT_CRITICAL_DEPTH = Float(0.5) * self.MINIMUM_DEPTH

#     self.C0 = cumulus_parameterization_config.C0_DEEP

#     # temperature for diurnal cycle section
#     self.T_STAR = Float(5.0)  # temp scale in original paper = 1 K

#     # timescale of cape removal
#     self.TAU_CAPE_REMOVAL = cumulus_parameterization_config.TAU_DEEP

#     # closure choice
#     self.CLOSURE_CHOICE = cumulus_parameterization_config.CLOSURE_CHOICE_DEEP


class DeepSpecificConstants:
    def __init__(self, cumulus_parameterization_config: GF2020CumulusParameterizationConfig):
        self.PLUME_INDEX = 2
        self.DOWNDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_LAND_DEEP
        self.DOWNDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_OCEAN_DEEP
        self.UPDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_LAND_DEEP
        self.UPDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_OCEAN_DEEP
        self.MINIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_LAND_DEEP
        self.MINIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_OCEAN_DEEP
        self.MAXIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_LAND_DEEP
        self.MAXIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_OCEAN_DEEP
        self.CLOUD_BASE_MASS_FLUX_FACTOR = cumulus_parameterization_config.CLOUD_BASE_MASS_FLUX_FACTOR_DEEP
        self.USE_EXCESS = cumulus_parameterization_config.USE_EXCESS_DEEP
        self.ENTRAINMENT_RATE = cumulus_parameterization_config.ENTRAINMENT_RATE_DEEP
        self.ENABLE_PLUME = cumulus_parameterization_config.ENABLE_DEEP
        self.AVERAGE_LAYER_DEPTH = cumulus_parameterization_config.AVERAGE_LAYER_DEPTH_DEEP

        # maximum depth (mb) of capping inversion (larger cap = no convection)
        if cumulus_parameterization_config.ZERO_DIFF == 1 or cumulus_parameterization_config.MOIST_TRIGGER == 0:
            self.CAP_MAX_INC = Float(20.0)
        else:
            self.CAP_MAX_INC = Float(90.0)

        # lambda_U parameter for momentum transport
        if PRESSURE_GRADIENT_CONSTANT != 0.0:
            self.LAMBDA_DEEP = Float(0.0)
            self.LAMBDA_DOWN = Float(0.0)
        else:
            self.LAMBDA_DEEP = cumulus_parameterization_config.LAMBDA_DEEP
            self.LAMBDA_DOWN = cumulus_parameterization_config.LAMBDA_SHALLOW_DOWN

        # minimum depth (m) clouds must have
        self.MINIMUM_DEPTH = Float(1000.0)

        # max height(m) above ground where updraft air can originate
        self.MAX_UPDRAFT_ORIGIN_HEIGHT = Float(4000.0)

        # height(m) above which no downdrafts are allowed to originate
        self.MAX_DOWNDRAFT_ORIGIN_HEIGHt = Float(3000.0)

        # depth(m) over which downdraft detrains all its mass
        self.DETRAINMENT_CRITICAL_DEPTH = Float(0.5) * self.MINIMUM_DEPTH

        self.C0 = cumulus_parameterization_config.C0_DEEP

        # temperature for diurnal cycle section
        self.T_STAR = Float(5.0)  # temp scale in original paper = 1 K

        # timescale of cape removal
        self.TAU_CAPE_REMOVAL = cumulus_parameterization_config.TAU_DEEP

        # closure choice
        self.CLOSURE_CHOICE = cumulus_parameterization_config.CLOSURE_CHOICE_DEEP


class MidSpecificConstants:
    def __init__(self, cumulus_parameterization_config: GF2020CumulusParameterizationConfig):
        # set a number of plume dependent constants
        self.PLUME_INDEX = 1
        self.DOWNDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_LAND_MID
        self.DOWNDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_OCEAN_MID
        self.UPDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_LAND_MID
        self.UPDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_OCEAN_MID
        self.MINIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_LAND_MID
        self.MINIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_OCEAN_MID
        self.MAXIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_LAND_MID
        self.MAXIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_OCEAN_MID
        self.CLOUD_BASE_MASS_FLUX_FACTOR = cumulus_parameterization_config.CLOUD_BASE_MASS_FLUX_FACTOR_MID
        self.USE_EXCESS = cumulus_parameterization_config.USE_EXCESS_MID
        self.ENTRAINMENT_RATE = cumulus_parameterization_config.ENTRAINMENT_RATE_MID
        self.ENABLE_PLUME = cumulus_parameterization_config.ENABLE_MID
        self.AVERAGE_LAYER_DEPTH = cumulus_parameterization_config.AVERAGE_LAYER_DEPTH_MID

        # maximum depth (mb) of capping inversion (larger cap = no convection)
        if cumulus_parameterization_config.ZERO_DIFF == 1 or cumulus_parameterization_config.MOIST_TRIGGER == 0:
            self.CAP_MAX_INC = Float(10.0)
        else:
            self.CAP_MAX_INC = Float(90.0)

        # lambda_U parameter for momentum transport
        if PRESSURE_GRADIENT_CONSTANT != 0.0:
            self.LAMBDA_DEEP = Float(0.0)
            self.LAMBDA_DOWN = Float(0.0)
        else:
            self.LAMBDA_DEEP = cumulus_parameterization_config.LAMBDA_SHALLOW_DOWN
            self.LAMBDA_DOWN = cumulus_parameterization_config.LAMBDA_SHALLOW_DOWN

        # minimum depth (m) clouds must have
        self.MINIMUM_DEPTH = Float(1000.0)

        # max height(m) above ground where updraft air can originate
        self.MAX_UPDRAFT_ORIGIN_HEIGHT = Float(3000.0)

        # height(m) above which no downdrafts are allowed to originate
        self.MAX_DOWNDRAFT_ORIGIN_HEIGHt = Float(3000.0)

        # depth(m) over which downdraft detrains all its mass
        self.DETRAINMENT_CRITICAL_DEPTH = Float(0.5) * self.MINIMUM_DEPTH

        self.C0 = cumulus_parameterization_config.C0_MID

        # temperature for diurnal cycle section
        self.T_STAR = Float(40.0)

        # timescale of cape removal
        self.TAU_CAPE_REMOVAL = cumulus_parameterization_config.TAU_MID

        # closure choice
        self.CLOSURE_CHOICE = cumulus_parameterization_config.CLOSURE_CHOICE_MID


class ShallowSpecificConstants:
    def __init__(self, cumulus_parameterization_config: GF2020CumulusParameterizationConfig):
        self.PLUME_INDEX = 0
        self.DOWNDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_LAND_SHALLOW
        self.DOWNDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.DOWNDRAFT_MAX_HEIGHT_OCEAN_SHALLOW
        self.UPDRAFT_MAX_HEIGHT_LAND = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_LAND_SHALLOW
        self.UPDRAFT_MAX_HEIGHT_OCEAN = cumulus_parameterization_config.UPDRAFT_MAX_HEIGHT_OCEAN_SHALLOW
        self.MINIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_LAND_SHALLOW
        self.MINIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MINIMUM_EVAP_FRACTION_OCEAN_SHALLOW
        self.MAXIMUM_EVAP_FRACTION_LAND = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_LAND_SHALLOW
        self.MAXIMUM_EVAP_FRACTION_OCEAN = cumulus_parameterization_config.MAXIMUM_EVAP_FRACTION_OCEAN_SHALLOW
        self.CLOUD_BASE_MASS_FLUX_FACTOR = cumulus_parameterization_config.CLOUD_BASE_MASS_FLUX_FACTOR_SHALLOW
        self.USE_EXCESS = cumulus_parameterization_config.USE_EXCESS_SHALLOW
        self.ENTRAINMENT_RATE = cumulus_parameterization_config.ENTRAINMENT_RATE_SHALLOW
        self.ENABLE_PLUME = cumulus_parameterization_config.ENABLE_SHALLOW
        self.AVERAGE_LAYER_DEPTH = cumulus_parameterization_config.AVERAGE_LAYER_DEPTH_SHALLOW
        # maximum depth (mb) of capping inversion (larger cap = no convection)
        if cumulus_parameterization_config.ZERO_DIFF == 1 or cumulus_parameterization_config.MOIST_TRIGGER == 0:
            self.CAP_MAX_INC = Float(25.0)
        else:
            self.CAP_MAX_INC = Float(10.0)
        # lambda_U parameter for momentum transport
        if PRESSURE_GRADIENT_CONSTANT != 0.0:
            self.LAMBDA_DEEP = Float(0.0)

            self.LAMBDA_DOWN = Float(0.0)
        else:
            self.LAMBDA_DEEP = cumulus_parameterization_config.LAMBDA_DEEP
            self.LAMBDA_DOWN = cumulus_parameterization_config.LAMBDA_SHALLOW_DOWN
        # minimum depth (m) clouds must have
        self.MINIMUM_DEPTH = Float(500.0)
        # max height(m) above ground where updraft air can originate
        self.MAX_UPDRAFT_ORIGIN_HEIGHT = Float(2000.0)
        # height(m) above which no downdrafts are allowed to originate
        self.MAX_DOWNDRAFT_ORIGIN_HEIGHt = Float(3000.0)
        # depth(m) over which downdraft detrains all its mass
        self.DETRAINMENT_CRITICAL_DEPTH = Float(0.5) * self.MINIMUM_DEPTH
        self.C0 = cumulus_parameterization_config.C0_SHAL
        # temperature for diurnal cycle section
        self.T_STAR = Float(40.0)
        # timescale of cape removal
        self.TAU_CAPE_REMOVAL = -999  # not used - ideally should not exist for this plume
        # closure choice
        self.CLOSURE_CHOICE = cumulus_parameterization_config.CLOSURE_CHOICE_SHALLOW
