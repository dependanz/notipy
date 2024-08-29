import notipy

class NotipyBase:
    def __init__(self):
        self.channels = {
            'email' : notipy.email.Notify
        }
        
    def __getitem__(self, channel):
        return self.channels[channel]
        
Notify = NotipyBase()