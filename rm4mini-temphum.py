#!/usr/bin/python3
import broadlink
import sys
import json


def normalize_mac(value):
    return ''.join(c for c in value.lower() if c in '0123456789abcdef')

DEVICE_IP = sys.argv[1]
DEVICE_MAC = normalize_mac(sys.argv[2])

device = broadlink.hello(DEVICE_IP)
if device.mac.hex().lower() != DEVICE_MAC:
    raise RuntimeError('Discovered device MAC does not match configured MAC')

device.auth()
device.update()
data = device.check_sensors()

result_json = {
    "Temp": data['temperature'],
    "Hum": data['humidity'],
    "DeviceName": device.name,
    "DeviceType": device.get_type(),
    "Model": device.model,
    "Manufacturer": device.manufacturer,
    "ProductId": '0x%04X' % device.devtype,
    "FirmwareVersion": device.get_fwversion(),
    "Locked": int(device.is_locked)
}

print(json.dumps(result_json))
