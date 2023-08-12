from . import _ok as base

class Input(base.sendhelp):

    method_CancelDragging:str
    method_DispatchKeyEvent:str
    method_DispatchMouseEvent:str
    method_DispatchTouchEvent:str
    method_SetIgnoreInputEvents:str
    method_DispatchDragEvent:str
    method_EmulateTouchFromMouseEvent:str
    method_ImeSetComposition:str
    method_InsertText:str
    method_SetInterceptDrags:str
    method_SynthesizePinchGesture:str
    method_SynthesizeScrollGesture:str
    method_SynthesizeTapGesture:str

    event_DragIntercepted:str

    type_MouseButton:str
    type_TimeSinceEpoch:str
    type_TouchPoint:str
    type_DragData:str
    type_DragDataItem:str
    type_GestureSourceType:str

    def __init__(self):
        super().__init__()

    
domain = Input()