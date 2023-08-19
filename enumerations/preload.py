
from . import _ok as base

class Preload(base.sendhelp):

    method_Disable:str
    method_Enable:str

    event_PrefetchStatusUpdated:str
    event_PreloadEnabledStateUpdated:str
    event_PreloadingAttemptSourcesUpdated:str
    event_PrerenderAttemptCompleted:str
    event_PrerenderStatusUpdated:str
    event_RuleSetRemoved:str
    event_RuleSetUpdated:str

    type_PrefetchStatus:str
    type_PreloadingAttemptKey:str
    type_PreloadingAttemptSource:str
    type_PreloadingStatus:str
    type_PrerenderFinalStatus:str
    type_RuleSet:str
    type_RuleSetErrorType:str
    type_RuleSetId:str
    type_SpeculationAction:str
    type_SpeculationTargetHint:str

    def __init__(self):
        super().__init__()

    
