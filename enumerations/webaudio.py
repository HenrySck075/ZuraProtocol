from . import _ok as base

class WebAudio(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetRealtimeData:str

    event_AudioListenerCreated:str
    event_AudioListenerWillBeDestroyed:str
    event_AudioNodeCreated:str
    event_AudioNodeWillBeDestroyed:str
    event_AudioParamCreated:str
    event_AudioParamWillBeDestroyed:str
    event_ContextChanged:str
    event_ContextCreated:str
    event_ContextWillBeDestroyed:str
    event_NodeParamConnected:str
    event_NodeParamDisconnected:str
    event_NodesConnected:str
    event_NodesDisconnected:str

    type_AudioListener:str
    type_AudioNode:str
    type_AudioParam:str
    type_AutomationRate:str
    type_BaseAudioContext:str
    type_ChannelCountMode:str
    type_ChannelInterpretation:str
    type_ContextRealtimeData:str
    type_ContextState:str
    type_ContextType:str
    type_GraphObjectId:str
    type_NodeType:str
    type_ParamType:str

    def __init__(self):
        super().__init__()

    
domain = WebAudio()