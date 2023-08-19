
from . import _ok as base

class Inspector(base.sendhelp):

    method_Disable:str
    method_Enable:str

    event_Detached:str
    event_TargetCrashed:str
    event_TargetReloadedAfterCrash:str

    def __init__(self):
        super().__init__()

    
