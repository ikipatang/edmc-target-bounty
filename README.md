# EDMC target bounty
An EDMC plugin for scanning ships and getting their bounty value

## Requirements
- [Elite Dangerous Market Connector (aka EDMC)](https://github.com/Marginal/EDMarketConnector/wiki/Installation-&-Setup)
- [EDMCOVerlay](https://github.com/inorton/EDMCOverlay/releases/latest)

**NB**: the project has been tested only on windows

## Usage
Target bounty will display on screen status clean or the bounty on locked target scan

**Supported** in **open**, **solo** and **private group** mode.

## Installation
- On EDMC's Plugins settings tab press the “Open” button. This reveals the plugins folder where EDMC looks for plugins
- Download the project ~~Download the latest release~~
- Open the `.zip` archive that you downloaded and move the `edmc-target-bounty` folder contained inside into the plugins folder

You will need to re-start EDMC for it to notice the new plugin.

## Features
- Display shipType, pilotName, pilotRank and shield status on locked target scan
- Display warning bounty value on locked target scan
- Display notice clear status on locked target scan

### TODO
I am no satisfied of the output for now       
I would prefer to have it in the edmc screen or under the scanned status
- Try to tweak 
  - [OmniScanner](https://github.com/seldonlabs/OmniScanner) to make it work in private/solo
  - [EDR](https://github.com/lekeno/edr/) to make it work in private/solo

## Versions
- 0.0.1: Initial version

## Thanks
- To Jonathan Harris for [EDMC][0]
- To Ian Norton for [EDMCOverlay][1] and [EDMCHits][2]

[0]:https://github.com/Marginal/EDMarketConnector
[1]:https://github.com/inorton/EDMCOverlay
[2]:https://github.com/inorton/EDMCHits




