from . import _ok as base

class Tracing(base.sendhelp):

    method_End:str
    method_GetCategories:str
    method_RecordClockSyncMarker:str
    method_RequestMemoryDump:str
    method_Start:str

    event_BufferUsage:str
    event_DataCollected:str
    event_TracingComplete:str

    type_MemoryDumpConfig:str
    type_MemoryDumpLevelOfDetail:str
    type_StreamCompression:str
    type_StreamFormat:str
    type_TraceConfig:str
    type_TracingBackend:str

    def __init__(self):
        super().__init__()

    
domain = Tracing()