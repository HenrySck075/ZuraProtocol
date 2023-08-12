import json, os, requests, websocket
import time
from subprocess import PIPE, Popen
from . import enumerations as enum
import socket
from typing import TypedDict, Callable
import logging, threading
sock = socket.socket()

log = logging.getLogger("KiraProtocol")
logging.basicConfig(format='%(asctime)s - %(message)s %(levelname)s', level=logging.DEBUG)

class DevToolsResponse(TypedDict, total=False):
    sessionId: str # this and
    method: str
    id: int # this might not appear in response, especially events
    params: dict
    result: dict # and also this

class KiraOptions:
    _arguments = []
    page_load_strategy = 'eager'
    def add_argument(self, arg): self._arguments.append(arg)


class KiraProtocol:
    """Use DevTools WebSocket dammit!

    (ChefRush ref)"""

    current_window_handle = ""
    
    def __init__(
        self,
        browserPath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        port = 0,
        option: KiraOptions = None
    ):
        """Use DevTools WebSocket dammit!

        (ChefRush ref)"""
        self.id = 1 # increase every execute_command call
        
        self.option = option if isinstance(option,KiraOptions) else KiraProtocol()

        if port == 0:
            sock.bind(('', port))
            port = sock.getsockname()[1]

        print(f"current port is {port}")
        logi = open(os.devnull, "wb")
        def writePrint(buf):
            print(buf)
            logi.write(buf)

        logi.write = writePrint
        # start the browser
        print("Opening browser...")
        a = [browserPath,f"--remote-debugging-port={port}",f"--remote-allow-origins=http://localhost:{port}"]
        a.extend(self.option._arguments)
        Popen(a, stderr=logi, stdout=logi, bufsize=1) #idc
        time.sleep(2)
        # get the
        print("Connecting to DevTools...")
        from requests.adapters import HTTPAdapter, Retry

        s = requests.Session()

        retries = Retry(total=20, # i love you
                        backoff_factor=0.1,
                        status_forcelist=[ 500, 502, 503, 504 ])

        s.mount('http://', HTTPAdapter(max_retries=retries))

        wsUrl = s.get(f"http://localhost:{port}/json/version").json()["webSocketDebuggerUrl"]
        socket = websocket.WebSocket()
        socket.connect(wsUrl)
        self.__socket = DevTools(socket)
        
        a = self.__socket.execute("Target.getTargets")["result"]["targetInfos"][0]
        self.current_window_handle = self.__socket.execute("Target.attachToTarget",{"targetId":a["targetId"],"flatten":True})["params"]["sessionId"]
        self.current_url = a["url"]
        self.title = a["title"]
    
    def __dude_being_fr__(self):
        """Enable every single domains known to man

        ```
        
        hello guys, henry 30 minutes later here.
        
        im so fucking dumb bruh why did this exist"""
        for i in ["Accessibility", "Animation", "Audits", "Autofill", "BackgroundService", "Browser", "CacheStorage", "Cast", "Console", "CSS", "Database", "Debugger", "DeviceAccess", "DeviceOrientation", "DOM", "DOMDebugger", "DOMSnapshot", "DOMStorage", "Emulation", "EventBreakpoints", "FedCm", "Fetch", "HeadlessExperimental", "HeapProfiler", "IndexedDB", "Input", "Inspector", "IO", "LayerTree", "Log", "Media", "Memory", "Network", "Overlay", "Page", "Performance", "PerformanceTimeline", "Preload", "Profiler", "Runtime", "Schema", "Security", "ServiceWorker", "Storage", "SystemInfo", "Target", "Tethering", "Tracing", "WebAudio", "WebAuthn"]:
            self.__socket.execute(i+".enable")

    # Properties, maybe
    @property
    def window_handles(self):
        return self.__socket.execute(enum.Page.method_GetFrameTree)
    
    @property
    def socket(self): return self.__socket

    # funny

    def get(self, url):
        self.__socket.execute(enum.Page.method_Navigate, {"url": url})
        
        if self.option.page_load_strategy == "eager": 
            self.__socket.execute(enum.Page.method_Enable)
            self.__socket.wait_for_event(enum.Page.event_DomContentEventFired)
            self.__socket.execute(enum.Page.method_Disable)
