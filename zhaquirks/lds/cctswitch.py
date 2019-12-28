"""Device handler for CCS-Switch-D0001 remote control."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Groups,
    Identify,
    LevelControl,
    OnOff,
    Ota,
    PowerConfiguration,
)
from zigpy.zcl.clusters.lighting import Color
from zigpy.zcl.clusters.lightlink import LightLink

from . import MANUFACTURER, LightLinkCluster
from ..const import (
    ARGS,
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    CLUSTER_ID,
    COMMAND,
    COMMAND_MOVE,
    COMMAND_MOVE_ON_OFF,
    COMMAND_MOVE_TO_COLOR_TEMP,
    COMMAND_MOVE_TO_LEVEL_WITH_ON_OFF,
    COMMAND_MOVE_TO_LEVEL,
    COMMAND_RELEASE,
    COMMAND_STEP,
    COMMAND_STEP_ON_OFF,
    COMMAND_TOGGLE,
    DEVICE_TYPE,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    SHORT_PRESS,
)


class CCTSwitch(CustomDevice):
    """Custom device representing CCTSwitch-D0001 remote control."""

    signature = {
        # <SimpleDescriptor endpoint = 1 profile = 260 device_type = 2048
        # device_version = 1 input_clusters = [0, 1, 3, 4096, 64769]
        # output_clusters = [3, 4, 6, 8, 25, 768, 4096] >
        MODELS_INFO: [(MANUFACTURER, "ZBT-CCTSwitch-D0001")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COLOR_CONTROLLER,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    LightLink.cluster_id,
                    0xFD01,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COLOR_CONTROLLER,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    LightLinkCluster,
                    0xFD01,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            }
        }
    }

    device_automation_triggers = {
        (SHORT_PRESS, BUTTON_1): {
            CLUSTER_ID: 6,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, BUTTON_2): {
            COMMAND: COMMAND_MOVE_TO_LEVEL,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
        },
        (LONG_PRESS, BUTTON_2): {
            COMMAND: COMMAND_MOVE,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, BUTTON_3): {
            COMMAND: COMMAND_MOVE_TO_COLOR_TEMP,
            CLUSTER_ID: 768,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, BUTTON_4): {
            COMMAND: COMMAND_MOVE_TO_LEVEL_WITH_ON_OFF
        },
    }
