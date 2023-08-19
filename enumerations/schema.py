from . import _ok as base

class Schema(base.sendhelp):

    method_GetDomains:str

    type_Domain:str

    def __init__(self):
        super().__init__()

    
domain = Schema()