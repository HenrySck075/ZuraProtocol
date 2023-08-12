from . import _ok as base

class EventBreakpoints(base.sendhelp):

    method_RemoveInstrumentationBreakpoint:str
    method_SetInstrumentationBreakpoint:str

    def __init__(self):
        super().__init__()

    
domain = EventBreakpoints()