import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class EnjoyTheWoodConfigFlow(config_entries.ConfigFlow):
    """Handle a config flow for Enjoy the Wood LED Map."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        if user_input is not None:
            ip_address = user_input.get(CONF_IP_ADDRESS)
            # Hier könnte weitere Logik für IP-Validierung hinzugefügt werden
            return self.async_create_entry(
                title="Enjoy the Wood LED Map", data={"ip_address": ip_address}
            )

        # Wenn der Benutzer noch keine Eingabe gemacht hat, Formular anzeigen
        return self.async_show_form(
            step_id="user", data_schema=self._get_user_input_schema()
        )

    def _get_user_input_schema(self):
        """Return the schema for user input."""
        return vol.Schema(
            {
                vol.Required(CONF_IP_ADDRESS): str,
            }
        )
