
from . import _ok as base

class Media(base.sendhelp):

    method_Disable:str
    method_Enable:str

    event_PlayerErrorsRaised:str
    event_PlayerEventsAdded:str
    event_PlayerMessagesLogged:str
    event_PlayerPropertiesChanged:str
    event_PlayersCreated:str

    type_PlayerError:str
    type_PlayerErrorSourceLocation:str
    type_PlayerEvent:str
    type_PlayerId:str
    type_PlayerMessage:str
    type_PlayerProperty:str
    type_Timestamp:str

    def __init__(self):
        super().__init__()

    
