from . import _ok as base

class HeadlessExperimental(base.sendhelp):

    method_BeginFrame:str
    method_Disable:str
    method_Enable:str

    type_ScreenshotParams:str

    def __init__(self):
        super().__init__()

    
domain = HeadlessExperimental()