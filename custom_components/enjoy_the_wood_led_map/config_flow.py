import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

class EnjoyTheWoodConfigFlow(config_entries.ConfigFlow, domain="enjoy_the_wood_led_map"):
    """Handle a config flow for Enjoy the Wood LED Map integration."""

    async def async_step_user(self, user_input=None):
        """Handle the user configuration input."""
        if user_input is not None:
            ip_address = user_input.get("ip_address")
            if ip_address:
                _LOGGER.info("User provided IP address: %s", ip_address)
                # Return a successful configuration entry
                return self.async_create_entry(
                    title="Enjoy the Wood LED Map", data={"ip_address": ip_address}
                )
            else:
                _LOGGER.error("IP address is missing from user input.")
                return self.async_show_form(
                    step_id="user",
                    data_schema=vol.Schema({vol.Required("ip_address"): str}),
                    errors={"base": "IP address is required"}
                )
        
        # If no user input yet, show the form
        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("ip_address"): str})
        )
