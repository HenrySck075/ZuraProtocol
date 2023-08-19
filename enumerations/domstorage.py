
from . import _ok as base

class DOMStorage(base.sendhelp):

    method_Clear:str
    method_Disable:str
    method_Enable:str
    method_GetDOMStorageItems:str
    method_RemoveDOMStorageItem:str
    method_SetDOMStorageItem:str

    event_DomStorageItemAdded:str
    event_DomStorageItemRemoved:str
    event_DomStorageItemsCleared:str
    event_DomStorageItemUpdated:str

    type_Item:str
    type_SerializedStorageKey:str
    type_StorageId:str

    def __init__(self):
        super().__init__()

    
