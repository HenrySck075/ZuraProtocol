
from . import _ok as base

class DeviceOrientation(base.sendhelp):

    method_ClearDeviceOrientationOverride:str
    method_SetDeviceOrientationOverride:str

    def __init__(self):
        super().__init__()

    
