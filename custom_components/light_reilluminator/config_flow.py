"""Adds config flow."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from homeassistant.data_entry_flow import FlowResult

import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class LightReilluminatorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Light Reilluminator."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step initiated by the user."""
        # Enforce single instance
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        # No config needed; just a confirmation screen
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({}),
            )

        # Create the single config entry
        return self.async_create_entry(
            title="Light Reilluminator",
            data={},
        )
