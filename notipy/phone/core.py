import notipy

CARRIER_MAP = {
    "att"     : "mms.att.net",
    "tmobile" : "tmomail.net",
    "verizon" : "vtext.com",
    "sprint"  : "messaging.sprintpcs.com"
}

def Notify(config):
    # [TODO] Validate config has phone number destination
    if 'destination' not in config:
        raise ValueError('config file must have a destination')
    
    # Convert destination to an email
    if 'carrier' not in config:
        raise ValueError('config file must have a carrier label')
    config['destination'] = config['destination'] + '@' + CARRIER_MAP[config['carrier']]
    
    # Notify as email
    notipy.Notify['email'](
        config = config
    )