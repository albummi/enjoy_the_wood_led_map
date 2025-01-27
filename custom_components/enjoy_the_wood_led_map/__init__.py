from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .light import EnjoyTheWoodLedMapLight  # Importiere die Entität

DOMAIN = "enjoy_the_wood_led_map"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Enjoy the Wood LED Map from a config entry."""
    ip_address = entry.data["ip_address"]
    
    # Entität für die LED-Karte erstellen und zur Home Assistant-Instanz hinzufügen
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = EnjoyTheWoodLedMapLight(ip_address)
    
    # Rückgabe der erfolgreichen Registrierung der Entität
    await hass.helpers.entity_component.async_add_entities([EnjoyTheWoodLedMapLight(ip_address)])
    
    return True
