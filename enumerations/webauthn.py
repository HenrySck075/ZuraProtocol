
from . import _ok as base

class WebAuthn(base.sendhelp):

    method_AddCredential:str
    method_AddVirtualAuthenticator:str
    method_ClearCredentials:str
    method_Disable:str
    method_Enable:str
    method_GetCredential:str
    method_GetCredentials:str
    method_RemoveCredential:str
    method_RemoveVirtualAuthenticator:str
    method_SetAutomaticPresenceSimulation:str
    method_SetResponseOverrideBits:str
    method_SetUserVerified:str

    event_CredentialAdded:str
    event_CredentialAsserted:str

    type_AuthenticatorId:str
    type_AuthenticatorProtocol:str
    type_AuthenticatorTransport:str
    type_Credential:str
    type_Ctap2Version:str
    type_VirtualAuthenticatorOptions:str

    def __init__(self):
        super().__init__()

    
domain = WebAuthn()