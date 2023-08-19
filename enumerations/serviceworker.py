
from . import _ok as base

class ServiceWorker(base.sendhelp):

    method_DeliverPushMessage:str
    method_Disable:str
    method_DispatchPeriodicSyncEvent:str
    method_DispatchSyncEvent:str
    method_Enable:str
    method_InspectWorker:str
    method_SetForceUpdateOnPageLoad:str
    method_SkipWaiting:str
    method_StartWorker:str
    method_StopAllWorkers:str
    method_StopWorker:str
    method_Unregister:str
    method_UpdateRegistration:str

    event_WorkerErrorReported:str
    event_WorkerRegistrationUpdated:str
    event_WorkerVersionUpdated:str

    type_RegistrationID:str
    type_ServiceWorkerErrorMessage:str
    type_ServiceWorkerRegistration:str
    type_ServiceWorkerVersion:str
    type_ServiceWorkerVersionRunningStatus:str
    type_ServiceWorkerVersionStatus:str

    def __init__(self):
        super().__init__()

    
