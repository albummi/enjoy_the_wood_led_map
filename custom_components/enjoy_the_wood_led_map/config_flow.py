import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

class EnjoyTheWoodConfigFlow(config_entries.ConfigFlow, domain="enjoy_the_wood_led_map"):
    """Handle a config flow for Enjoy the Wood LED Map integration."""

    async def async_step_user(self, user_input=None):
        """Handle the user configuration input."""
        if user_input is not None:
            # Speichern der IP-Adresse in der Konfiguration
            return self.async_create_entry(
                title="Enjoy the Wood LED Map", data={"ip_address": user_input["ip_address"]}
            )
        
        # Wenn noch keine Eingabe vorliegt, zeige das Formular
        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("ip_address"): str})
        )
