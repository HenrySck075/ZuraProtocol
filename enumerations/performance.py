from . import _ok as base

class Performance(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetMetrics:str
    method_SetTimeDomain:str

    event_Metrics:str

    type_Metric:str

    def __init__(self):
        super().__init__()

    
domain = Performance()