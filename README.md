# Socket Server
A socket-based server for testing TCP and RS-232 signals sent to audiovisual (AV) devices. It emulates device-specific responses to validate control logic. While capable of running independently, this server is part of MAVERICK, a comprehensive testing suite developed for Pershing Technologies.

## How It Works
Each device is added through the JSON configuration in the [device_types.json](device_types.json) file. Each device has the following attributes and properties:

### Device
- Attributes:
    - [Status Variables](#status-variables) : custom variables for each device, specific to each instance of a device
- Methods:
    - **Get** : get the value of any variable with specified name
    - **Set** : set the value of any variable with specified name
    - **Unset** : delete the value of variable with specified name
    - **Find** : find any variables with specified value
    - **Increment** : increment the value of specified variable
    - **Decrement** : decrement the value of specified variable

### Status Variables
Each device will have a key-value collection of status variables.
- Nested Values
    - status variables may also have nested key-value pairs
    - nested key-value pairs will be specified in the JSON config by using "." in the key name
    - e.g. In the example below, first name should be specified as "name.first"
        ```
        {
            "name": {
                "first": John
                "last": Doe
            }
        }
        ```


## Geting Started
Section Coming Soon

