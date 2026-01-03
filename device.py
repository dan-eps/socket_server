from status_variable import StatusVariable 
from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)

def set_dotted(d, path, value):
    cur = d
    for k in path.split(".")[:-1]:
        cur = cur.setdefault(k, {})
    cur[path.split(".")[-1]] = value


class Device:
    def __init__(self, name: str, port: int, status_variables: dict):
        self.__name = name
        self.__port = port
        self.__status_variables = status_variables
    
    @property
    def name(self):
        return self.__name
    
    @property
    def port(self):
        return self.__port
    
    @property
    def vars(self):
        return self.__status_variables

    def __str__(self) -> str:
        d_string = ", ".join([str(self.vars[k]) for k in self.vars])
        return f"{self.name} / Port: {self.port} / Vars: {d_string}"


def create_device_from_config(config) -> Device:
    status_variables = nested_dict()
    for key in (sv := config["status_variables"]):
        set_dotted(status_variables, key, StatusVariable(key, sv[key].get("default", None), sv[key].get("valid_values", None)))
    d = Device(name=config["name"], port=config["port"], status_variables=status_variables)
    return d