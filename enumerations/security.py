from . import _ok as base

class Security(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_HandleCertificateError:str
    method_SetOverrideCertificateErrors:str
    method_SetIgnoreCertificateErrors:str

    event_CertificateError:str
    event_SecurityStateChanged:str
    event_VisibleSecurityStateChanged:str

    type_CertificateErrorAction:str
    type_CertificateId:str
    type_MixedContentType:str
    type_SecurityState:str
    type_SecurityStateExplanation:str
    type_InsecureContentStatus:str
    type_CertificateSecurityState:str
    type_SafetyTipInfo:str
    type_SafetyTipStatus:str
    type_VisibleSecurityState:str

    def __init__(self):
        super().__init__()

    
domain = Security()