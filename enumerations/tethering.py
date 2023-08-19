
from . import _ok as base

class Tethering(base.sendhelp):

    method_Bind:str
    method_Unbind:str

    event_Accepted:str

    def __init__(self):
        super().__init__()

    
