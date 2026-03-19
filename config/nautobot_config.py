"""Nautobot development configuration file."""

# pylint: disable=invalid-envvar-default
import os
import sys

from nautobot.core.settings import *  # noqa: F403  # pylint: disable=wildcard-import,unused-wildcard-import
from nautobot.core.settings_funcs import is_truthy, parse_redis_connection

#
# Debug
#

DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", False))

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

#
# Logging
#

LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

#
# Redis
#

# Redis Cacheops
CACHEOPS_REDIS = parse_redis_connection(redis_database=1)

#
# Celery settings are not defined here because they can be overloaded with
# environment variables. By default they use `CACHES["default"]["LOCATION"]`.
#

# Enable installed plugins. Add the name of each plugin to the list.
# PLUGINS = ["nautobot_example_plugin"]
PLUGINS = [
    # Network to Code plugins
    "welcome_wizard",                   # a plugin to help new user populate their instance with common foundational data
    "nautobot_plugin_nornir",           # deals with the inventory where you have your host information
    "nautobot_ssot",                    # single source of truth module
    "nautobot_device_onboarding",       # use NAPALM and NetMiko to onboard devices into Nautobot
    "nautobot_golden_config",           # compare active configs with golden configs
    "nautobot_device_lifecycle_mgmt",
    "nautobot_firewall_models",

    # External plugins

    ]

# Plugins configuration settings is a dictionary of settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
    "nautobot_example_plugin": {},
    "nautobot_ssot": {},
    "nautobot_plugin_nornir": {
        "nornir_settings": {
            "credentials": "nautobot_plugin_nornir.plugins.credentials.nautobot_secrets.CredentialsNautobotSecrets",
            "runner": {        
                "plugin": "threaded",         
                "options": {              
                    "num_workers": 20,            
                },
            }
        },
    },
    "welcome_wizard": {
        "enable_devicetype-library": True,
        "enable_welcome_banner": True,
        "manufacturer_transform_func": None,
        "manufacturer_map": {},
    },
    "nautobot_device_onboarding": {
        "create_platform_if_missing": True,
        "create_manufacturer_if_missing": True,
        "create_device_type_if_missing": True,
        "create_device_role_if_missing": True,
        "default_device_role": "network",
    }
    # "nautobot_chatops": {},
}
