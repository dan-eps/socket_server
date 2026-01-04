from device import Device, create_device_from_config
import json

HOST = '127.0.0.1'
PORT = 12345

bluray_commands = ["PLAY=ON"]

if __name__ == '__main__':

    try:
        with open('device_types.json', 'r') as file:
            devices_configs = json.load(file).get('device_types')
    except FileNotFoundError:
        print("Error: The file 'device_types.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

    
    all_devices = {}
    for device_config in devices_configs:
        device = create_device_from_config(device_config)
        all_devices[device.port] = device

    bluray_player = all_devices[101]
    for command in bluray_commands:
        

