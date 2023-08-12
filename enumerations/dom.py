from . import _ok as base

class DOM(base.sendhelp):

    method_DescribeNode:str
    method_Disable:str
    method_Enable:str
    method_Focus:str
    method_GetAttributes:str
    method_GetBoxModel:str
    method_GetDocument:str
    method_GetNodeForLocation:str
    method_GetOuterHTML:str
    method_HideHighlight:str
    method_HighlightNode:str
    method_HighlightRect:str
    method_MoveTo:str
    method_QuerySelector:str
    method_QuerySelectorAll:str
    method_RemoveAttribute:str
    method_RemoveNode:str
    method_RequestChildNodes:str
    method_RequestNode:str
    method_ResolveNode:str
    method_SetAttributesAsText:str
    method_SetAttributeValue:str
    method_SetFileInputFiles:str
    method_SetNodeName:str
    method_SetNodeValue:str
    method_SetOuterHTML:str
    method_GetFlattenedDocument:str
    method_CollectClassNamesFromSubtree:str
    method_CopyTo:str
    method_DiscardSearchResults:str
    method_GetContainerForNode:str
    method_GetContentQuads:str
    method_GetFileInfo:str
    method_GetFrameOwner:str
    method_GetNodesForSubtreeByStyle:str
    method_GetNodeStackTraces:str
    method_GetQueryingDescendantsForContainer:str
    method_GetRelayoutBoundary:str
    method_GetSearchResults:str
    method_GetTopLayerElements:str
    method_MarkUndoableState:str
    method_PerformSearch:str
    method_PushNodeByPathToFrontend:str
    method_PushNodesByBackendIdsToFrontend:str
    method_Redo:str
    method_ScrollIntoViewIfNeeded:str
    method_SetInspectedNode:str
    method_SetNodeStackTracesEnabled:str
    method_Undo:str

    event_AttributeModified:str
    event_AttributeRemoved:str
    event_CharacterDataModified:str
    event_ChildNodeCountUpdated:str
    event_ChildNodeInserted:str
    event_ChildNodeRemoved:str
    event_DocumentUpdated:str
    event_SetChildNodes:str
    event_DistributedNodesUpdated:str
    event_InlineStyleInvalidated:str
    event_PseudoElementAdded:str
    event_PseudoElementRemoved:str
    event_ShadowRootPopped:str
    event_ShadowRootPushed:str
    event_TopLayerElementsUpdated:str

    type_BackendNode:str
    type_BackendNodeId:str
    type_BoxModel:str
    type_CompatibilityMode:str
    type_CSSComputedStyleProperty:str
    type_LogicalAxes:str
    type_Node:str
    type_NodeId:str
    type_PhysicalAxes:str
    type_PseudoType:str
    type_Quad:str
    type_Rect:str
    type_RGBA:str
    type_ShadowRootType:str
    type_ShapeOutsideInfo:str

    def __init__(self):
        super().__init__()

    
domain = DOM()