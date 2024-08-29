import yaml
from .email import Notify as NotifyEmail
from .phone import Notify as NotifyPhone

def parse_config(config_file):
    # Read config yaml
    with open(config_file, 'r') as fp:
        try:
            config = yaml.safe_load(fp)
        except yaml.YAMLError as exc:
            print(exc)
    return config

class NotipyBase:
    def __init__(self):
        self.channels = {
            'email' : NotifyEmail,
            'phone' : NotifyPhone
        }
        
    def __getitem__(self, channel):
        return self.channels[channel]
        
Notify = NotipyBase()