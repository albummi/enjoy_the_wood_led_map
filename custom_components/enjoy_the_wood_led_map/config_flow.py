from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class EnjoyTheWoodLedMapConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Enjoy the Wood LED Map."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Enjoy the Wood LED Map", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str,
            })
        )
