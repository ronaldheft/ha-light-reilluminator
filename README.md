# HA Light Reilluminator

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

This Home Assistant integration records the history of light attributes, such as brightness or color temperature, in your recorder database.

Home Assistant used to record these attributes by default, but [since 2024.8, the attributes have been removed from the recorder history](https://github.com/home-assistant/core/pull/121776). This integration restores them.

## Why Record Light Attributes?

The primary reason is for accurate light presence simulation. Knowing the historic brightness and color temperature of your lights makes for a more convincing simulation.

This integration was built to be used alongside [the component presence_simulation](https://github.com/slashback100/presence_simulation), but it will work for any uses case that needs light attributes from Home Assistant's recorder database.

## Downsides to Recording Light Attributes

Home Assistant originally [removed light attributes because they can take up significant space in your recorder database](https://github.com/home-assistant/core/pull/121776). They specifically called out:

>We have at least three cases where we can generate a massive amount of data in state_attributes:
>
> - Automations that frequently change light colors
> - Lights that report color changes during effects
> - Custom integrations like adaptive lighting that frequently change color temp

If these situations do not apply to you or you [configure filters to exclude lights with frequent state changes](https://www.home-assistant.io/integrations/recorder/#configure-filter) (for example, Hue lights synced to your TV), the storage requirements for light attributes are minimal.

# Installation

## Option 1: HACS (recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ronaldheft&repository=ha-light-reilluminator&category=integration)

## Option 2: Manual

1. In your Home Assistant configuration directory (`~/.homeassistant` for instance), create a directory `custom_components/light_reilluminator` and put the code in it.
2. Restart Home Assistant

# Configuration

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=light_reilluminator)

1. Add the integration via the above link
2. Follow the directions and restart Home Assistant
3. After restart, light attributes will start being recorded in the recorder database
4. Remember it will take some time to accumulate a history for presence simulation