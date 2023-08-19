from . import _ok as base

class Debugger(base.sendhelp):

    method_ContinueToLocation:str
    method_Disable:str
    method_Enable:str
    method_EvaluateOnCallFrame:str
    method_GetPossibleBreakpoints:str
    method_GetScriptSource:str
    method_Pause:str
    method_RemoveBreakpoint:str
    method_RestartFrame:str
    method_Resume:str
    method_SearchInContent:str
    method_SetAsyncCallStackDepth:str
    method_SetBreakpoint:str
    method_SetBreakpointByUrl:str
    method_SetBreakpointsActive:str
    method_SetInstrumentationBreakpoint:str
    method_SetPauseOnExceptions:str
    method_SetScriptSource:str
    method_SetSkipAllPauses:str
    method_SetVariableValue:str
    method_StepInto:str
    method_StepOut:str
    method_StepOver:str
    method_GetWasmBytecode:str
    method_DisassembleWasmModule:str
    method_GetStackTrace:str
    method_NextWasmDisassemblyChunk:str
    method_SetBlackboxedRanges:str
    method_SetBlackboxPatterns:str
    method_SetBreakpointOnFunctionCall:str
    method_SetReturnValue:str
    method_PauseOnAsyncCall:str

    event_BreakpointResolved:str
    event_Paused:str
    event_Resumed:str
    event_ScriptFailedToParse:str
    event_ScriptParsed:str

    type_BreakLocation:str
    type_BreakpointId:str
    type_CallFrame:str
    type_CallFrameId:str
    type_DebugSymbols:str
    type_Location:str
    type_Scope:str
    type_ScriptLanguage:str
    type_SearchMatch:str
    type_LocationRange:str
    type_ScriptPosition:str
    type_WasmDisassemblyChunk:str

    def __init__(self):
        super().__init__()

    
domain = Debugger()