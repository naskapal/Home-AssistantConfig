# Home-AssistantConfig
# [![Build Status](https://travis-ci.org/unbornx/Home-AssistantConfig.svg?branch=master)](https://travis-ci.org/unbornx/Home-AssistantConfig) Home-Assistant Config by unbornx
[Home Assistant](https://home-assistant.io/) configuration files (YAMLs)

Based on CCOSTAN https://github.com/CCOSTAN/Home-AssistantConfig configs and hunterstee https://github.com/hunterstee/Home-Assistant

**Running Dockers :**

* Unifi controller - jacobalberty/unifi:latest
* Home Assistant - homeassistant/home-assistant:latest
* PI-Hole - diginc/pi-hole:latest
* Database for Home Assistant - mariadb:latest
* Harmony hub emulator - restful-harmony:latest
* HUE bridge emulator - bios/docker-alexa-ha-bridge:latest
* Docker manager - portainer/portainer
* deCONZ - Deconz docker for conbee zigbee gateway

Running those pretty much standard. I use MACVLAN so they can be on my local LAN.


**Devices**

* Philips HUE bridge v2
* Philips HUE color bulbs
* Philips HUE GU10 bulbs
* Philips HUE Wall switch
* Philips HUE white ambiance bulbs
* Yeelight LED strip, wifi controlled
* Supernight LED strip with wifi controller
* Nexlux LED strip with wifi controller
* Lighting Ever LED strip with wifi controller
* Amazon echo DOT
* Amcrests camera running on BlueIris
* Ubiquiti Unifi AP LR
* AEON labs Zwave USB stick
* AEON Labs window and door sensors
* Fibaro Z-Wave Motion Sensor - FGMS-001
* Logitech Harmony hub
* ConBee USB from Dresden Elektronik as Zigbee gateway
* Xiaomi Presence, temperature and water leak sensors

**TODO**

* Wall mounted tablets
* Amps and mixers for audio
