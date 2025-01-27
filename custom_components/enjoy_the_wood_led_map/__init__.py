import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    _LOGGER.debug("Setting up the Enjoy the Wood LED Map integration")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Set up Enjoy the Wood LED Map from a config entry."""
    _LOGGER.debug(f"Setting up entry: {entry.data}")

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    ip_address = entry.data.get("ip_address")
    hass.data[DOMAIN][entry.entry_id] = ip_address

    # Check if the entry is already set up
    if entry.entry_id in hass.data[DOMAIN]:
        _LOGGER.warning(f"Config entry {entry.entry_id} for {DOMAIN} has already been set up!")
        return False

    # Forward the setup to the light platform
    await hass.config_entries.async_forward_entry_setups(entry, ["light"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Unload Enjoy the Wood LED Map."""
    _LOGGER.debug(f"Unloading entry: {entry.data}")

    if entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    await hass.config_entries.async_forward_entry_unload(entry, "light")
    return True
