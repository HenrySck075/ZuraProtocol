from . import _ok as base

class DOMDebugger(base.sendhelp):

    method_GetEventListeners:str
    method_RemoveDOMBreakpoint:str
    method_RemoveEventListenerBreakpoint:str
    method_RemoveXHRBreakpoint:str
    method_SetDOMBreakpoint:str
    method_SetEventListenerBreakpoint:str
    method_SetXHRBreakpoint:str
    method_RemoveInstrumentationBreakpoint:str
    method_SetBreakOnCSPViolation:str
    method_SetInstrumentationBreakpoint:str

    type_DOMBreakpointType:str
    type_EventListener:str
    type_CSPViolationType:str

    def __init__(self):
        super().__init__()

    
domain = DOMDebugger()