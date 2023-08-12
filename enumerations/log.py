from . import _ok as base

class Log(base.sendhelp):

    method_Clear:str
    method_Disable:str
    method_Enable:str
    method_StartViolationsReport:str
    method_StopViolationsReport:str

    event_EntryAdded:str

    type_LogEntry:str
    type_ViolationSetting:str

    def __init__(self):
        super().__init__()

    
domain = Log()