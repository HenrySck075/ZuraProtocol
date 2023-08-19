
from . import _ok as base

class Cast(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_SetSinkToUse:str
    method_StartDesktopMirroring:str
    method_StartTabMirroring:str
    method_StopCasting:str

    event_IssueUpdated:str
    event_SinksUpdated:str

    type_Sink:str

    def __init__(self):
        super().__init__()

    
