from device import Device, create_device_from_config
import json

HOST = '127.0.0.1'
PORT = 12345

if __name__ == '__main__':

    try:
        with open('device_types.json', 'r') as file:
            devices_configs = json.load(file).get('device_types')
    except FileNotFoundError:
        print("Error: The file 'device_types.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

    

    for device_config in devices_configs:
        device = create_device_from_config(device_config)
        print(device)

