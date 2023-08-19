
from . import _ok as base

class SystemInfo(base.sendhelp):

    method_GetFeatureState:str
    method_GetInfo:str
    method_GetProcessInfo:str

    type_GPUDevice:str
    type_GPUInfo:str
    type_ImageDecodeAcceleratorCapability:str
    type_ImageType:str
    type_ProcessInfo:str
    type_Size:str
    type_SubsamplingFormat:str
    type_VideoDecodeAcceleratorCapability:str
    type_VideoEncodeAcceleratorCapability:str

    def __init__(self):
        super().__init__()

    
