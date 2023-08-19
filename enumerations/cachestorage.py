
from . import _ok as base

class CacheStorage(base.sendhelp):

    method_DeleteCache:str
    method_DeleteEntry:str
    method_RequestCachedResponse:str
    method_RequestCacheNames:str
    method_RequestEntries:str

    type_Cache:str
    type_CachedResponse:str
    type_CachedResponseType:str
    type_CacheId:str
    type_DataEntry:str
    type_Header:str

    def __init__(self):
        super().__init__()

    
