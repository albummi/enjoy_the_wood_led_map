import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.light import LightEntity
from .light import EnjoyTheWoodLedMapLight

_LOGGER = logging.getLogger(__name__)

DOMAIN = "enjoy_the_wood_led_map"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    _LOGGER.info("Setting up Enjoy the Wood LED Map integration.")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Enjoy the Wood LED Map from a config entry."""
    ip_address = entry.data["ip_address"]
    _LOGGER.info("Setting up Enjoy the Wood LED Map with IP: %s", ip_address)
    
    # Entität erstellen und zur Home Assistant-Instanz hinzufügen
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = EnjoyTheWoodLedMapLight(ip_address)

    # Entität zu Home Assistant hinzufügen
    await hass.helpers.entity_platform.async_add_entities([EnjoyTheWoodLedMapLight(ip_address)])
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the Enjoy the Wood LED Map integration."""
    _LOGGER.info("Unloading Enjoy the Wood LED Map integration.")
    return True
