
from . import _ok as base

class PerformanceTimeline(base.sendhelp):

    method_Enable:str

    event_TimelineEventAdded:str

    type_LargestContentfulPaint:str
    type_LayoutShift:str
    type_LayoutShiftAttribution:str
    type_TimelineEvent:str

    def __init__(self):
        super().__init__()

    
