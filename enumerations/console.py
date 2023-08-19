
from . import _ok as base

class Console(base.sendhelp):

    method_ClearMessages:str
    method_Disable:str
    method_Enable:str

    event_MessageAdded:str

    type_ConsoleMessage:str

    def __init__(self):
        super().__init__()

    
