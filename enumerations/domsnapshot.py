from . import _ok as base

class DOMSnapshot(base.sendhelp):

    method_CaptureSnapshot:str
    method_Disable:str
    method_Enable:str
    method_GetSnapshot:str

    type_ArrayOfStrings:str
    type_ComputedStyle:str
    type_DocumentSnapshot:str
    type_DOMNode:str
    type_InlineTextBox:str
    type_LayoutTreeNode:str
    type_LayoutTreeSnapshot:str
    type_NameValue:str
    type_NodeTreeSnapshot:str
    type_RareBooleanData:str
    type_RareIntegerData:str
    type_RareStringData:str
    type_Rectangle:str
    type_StringIndex:str
    type_TextBoxSnapshot:str

    def __init__(self):
        super().__init__()

    
domain = DOMSnapshot()