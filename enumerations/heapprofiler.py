from . import _ok as base

class HeapProfiler(base.sendhelp):

    method_AddInspectedHeapObject:str
    method_CollectGarbage:str
    method_Disable:str
    method_Enable:str
    method_GetHeapObjectId:str
    method_GetObjectByHeapObjectId:str
    method_GetSamplingProfile:str
    method_StartSampling:str
    method_StartTrackingHeapObjects:str
    method_StopSampling:str
    method_StopTrackingHeapObjects:str
    method_TakeHeapSnapshot:str

    event_AddHeapSnapshotChunk:str
    event_HeapStatsUpdate:str
    event_LastSeenObjectId:str
    event_ReportHeapSnapshotProgress:str
    event_ResetProfiles:str

    type_HeapSnapshotObjectId:str
    type_SamplingHeapProfile:str
    type_SamplingHeapProfileNode:str
    type_SamplingHeapProfileSample:str

    def __init__(self):
        super().__init__()

    
domain = HeapProfiler()