#!/usr/bin/python3
import broadlink
import sys
import json

DEVICE_IP = sys.argv[1]
DEVICE_PORT = 80
DEVICE_TYPE = 0x653c
DEVICE_MAC = sys.argv[2]

device = broadlink.gendevice(DEVICE_TYPE, (DEVICE_IP, DEVICE_PORT), DEVICE_MAC)
device.auth()
data = device.check_sensors()

result_json = {
    "Temp": data['temperature'],
    "Hum": data['humidity']
}

print(json.dumps(result_json))
