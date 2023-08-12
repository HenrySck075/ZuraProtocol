from . import _ok as base

class Fetch(base.sendhelp):

    method_ContinueRequest:str
    method_ContinueWithAuth:str
    method_Disable:str
    method_Enable:str
    method_FailRequest:str
    method_FulfillRequest:str
    method_GetResponseBody:str
    method_TakeResponseBodyAsStream:str
    method_ContinueResponse:str

    event_AuthRequired:str
    event_RequestPaused:str

    type_AuthChallenge:str
    type_AuthChallengeResponse:str
    type_HeaderEntry:str
    type_RequestId:str
    type_RequestPattern:str
    type_RequestStage:str

    def __init__(self):
        super().__init__()

    
domain = Fetch()