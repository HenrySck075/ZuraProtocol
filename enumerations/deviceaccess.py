
from . import _ok as base

class DeviceAccess(base.sendhelp):

    method_CancelPrompt:str
    method_Disable:str
    method_Enable:str
    method_SelectPrompt:str

    event_DeviceRequestPrompted:str

    type_DeviceId:str
    type_PromptDevice:str
    type_RequestId:str

    def __init__(self):
        super().__init__()

    
