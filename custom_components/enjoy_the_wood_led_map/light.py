from homeassistant.components.light import LightEntity

class EnjoyTheWoodLedMapLight(LightEntity):
    """Representation of Enjoy the Wood LED Map Light."""

    def __init__(self, ip_address: str):
        """Initialize the light entity."""
        self._ip_address = ip_address
        self._is_on = False

    @property
    def name(self):
        """Return the name of the light."""
        return "Enjoy the Wood LED Map"

    @property
    def is_on(self):
        """Return the status of the light."""
        return self._is_on

    async def async_turn_on(self, **kwargs):
        """Turn the light on."""
        # Logik zum Einschalten des LED Maps
        self._is_on = True
        self.schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the light off."""
        # Logik zum Ausschalten des LED Maps
        self._is_on = False
        self.schedule_update_ha_state()
