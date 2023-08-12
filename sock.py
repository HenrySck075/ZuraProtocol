
class HatsuneMiku:
    def __init__(self, socket):
        self.__ws = socket

    def execute_command(self, method:str, params:dict={}) -> DevToolsResponse:
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
