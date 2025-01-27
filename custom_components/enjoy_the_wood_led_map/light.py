import logging
import aiohttp
from homeassistant.components.light import LightEntity, COLOR_MODE_ONOFF
from homeassistant.const import CONF_IP_ADDRESS

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Enjoy the Wood LED Map as a light entity."""
    ip_address = entry.data[CONF_IP_ADDRESS]
    async_add_entities([EnjoyTheWoodLedMapLight(ip_address)])


class EnjoyTheWoodLedMapLight(LightEntity):
    """Representation of the Enjoy the Wood LED Map as a light entity."""

    def __init__(self, ip_address):
        """Initialize the light entity."""
        self._ip_address = ip_address
        self._state = False
        self._effect = None

    @property
    def name(self):
        """Return the name of the light."""
        return "Enjoy the Wood LED Map"

    @property
    def is_on(self):
        """Return if the LED map is on or off."""
        return self._state

    @property
    def supported_color_modes(self):
        """Return the list of supported color modes."""
        return {COLOR_MODE_ONOFF}

    @property
    def color_mode(self):
        """Return the current color mode."""
        return COLOR_MODE_ONOFF

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
        async with aiohttp.ClientSession() as session:
            await session.get(f"http://{self._ip_address}/?cmd=on")

        if effect := kwargs.get("effect"):
            self._effect = effect
            async with aiohttp.ClientSession() as session:
                await session.get(f"http://{self._ip_address}/?cmd={self._effect}")

    async def async_turn_off(self, **kwargs):
        """Turn off the LED map."""
        self._state = False
        self._effect = None
        async with aiohttp.ClientSession() as session:
            await session.get(f"http://{self._ip_address}/?cmd=off")
