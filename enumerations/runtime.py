
from . import _ok as base

class Runtime(base.sendhelp):

    method_AwaitPromise:str
    method_CallFunctionOn:str
    method_CompileScript:str
    method_Disable:str
    method_DiscardConsoleEntries:str
    method_Enable:str
    method_Evaluate:str
    method_GetProperties:str
    method_GlobalLexicalScopeNames:str
    method_QueryObjects:str
    method_ReleaseObject:str
    method_ReleaseObjectGroup:str
    method_RunIfWaitingForDebugger:str
    method_RunScript:str
    method_SetAsyncCallStackDepth:str
    method_AddBinding:str
    method_GetExceptionDetails:str
    method_GetHeapUsage:str
    method_GetIsolateId:str
    method_RemoveBinding:str
    method_SetCustomObjectFormatterEnabled:str
    method_SetMaxCallStackSizeToCapture:str
    method_TerminateExecution:str

    event_ConsoleAPICalled:str
    event_ExceptionRevoked:str
    event_ExceptionThrown:str
    event_ExecutionContextCreated:str
    event_ExecutionContextDestroyed:str
    event_ExecutionContextsCleared:str
    event_InspectRequested:str
    event_BindingCalled:str

    type_CallArgument:str
    type_CallFrame:str
    type_DeepSerializedValue:str
    type_ExceptionDetails:str
    type_ExecutionContextDescription:str
    type_ExecutionContextId:str
    type_InternalPropertyDescriptor:str
    type_PropertyDescriptor:str
    type_RemoteObject:str
    type_RemoteObjectId:str
    type_ScriptId:str
    type_SerializationOptions:str
    type_StackTrace:str
    type_TimeDelta:str
    type_Timestamp:str
    type_UnserializableValue:str
    type_CustomPreview:str
    type_EntryPreview:str
    type_ObjectPreview:str
    type_PrivatePropertyDescriptor:str
    type_PropertyPreview:str
    type_StackTraceId:str
    type_UniqueDebuggerId:str

    def __init__(self):
        super().__init__()

    
