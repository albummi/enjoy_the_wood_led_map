import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_component import async_add_entities
from .light import EnjoyTheWoodLedMapLight
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Set up Enjoy the Wood LED Map from a config entry."""
    ip_address = entry.data.get("ip_address")
    
    # Erstelle eine Instanz für das LED Map und füge sie hinzu
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = ip_address
    
    # Füge die Entität zu Home Assistant hinzu
    await hass.config_entries.async_forward_entry_setup(entry, "light")

    return True

async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Unload Enjoy the Wood LED Map."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
