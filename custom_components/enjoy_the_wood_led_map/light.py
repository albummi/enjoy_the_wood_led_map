import logging
import requests
from homeassistant.components.light import LightEntity
from homeassistant.const import CONF_IP_ADDRESS

_LOGGER = logging.getLogger(__name__)

DOMAIN = "enjoy_the_wood_led_map"
DEFAULT_NAME = "Enjoy the Wood LED Map"

class EnjoyTheWoodLedMapLight(LightEntity):
    """Representation of the Enjoy the Wood LED Map as a light entity."""

    def __init__(self, ip_address):
        """Initialize the light."""
        self._ip_address = ip_address
        self._name = DEFAULT_NAME
        self._is_on = False
        self._effect = None
        self._color = None

    @property
    def name(self):
        """Return the name of the light."""
        return self._name

    @property
    def is_on(self):
        """Return if the light is on."""
        return self._is_on

    @property
    def effect_list(self):
        """Return the list of available effects."""
        return [
            "RainbowLoop", "Strobe", "theaterChase", "Sparkle", "RunningLights",
            "RainbowTwinkle", "RgbPropeller", "RandomColorPop", "PopLeftRight",
            "SinWaveBrightness", "MarchRandomColors", "VerticalSomething",
            "PulseColorSaturation", "PulseColorBrightness", "StripFflicker",
            "CycloneTwo", "RandomBurst"
        ]

    @property
    def effect(self):
        """Return the current effect."""
        return self._effect

    @property
    def rgb_color(self):
        """Return the color of the light."""
        return self._color

    async def async_turn_on(self, **kwargs):
        """Turn on the light."""
        self._is_on = True
        await self._send_command("on")

        if "rgb_color" in kwargs:
            self._color = kwargs["rgb_color"]
            # You can add logic to convert RGB to a specific format for the LED map if needed.

        if "effect" in kwargs:
            self._effect = kwargs["effect"]
            await self._set_effect(self._effect)

    async def async_turn_off(self, **kwargs):
        """Turn off the light."""
        self._is_on = False
        await self._send_command("off")

    async def _send_command(self, command):
        """Send a command to the LED map via HTTP."""
        url = f"http://{self._ip_address}/?cmd={command}"
        try:
            response = requests.get(url)
            _LOGGER.debug(f"Command {command} sent to {self._ip_address}: {response.status_code}")
        except requests.RequestException as e:
            _LOGGER.error(f"Error sending command to {self._ip_address}: {e}")

    async def _set_effect(self, effect):
        """Set the effect on the LED map."""
        if effect in self.effect_list:
            await self._send_command(effect)
