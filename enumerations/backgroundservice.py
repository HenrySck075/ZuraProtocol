
from . import _ok as base

class BackgroundService(base.sendhelp):

    method_ClearEvents:str
    method_SetRecording:str
    method_StartObserving:str
    method_StopObserving:str

    event_BackgroundServiceEventReceived:str
    event_RecordingStateChanged:str

    type_BackgroundServiceEvent:str
    type_EventMetadata:str
    type_ServiceName:str

    def __init__(self):
        super().__init__()

    
