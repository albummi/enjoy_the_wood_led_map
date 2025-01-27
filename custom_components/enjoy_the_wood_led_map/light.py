from homeassistant.components.light import LightEntity
import requests

class EnjoyTheWoodLedMapLight(LightEntity):
    """Representation of the Enjoy the Wood LED Map as a light entity."""

    def __init__(self, ip_address):
        """Initialize the light entity."""
        self._ip_address = ip_address
        self._state = False
        self._effect = None
        self._color = None

    @property
    def name(self):
        """Return the name of the light."""
        return "Enjoy the Wood LED Map"

    @property
    def is_on(self):
        """Return if the LED map is on or off."""
        return self._state

    @property
    def effect_list(self):
        """Return the list of available effects."""
        return [
            "RainbowLoop", "Strobe", "TheaterChase", "Sparkle", "RunningLights",
            "RainbowTwinkle", "RgbPropeller", "RandomColorPop", "PopLeftRight",
            "SinWaveBrightness", "MarchRandomColors", "VerticalSomething",
            "PulseColorSaturation", "PulseColorBrightness", "StripFlicker", "CycloneTwo", "RandomBurst"
        ]

    @property
    def effect(self):
        """Return the current effect."""
        return self._effect

    async def async_turn_on(self, **kwargs):
        """Turn on the LED map."""
        self._state = True
        requests.get(f"http://{self._ip_address}/?cmd=on")

        if EFFECT := kwargs.get("effect"):
            self._effect = EFFECT
            requests.get(f"http://{self._ip_address}/?cmd={self._effect}")
        
        if COLOR := kwargs.get("rgb_color"):
            self._color = COLOR
            # Hier könnte die Farbe an die LED-Karte gesendet werden

    async def async_turn_off(self, **kwargs):
        """Turn off the LED map."""
        self._state = False
        self._effect = None
        self._color = None
        requests.get(f"http://{self._ip_address}/?cmd=off")
