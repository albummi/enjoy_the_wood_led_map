import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Set up Enjoy the Wood LED Map from a config entry."""
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    ip_address = entry.data.get("ip_address")
    hass.data[DOMAIN][entry.entry_id] = ip_address

    # Füge die Entität zu Home Assistant hinzu
    await hass.config_entries.async_forward_entry_setup(entry, "light")

    return True

async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Unload Enjoy the Wood LED Map."""
    if entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)
    return True
