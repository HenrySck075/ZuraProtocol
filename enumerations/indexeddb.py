from . import _ok as base

class IndexedDB(base.sendhelp):

    method_ClearObjectStore:str
    method_DeleteDatabase:str
    method_DeleteObjectStoreEntries:str
    method_Disable:str
    method_Enable:str
    method_GetMetadata:str
    method_RequestData:str
    method_RequestDatabase:str
    method_RequestDatabaseNames:str

    type_DatabaseWithObjectStores:str
    type_DataEntry:str
    type_Key:str
    type_KeyPath:str
    type_KeyRange:str
    type_ObjectStore:str
    type_ObjectStoreIndex:str

    def __init__(self):
        super().__init__()

    
domain = IndexedDB()