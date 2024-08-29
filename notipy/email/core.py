from .gmail import *

def Notify(config):    
    #######################################
    # Validate source domain credentials 
    #######################################
    source_domain = config['source'].split('@')[-1]
    destination_domain = config['destination'].split('@')[-1]

    if source_domain == 'gmail.com':
        assert 'gmail_app_pass' in config
        assert config['gmail_app_pass'] is not None
        if 'messages' not in config:
            config['messages'] = []
        if 'label' not in config:
            config['label'] = 'notipy'
        if 'subject' not in config:
            config['subject'] = 'Processed Finished'
        send_gmail(
            source       = config['source'],
            destination  = config['destination'],
            app_password = config['gmail_app_pass'],
            label        = config['label'],
            subject      = config['subject'],
            messages     = [msg for msg in [*config['messages']] if msg is not None]
        )
    else:
        raise ValueError("Unsupported source address domain")
        