
from . import _ok as base

class Profiler(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetBestEffortCoverage:str
    method_SetSamplingInterval:str
    method_Start:str
    method_StartPreciseCoverage:str
    method_Stop:str
    method_StopPreciseCoverage:str
    method_TakePreciseCoverage:str

    event_ConsoleProfileFinished:str
    event_ConsoleProfileStarted:str
    event_PreciseCoverageDeltaUpdate:str

    type_CoverageRange:str
    type_FunctionCoverage:str
    type_PositionTickInfo:str
    type_Profile:str
    type_ProfileNode:str
    type_ScriptCoverage:str

    def __init__(self):
        super().__init__()

    
domain = Profiler()