## Idea of wake on lan
You come home tired from working at Macdonald, you take a shower, grab some food
and come to your only escape from reality, that is your home computer that is already
turned on! As far as I know, this is one use case for this script. Maybe YOU will find some other? I would love to hear some ideas.


## Instructions first time running
This script is meant to run on Raspberry Pi Zero W.
Clone-copy this repository and run the script.
It will ask for 3 things the first time it runs.

- Your pc ip address on which the script is going to check if it's Running or Sleeping.
- Your phone ip address to check if it's connected to your home router.
- Your pc MAC address which will be used to wake it up from sleep.

After that it will save your settings in a file

## Requirements
- Your home computer.
- Raspberry Pi device / Smaller the better / Will run in background constantly.
- Home Wifi
- Setting up 'Wake on lan' in your bios.

## How to set up Wake on lan on your bios
```
Press {BIOS KEY} during boot to enter BIOS Setup.

Go to the Power menu.

Set Wake-on-LAN to Power On.

Save and exit the BIOS Setup.
```
