import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .light import EnjoyTheWoodLedMapLight
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Set up Enjoy the Wood LED Map from a config entry."""
    ip_address = entry.data.get("ip_address")
    
    # Hier könnte eine Instanziierung deiner Entität erfolgen, die die IP-Adresse benötigt
    # Beispiel: Es könnte ein Gerät für die Steuerung des LED Maps erstellt werden
    hass.data[DOMAIN] = EnjoyTheWoodLedMapLight(ip_address)
    
    # Die Entität zu Home Assistant hinzufügen
    await hass.helpers.entity_component.async_add_entities([hass.data[DOMAIN]])

    return True
