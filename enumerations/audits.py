from . import _ok as base

class Audits(base.sendhelp):

    method_CheckContrast:str
    method_CheckFormsIssues:str
    method_Disable:str
    method_Enable:str
    method_GetEncodedResponse:str

    event_IssueAdded:str

    type_AffectedCookie:str
    type_AffectedFrame:str
    type_AffectedRequest:str
    type_AttributionReportingIssueDetails:str
    type_AttributionReportingIssueType:str
    type_BlockedByResponseIssueDetails:str
    type_BlockedByResponseReason:str
    type_BounceTrackingIssueDetails:str
    type_ClientHintIssueDetails:str
    type_ClientHintIssueReason:str
    type_ContentSecurityPolicyIssueDetails:str
    type_ContentSecurityPolicyViolationType:str
    type_CookieExclusionReason:str
    type_CookieIssueDetails:str
    type_CookieOperation:str
    type_CookieWarningReason:str
    type_CorsIssueDetails:str
    type_DeprecationIssueDetails:str
    type_FailedRequestInfo:str
    type_FederatedAuthRequestIssueDetails:str
    type_FederatedAuthRequestIssueReason:str
    type_FederatedAuthUserInfoRequestIssueDetails:str
    type_FederatedAuthUserInfoRequestIssueReason:str
    type_GenericIssueDetails:str
    type_GenericIssueErrorType:str
    type_HeavyAdIssueDetails:str
    type_HeavyAdReason:str
    type_HeavyAdResolutionStatus:str
    type_InspectorIssue:str
    type_InspectorIssueCode:str
    type_InspectorIssueDetails:str
    type_IssueId:str
    type_LowTextContrastIssueDetails:str
    type_MixedContentIssueDetails:str
    type_MixedContentResolutionStatus:str
    type_MixedContentResourceType:str
    type_QuirksModeIssueDetails:str
    type_SharedArrayBufferIssueDetails:str
    type_SharedArrayBufferIssueType:str
    type_SourceCodeLocation:str
    type_StylesheetLoadingIssueDetails:str
    type_StyleSheetLoadingIssueReason:str
    type_NavigatorUserAgentIssueDetails:str

    def __init__(self):
        super().__init__()

    
domain = Audits()