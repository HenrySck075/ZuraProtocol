from typing import TypedDict
import json, logging
from . import enumerations as enum

log = logging.getLogger("KiraProtocol")

class DevToolsResponse(TypedDict, total=False):
    sessionId: str # this and
    method: str
    id: int # this might not appear in response, especially events
    params: dict
    result: dict # and also this

class HatsuneMiku:
    def __init__(self, socket):
        self.__ws = socket
        self.id = 1
        self.current_window_handle = ""
    
    def set_handle(self, h):
        self.current_window_handle = h

    def execute(self, method:str, **params) -> DevToolsResponse:
        "WebSocket"
        a = {
            "sessionId": self.current_window_handle,
            "id": self.id,
            "method": method,
            "params": params
        }
        # if params == {}: del a["params"]
        self.__ws.send(json.dumps(a))
        self.id+=1
        # todo: errors raising because im funny
        return json.loads(self.__ws.recv())

    def wait_for_event(self, event:str) -> None:
        while True:
            rec=json.loads(self.__ws.recv())
            log.debug(rec)
            if "method" not in rec: continue
            if rec["method"] == event: break
            if rec["method"] == enum.Fetch.event_RequestPaused:
                self.__ws.execute(enum.Fetch.method_FulfillRequest,{"requestId":rec["params"]["requestId"],"responseCode":200})
    
    def receive(self):
        return json.loads(self.__ws.recv())
