from . import _ok as base

class IO(base.sendhelp):

    method_Close:str
    method_Read:str
    method_ResolveBlob:str

    type_StreamHandle:str

    def __init__(self):
        super().__init__()

    
domain = IO()