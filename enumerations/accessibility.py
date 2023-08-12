from . import _ok as base

class Accessibility(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetAXNodeAndAncestors:str
    method_GetChildAXNodes:str
    method_GetFullAXTree:str
    method_GetPartialAXTree:str
    method_GetRootAXNode:str
    method_QueryAXTree:str

    event_LoadComplete:str
    event_NodesUpdated:str

    type_AXNode:str
    type_AXNodeId:str
    type_AXProperty:str
    type_AXPropertyName:str
    type_AXRelatedNode:str
    type_AXValue:str
    type_AXValueNativeSourceType:str
    type_AXValueSource:str
    type_AXValueSourceType:str
    type_AXValueType:str

    def __init__(self):
        super().__init__()

    
domain = Accessibility()