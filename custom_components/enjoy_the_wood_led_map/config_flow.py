from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN  # Stelle sicher, dass `DOMAIN` korrekt definiert ist


class EnjoyTheWoodLedMapConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Enjoy the Wood LED Map."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Validate user input here (z. B. die IP-Adresse prüfen)
            return self.async_create_entry(title="Enjoy the Wood LED Map", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=self._get_user_input_schema()
        )

    def _get_user_input_schema(self):
        """Return the schema for user input."""
        import voluptuous as vol
        return vol.Schema({
            vol.Required("ip_address"): str,
        })
