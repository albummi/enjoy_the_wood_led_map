from homeassistant.config_entries import ConfigEntry
from .light import async_setup_entry  # Korrekt importieren
from homeassistant.core import HomeAssistant

DOMAIN = "enjoy_the_wood_led_map"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Enjoy the Wood LED Map from a config entry."""
    # Registriere die Entität von light.py
    ip_address = entry.data["ip_address"]
    await async_setup_entry(hass, entry, hass.async_add_entities)
    return True
