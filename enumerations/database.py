from . import _ok as base

class Database(base.sendhelp):

    method_Disable:str
    method_Enable:str
    method_ExecuteSQL:str
    method_GetDatabaseTableNames:str

    event_AddDatabase:str

    type_Database:str
    type_DatabaseId:str
    type_Error:str

    def __init__(self):
        super().__init__()

    
domain = Database()