from homeassistant.core import HomeAssistant

DOMAIN = "enjoy_the_wood_led_map"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Enjoy the Wood LED Map integration."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up Enjoy the Wood LED Map from a config entry."""
    # Hier kannst du deinen Integrationsstart hinzufügen
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    return True


async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload Enjoy the Wood LED Map."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
