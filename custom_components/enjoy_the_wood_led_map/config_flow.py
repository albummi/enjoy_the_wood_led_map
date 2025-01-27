from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.data_entry_flow import FlowResult

class EnjoyTheWoodConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for the Enjoy the Wood LED Map integration."""

    VERSION = 1

    def __init__(self):
        """Initialize the flow."""
        self.ip_address = None

    async def async_step_user(self, user_input=None):
        """Handle the user input for the configuration."""
        if user_input is not None:
            self.ip_address = user_input[CONF_IP_ADDRESS]
            return self.async_create_entry(
                title="Enjoy the Wood LED Map",
                data={CONF_IP_ADDRESS: self.ip_address},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str,
            }),
        )
