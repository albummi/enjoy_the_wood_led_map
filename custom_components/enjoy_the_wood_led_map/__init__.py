from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import discovery
from .light import async_setup_entry  # Importiere async_setup_entry von der light.py

DOMAIN = "enjoy_the_wood_led_map"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    # Hier kannst du globale Setup-Prozesse durchführen, wenn nötig
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Enjoy the Wood LED Map from a config entry."""
    # Hier registrierst du die Entität für die LED-Karte
    ip_address = entry.data["ip_address"]
    hass.data.setdefault(DOMAIN, {})
    # Registriere die Entität als "light"
    await async_setup_entry(hass, entry, hass.async_add_entities)

    # Optional: Zusätzliche Logik für das Setup, falls benötigt
    return True
