from . import _ok as base

class FedCm(base.sendhelp):

    method_Disable:str
    method_DismissDialog:str
    method_Enable:str
    method_ResetCooldown:str
    method_SelectAccount:str

    event_DialogShown:str

    type_Account:str
    type_DialogType:str
    type_LoginState:str

    def __init__(self):
        super().__init__()

    
domain = FedCm()