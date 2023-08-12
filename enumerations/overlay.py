from . import _ok as base

class Overlay(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_GetGridHighlightObjectsForTest:str
    method_GetHighlightObjectForTest:str
    method_GetSourceOrderHighlightObjectForTest:str
    method_HideHighlight:str
    method_HighlightNode:str
    method_HighlightQuad:str
    method_HighlightRect:str
    method_HighlightSourceOrder:str
    method_SetInspectMode:str
    method_SetPausedInDebuggerMessage:str
    method_SetShowAdHighlights:str
    method_SetShowContainerQueryOverlays:str
    method_SetShowDebugBorders:str
    method_SetShowFlexOverlays:str
    method_SetShowFPSCounter:str
    method_SetShowGridOverlays:str
    method_SetShowHinge:str
    method_SetShowIsolatedElements:str
    method_SetShowLayoutShiftRegions:str
    method_SetShowPaintRects:str
    method_SetShowScrollBottleneckRects:str
    method_SetShowScrollSnapOverlays:str
    method_SetShowViewportSizeOnResize:str
    method_SetShowWebVitals:str
    method_HighlightFrame:str
    method_SetShowHitTestBorders:str

    event_InspectModeCanceled:str
    event_InspectNodeRequested:str
    event_NodeHighlightRequested:str
    event_ScreenshotRequested:str

    type_BoxStyle:str
    type_ColorFormat:str
    type_ContainerQueryContainerHighlightConfig:str
    type_ContainerQueryHighlightConfig:str
    type_ContrastAlgorithm:str
    type_FlexContainerHighlightConfig:str
    type_FlexItemHighlightConfig:str
    type_FlexNodeHighlightConfig:str
    type_GridHighlightConfig:str
    type_GridNodeHighlightConfig:str
    type_HighlightConfig:str
    type_HingeConfig:str
    type_InspectMode:str
    type_IsolatedElementHighlightConfig:str
    type_IsolationModeHighlightConfig:str
    type_LineStyle:str
    type_ScrollSnapContainerHighlightConfig:str
    type_ScrollSnapHighlightConfig:str
    type_SourceOrderConfig:str

    def __init__(self):
        super().__init__()

    
domain = Overlay()