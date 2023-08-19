from . import _ok as base

class Emulation(base.sendhelp):

    method_CanEmulate:str
    method_ClearDeviceMetricsOverride:str
    method_ClearGeolocationOverride:str
    method_SetDefaultBackgroundColorOverride:str
    method_SetDeviceMetricsOverride:str
    method_SetEmulatedMedia:str
    method_SetGeolocationOverride:str
    method_SetScriptExecutionDisabled:str
    method_SetTouchEmulationEnabled:str
    method_SetUserAgentOverride:str
    method_ClearIdleOverride:str
    method_ResetPageScaleFactor:str
    method_SetAutoDarkModeOverride:str
    method_SetAutomationOverride:str
    method_SetCPUThrottlingRate:str
    method_SetDisabledImageTypes:str
    method_SetDocumentCookieDisabled:str
    method_SetEmitTouchEventsForMouse:str
    method_SetEmulatedVisionDeficiency:str
    method_SetFocusEmulationEnabled:str
    method_SetHardwareConcurrencyOverride:str
    method_SetIdleOverride:str
    method_SetLocaleOverride:str
    method_SetPageScaleFactor:str
    method_SetScrollbarsHidden:str
    method_SetTimezoneOverride:str
    method_SetVirtualTimePolicy:str
    method_SetNavigatorOverrides:str
    method_SetVisibleSize:str

    event_VirtualTimeBudgetExpired:str

    type_DisplayFeature:str
    type_MediaFeature:str
    type_ScreenOrientation:str
    type_DisabledImageType:str
    type_UserAgentBrandVersion:str
    type_UserAgentMetadata:str
    type_VirtualTimePolicy:str

    def __init__(self):
        super().__init__()

    
domain = Emulation()