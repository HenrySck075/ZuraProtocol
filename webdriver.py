from __future__ import annotations

import os, requests, websocket
import time
from subprocess import Popen
from . import enumerations as enum
import logging, threading, sys
from .sock import HatsuneMiku as DevTools

os.environ["PYTHONDONTWRITEBYTECODE"] = 1

log = logging.getLogger("KiraProtocol")
logging.basicConfig(format='%(asctime)s - %(message)s %(levelname)s', level=logging.DEBUG)

domains = ["Accessibility", "Animation", "Audits", "Autofill", "BackgroundService", "Browser", "CacheStorage", "Cast", "Console", "CSS", "Database", "Debugger", "DeviceAccess", "DeviceOrientation", "DOM", "DOMDebugger", "DOMSnapshot", "DOMStorage", "Emulation", "EventBreakpoints", "FedCm", "Fetch", "HeadlessExperimental", "HeapProfiler", "IndexedDB", "Input", "Inspector", "IO", "LayerTree", "Log", "Media", "Memory", "Network", "Overlay", "Page", "Performance", "PerformanceTimeline", "Preload", "Profiler", "Runtime", "Schema", "Security", "ServiceWorker", "Storage", "SystemInfo", "Target", "Tethering", "Tracing", "WebAudio", "WebAuthn"]

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
        
        self.option = option if isinstance(option,KiraOptions) else KiraProtocol()
        
        import socket
        sock = socket.socket()
        if port == 0:
            sock.bind(('', port))
            port = sock.getsockname()[1]

        del socket

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
        
        a = self.__socket.execute(enum.Target.method_GetTargets)["result"]["targetInfos"][0]
        self.__socket.set_handle(self.__socket.execute(enum.Target.method_AttachToTarget,{"targetId":a["targetId"],"flatten":True})["params"]["sessionId"])
        self.__socket.execute(enum.Runtime.method_Evaluate, expression="let __arguments__")
        self.current_url = a["url"]
        self.title = a["title"]
    
    def __enable__(self):
        """Enable every single domains known to man"""
        for i in domains:
            self.__socket.execute(i+".enable")
    
    def __disable__(self):
        """Disable every single domains known to mant"""
        for i in domains:
            self.__socket.execute(i+".disable")

    # Properties, maybe
    @property
    def window_handles(self):
        return self.__socket.execute(enum.Page.method_GetFrameTree)
    
    @property
    def socket(self):
        "For debugging if something goes wrong with the functions"
        return self.__socket

    @property
    def current_window_handle(self): return self.__socket.current_window_handle

    # funny

    def get(self, url):
        self.__socket.execute(enum.Page.method_Navigate, {"url": url})
        
        if self.option.page_load_strategy == "eager": 
            self.__socket.execute(enum.Page.method_Enable)
            self.__socket.wait_for_event(enum.Page.event_DomContentEventFired)
            self.__socket.execute(enum.Page.method_Disable)

    def quit(self):
        self.__socket.execute(enum.Browser.method_Close)

    # Find Elements

    def find_element(self, by, input):
        return getattr(self, "find_element_by_"+by.replace(" ","_"))(input)
    
    def find_element_by_css_selector(self, selector):
        self.__socket.execute(enum.Runtime.method_Evaluate,{"expression":""})