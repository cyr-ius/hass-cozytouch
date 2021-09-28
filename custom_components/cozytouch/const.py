"""Constants for the Cozytouch component."""
import logging
from cozytouchpy.constant import DeviceType
from homeassistant.components.climate.const import (
    HVAC_MODE_AUTO,
    HVAC_MODE_COOL,
    HVAC_MODE_HEAT,
    HVAC_MODE_HEAT_COOL,
    HVAC_MODE_OFF,
)

LOGGER = logging.getLogger(__package__)

DOMAIN = "cozytouch"
COORDINATOR = "cozytouch_coordinator"
COZYTOUCH_DATAS = "cozy_datas"
COMPONENTS = ["climate", "switch", "water_heater", "binary_sensor", "sensor"]
SENSOR_TYPES = ["all", "pass", "i2g"]

DEFAULT_TIMEOUT = 10
DEFAULT_SCAN_INTERVAL = 60
DEFAULT_TIMEOUT = 10
DEFAULT_TIME_OFFSET = 7200
KW_UNIT = "kW"
COZYTOUCH_ACTUATOR = "model"
CONF_COZYTOUCH_ACTUATOR = "model"
DEFAULT_COZYTOUCH_ACTUATOR = "all"

STATE_AUTO = "auto"
STATE_MANUEL = "manuel"
STATE_COMFORT = "comfort"
STATE_STOP = "stop"
STATE_EXTERNAL = "external"
SERVICE_SET_AWAY_MODE = "set_away_mode"
SERVICE_SET_BOOST_MODE = "set_boost_mode"
SERVICE_SET_OPERATION_MODE = "set_operation_mode"

PRESET_COMFORT = "Comfort"
PRESET_ECO = "Eco"
PRESET_SECURED = "Secured"
PRESET_COMFORT1 = "Comfort 1"
PRESET_COMFORT2 = "Comfort 2"
PRESET_FROSTPROTECTION = "Frostprotection"
PRESET_AUTO = "Auto"
PRESET_MANU = "Manu"
PRESET_STOP = "Stop"
PRESET_INTERNAL = "Internal Scheduling"
PRESET_EXTERNAL = "External Scheduling"
PRESET_AWAY = "Absence"
PRESET_BOOST = "Boost"

PRESET_MODE_TO_COZY = {
    PRESET_AUTO: "auto",
    PRESET_AWAY: "absence",
    PRESET_BOOST: "boost",
    PRESET_COMFORT: "comfort",
    PRESET_COMFORT1: "comfort-1",
    PRESET_COMFORT2: "comfort-1",
    PRESET_ECO: "eco",
    PRESET_EXTERNAL: "externalScheduling",
    PRESET_FROSTPROTECTION: "frostprotection",
    PRESET_INTERNAL: "internalScheduling",
    PRESET_MANU: "manu",
    PRESET_SECURED: "secured",
    PRESET_SECURED: "secured",
    PRESET_STOP: "off",
}

COZY_TO_PRESET_MODE = {
    "absence": PRESET_AWAY,
    "auto": PRESET_AUTO,
    "boost": PRESET_BOOST,
    "comfort-1": PRESET_COMFORT1,
    "comfort-2": PRESET_COMFORT2,
    "comfort": PRESET_COMFORT,
    "eco": PRESET_ECO,
    "externalScheduling": PRESET_EXTERNAL,
    "frostprotection": PRESET_FROSTPROTECTION,
    "internalScheduling": PRESET_INTERNAL,
    "manu": PRESET_MANU,
    "secured": PRESET_SECURED,
    "off": PRESET_STOP,
}

ATTR_TIME_PERIOD = "time_period"
ATTR_OPERATION_MODE = "boiler_opmode"

HVAC_MODE_LIST = "hvac_modes"
PRESET_MODE_LIST = "preset_modes"

SCHEMA_HEATER = DeviceType.HEATER
SCHEMA_HEATINGZONE = DeviceType.APC_HEATING_ZONE
SCHEMA_HEATINGCOOLINGZONE = DeviceType.APC_HEATING_COOLING_ZONE


HVAC_MODE_TO_HEATER = {
    HVAC_MODE_AUTO: "internal",
    HVAC_MODE_HEAT: "basic",
    HVAC_MODE_OFF: "standby",
}
HEATER_TO_HVAC_MODE = {
    "internal": HVAC_MODE_AUTO,
    "standby": HVAC_MODE_OFF,
    "basic": HVAC_MODE_HEAT,
    "auto": HVAC_MODE_AUTO,
    "off": HVAC_MODE_OFF,
}

SCHEMA_HEATER = {
    HVAC_MODE_LIST: [HVAC_MODE_HEAT, HVAC_MODE_AUTO, HVAC_MODE_OFF],
    PRESET_MODE_LIST: [
        PRESET_COMFORT,
        PRESET_COMFORT1,
        PRESET_COMFORT2,
        PRESET_ECO,
        PRESET_SECURED,
        PRESET_FROSTPROTECTION,
    ],
}

HVAC_MODE_TO_HEATING = {
    HVAC_MODE_HEAT: "heating",
    HVAC_MODE_OFF: "off",
}
HEATING_TO_HVAC_MODE = {
    "heating": HVAC_MODE_HEAT,
    "off": HVAC_MODE_OFF,
}

SCHEMA_HEATINGZONE = {
    HVAC_MODE_LIST: [HVAC_MODE_HEAT, HVAC_MODE_OFF],
    PRESET_MODE_LIST: [
        PRESET_COMFORT,
        PRESET_ECO,
        PRESET_AUTO,
        PRESET_MANU,
        PRESET_STOP,
        PRESET_INTERNAL,
        PRESET_EXTERNAL,
    ],
}

HVAC_MODE_TO_HEATINGCOOLING = {
    HVAC_MODE_COOL: "cooling",
    HVAC_MODE_HEAT: "heating",
    HVAC_MODE_HEAT_COOL: "heatingAndCooling",
    HVAC_MODE_OFF: "off",
}

HEATINGCOOLING_TO_HVAC_MODE = {
    "cooling": HVAC_MODE_COOL,
    "heating": HVAC_MODE_HEAT,
    "heatingAndCooling": HVAC_MODE_HEAT_COOL,
    "off": HVAC_MODE_OFF,
}

SCHEMA_HEATINGCOOLINGZONE = {
    HVAC_MODE_LIST: [
        HVAC_MODE_COOL,
        HVAC_MODE_HEAT,
        HVAC_MODE_HEAT_COOL,
        HVAC_MODE_OFF,
    ],
    PRESET_MODE_LIST: [
        PRESET_COMFORT,
        PRESET_ECO,
        PRESET_AUTO,
        PRESET_MANU,
        PRESET_STOP,
        PRESET_INTERNAL,
        PRESET_EXTERNAL,
    ],
}
