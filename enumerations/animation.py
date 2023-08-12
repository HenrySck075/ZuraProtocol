from . import _ok as base

class Animation(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetCurrentTime:str
    method_GetPlaybackRate:str
    method_ReleaseAnimations:str
    method_ResolveAnimation:str
    method_SeekAnimations:str
    method_SetPaused:str
    method_SetPlaybackRate:str
    method_SetTiming:str

    event_AnimationCanceled:str
    event_AnimationCreated:str
    event_AnimationStarted:str

    type_Animation:str
    type_AnimationEffect:str
    type_KeyframesRule:str
    type_KeyframeStyle:str

    def __init__(self):
        super().__init__()

    
domain = Animation()