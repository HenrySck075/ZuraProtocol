
from . import _ok as base

class Autofill(base.sendhelp):

    method_SetAddresses:str
    method_Trigger:str

    type_Address:str
    type_AddressField:str
    type_CreditCard:str

    def __init__(self):
        super().__init__()

    
