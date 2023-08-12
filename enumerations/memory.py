from . import _ok as base

class Memory(base.sendhelp):

    method_ForciblyPurgeJavaScriptMemory:str
    method_GetAllTimeSamplingProfile:str
    method_GetBrowserSamplingProfile:str
    method_GetDOMCounters:str
    method_GetSamplingProfile:str
    method_PrepareForLeakDetection:str
    method_SetPressureNotificationsSuppressed:str
    method_SimulatePressureNotification:str
    method_StartSampling:str
    method_StopSampling:str

    type_Module:str
    type_PressureLevel:str
    type_SamplingProfile:str
    type_SamplingProfileNode:str

    def __init__(self):
        super().__init__()

    
domain = Memory()