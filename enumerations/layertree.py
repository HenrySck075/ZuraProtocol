
from . import _ok as base

class LayerTree(base.sendhelp):

    method_CompositingReasons:str
    method_Disable:str
    method_Enable:str
    method_LoadSnapshot:str
    method_MakeSnapshot:str
    method_ProfileSnapshot:str
    method_ReleaseSnapshot:str
    method_ReplaySnapshot:str
    method_SnapshotCommandLog:str

    event_LayerPainted:str
    event_LayerTreeDidChange:str

    type_Layer:str
    type_LayerId:str
    type_PaintProfile:str
    type_PictureTile:str
    type_ScrollRect:str
    type_SnapshotId:str
    type_StickyPositionConstraint:str

    def __init__(self):
        super().__init__()

    
domain = LayerTree()