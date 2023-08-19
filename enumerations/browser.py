from . import _ok as base

class Browser(base.sendhelp):

    method_AddPrivacySandboxEnrollmentOverride:str
    method_Close:str
    method_GetVersion:str
    method_CancelDownload:str
    method_Crash:str
    method_CrashGpuProcess:str
    method_ExecuteBrowserCommand:str
    method_GetBrowserCommandLine:str
    method_GetHistogram:str
    method_GetHistograms:str
    method_GetWindowBounds:str
    method_GetWindowForTarget:str
    method_GrantPermissions:str
    method_ResetPermissions:str
    method_SetDockTile:str
    method_SetDownloadBehavior:str
    method_SetPermission:str
    method_SetWindowBounds:str

    event_DownloadProgress:str
    event_DownloadWillBegin:str

    type_Bounds:str
    type_BrowserCommandId:str
    type_BrowserContextID:str
    type_Bucket:str
    type_Histogram:str
    type_PermissionDescriptor:str
    type_PermissionSetting:str
    type_PermissionType:str
    type_WindowID:str
    type_WindowState:str

    def __init__(self):
        super().__init__()

    
domain = Browser()