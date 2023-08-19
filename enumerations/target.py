
from . import _ok as base

class Target(base.sendhelp):

    method_ActivateTarget:str
    method_AttachToTarget:str
    method_CloseTarget:str
    method_CreateTarget:str
    method_DetachFromTarget:str
    method_GetTargets:str
    method_SetDiscoverTargets:str
    method_SendMessageToTarget:str
    method_AttachToBrowserTarget:str
    method_AutoAttachRelated:str
    method_CreateBrowserContext:str
    method_DisposeBrowserContext:str
    method_ExposeDevToolsProtocol:str
    method_GetBrowserContexts:str
    method_GetTargetInfo:str
    method_SetAutoAttach:str
    method_SetRemoteLocations:str

    event_ReceivedMessageFromTarget:str
    event_TargetCrashed:str
    event_TargetCreated:str
    event_TargetDestroyed:str
    event_TargetInfoChanged:str
    event_AttachedToTarget:str
    event_DetachedFromTarget:str

    type_SessionID:str
    type_TargetID:str
    type_TargetInfo:str
    type_FilterEntry:str
    type_RemoteLocation:str
    type_TargetFilter:str

    def __init__(self):
        super().__init__()

    
domain = Target()