import mimetypes
import os, requests, websocket
import time
from subprocess import Popen
from . import enumerations as enum
import logging, json
from .sock import HatsuneMiku as DevTools
from .webelement import Element

log = logging.getLogger("KiraProtocol")
#logging.basicConfig(format='%(asctime)s - %(message)s %(levelname)s', level=logging.DEBUG)

domains = ["Accessibility", "Animation", "Audits", "Autofill", "BackgroundService", "Browser", "CacheStorage", "Cast", "Console", "CSS", "Database", "Debugger", "DeviceAccess", "DeviceOrientation", "DOM", "DOMDebugger", "DOMSnapshot", "DOMStorage", "Emulation", "EventBreakpoints", "FedCm", "Fetch", "HeadlessExperimental", "HeapProfiler", "IndexedDB", "Input", "Inspector", "IO", "LayerTree", "Log", "Media", "Memory", "Network", "Overlay", "Page", "Performance", "PerformanceTimeline", "Preload", "Profiler", "Runtime", "Schema", "Security", "ServiceWorker", "Storage", "SystemInfo", "Target", "Tethering", "Tracing", "WebAudio", "WebAuthn"]

class KiraOptions:
    def __init__(self):
        self._arguments = []
        self.page_load_strategy = 'eager'
        self.binary_location = ""
        """The binary location
        
        If left empty then I'll try to connect to existing protocol instead"""
    def add_argument(self, arg): self._arguments.append(arg)

class Protocol:
    """Use DevTools WebSocket dammit!

    (ChefRush ref)"""

    current_window_frame = ""
    
    def __init__(
        self,
        port = 0,
        option: KiraOptions = None,
        page = None
    ):
        """Use DevTools WebSocket dammit!

        (ChefRush ref)
        
        :param port: The port
        :param option: Browser startup option
        :param page: Page info from `/json`. If specified, 2 params above will be ignored"""
        
        self.option = option if isinstance(option,KiraOptions) else KiraOptions()
        browserPath = self.option.binary_location
        
        import socket
        sock = socket.socket()
        if port == 0:
            sock.bind(('', port))
            port = sock.getsockname()[1]

        del socket

        self.connected_to_page = (page != None)
        if page == None:
            a = [browserPath,f"--remote-debugging-port={port}",f"--remote-allow-origins=http://localhost:{port}"]
            a.extend(self.option._arguments)
            if self.option.binary_location != "":
                Popen(a, bufsize=1) #idc
                time.sleep(2)
            # get the
            from requests.adapters import HTTPAdapter, Retry

            s = requests.Session()

            retries = Retry(total=20, # i love you
                            backoff_factor=0.1,
                            status_forcelist=[ 500, 502, 503, 504 ])

            s.mount('http://', HTTPAdapter(max_retries=retries))

            wsUrl = s.get(f"http://localhost:{port}/json/version").json()["webSocketDebuggerUrl"]
        else: wsUrl = page["webSocketDebuggerUrl"]
        socket = websocket.WebSocket()
        socket.connect(wsUrl,timeout=20)
        self.__socket = DevTools(socket)
        
        if page == None:
            a = self.__socket.execute(enum.Target.method_GetTargets)["result"]["targetInfos"][0]
            self.__socket.set_frame(self.__socket.execute(enum.Target.method_AttachToTarget,targetId=a["targetId"],flatten=True)["result"]["sessionId"])
            self.__socket.execute(enum.Runtime.method_Evaluate, expression="let __arguments__ = {}")
            self.current_url = a["url"]
            self.title = a["title"]
        else: 
            self.current_url = page["url"]
            self.title = page["title"]
        log.info("Init finished, if the code's halting the fix it yourself")
    
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
    def window_frames(self):
        return self.__socket.execute(enum.Page.method_GetFrameTree) if not self.connected_to_page else None
    
    @property
    def socket(self):
        "For debugging if something goes wrong with the functions"
        return self.__socket

    @property
    def current_window_frame(self): return self.__socket.current_window_frame

    # funny

    def get(self, url):
        "Open URL"
        self.__socket.execute(enum.Page.method_Navigate, url = url)
        
        if self.option.page_load_strategy == "eager": 
            self.__socket.execute(enum.Page.method_Enable)
            self.__socket.wait_for_event(enum.Page.event_DomContentEventFired)
            self.__socket.execute(enum.Page.method_Disable)
        a = self.__socket.execute(enum.Target.method_GetTargets)["result"]["targetInfos"][0]
        self.current_url = a["url"]
        self.title = a["title"]
        self.__socket.execute(enum.Runtime.method_Evaluate, expression="let __arguments__ = {}")

    def fetch(self, url, method="GET", header=None, body=None, files = {}) -> dict:
        """Fetch data from URL in current session
        
        NOTE: the body and response are currently expected to be a JSON object

        :param files: Structure: \
        ``` \
        {filetype (e.g. image, avatar, ...): file content in bytes \
        ```
        """
        expr = ""
        if files != {}:
            expr += "__arguments__['formdata'] = new FormData()\n"
            expr += f"__arguments__['formdata'].append('str', {json.dumps(body)})"+"\n"
            body = None
            for i in files.keys():
                self.__socket.execute(enum.Runtime.method_Evaluate, expression = f"__arguments__['fd_{i}'] = new Blob(['{files[i]}'])")
                expr += f"__arguments__['formdata'].append('{i}', __arguments__['fd_{i}'])"+"\n"

        expr += f'await (await fetch("{url}", \u007bmode: "same-origin", method: "{method}"'
        if body!=None and method not in ["POST", "PUT"]: body = None
        if type(header)==dict: expr+=", headers: " + json.dumps(header)
        if type(body  )==dict: expr+=", body: JSON.stringify(" + json.dumps(body) + ")"
        if files != {}       : expr+=", body: __arguments__['formdata']"
        expr+="})).json()"
        a=self.__socket.execute(enum.Runtime.method_Evaluate, replMode=True, returnByValue=True, expression=expr)
        print(a)
        return a["result"]["result"]["value"]
        
    
    def quit(self):
        if self.connected_to_page: self.__socket.execute(enum.Page.method_Close)
        else: self.__socket.execute(enum.Browser.method_Close)
        self.__socket.close()

    # Find Elements
    def _add_to_args(self, func):
        location = self.__socket.execute(enum.Runtime.method_Evaluate, expression = "Object.keys(__arguments__).length")["result"]["result"]["value"]
        a = self.__socket.execute(enum.Runtime.method_Evaluate, expression = f"__arguments__[{location}] = {func}")
        if a["result"]["result"]["subtype"] == 'null': location = None
        return location
    
    def __get_element_by_args_location(self,location):
        if location is not None:
            node = self.__socket.execute(enum.DOM.method_DescribeNode,objectId = self.__socket.execute(enum.Runtime.method_Evaluate, expression=f"__arguments__[{location}]")["result"]["result"]["objectId"])["result"]["node"]
            return Element(nodeId = node["nodeId"], socket = self.__socket, location = location, handle=self.current_window_handle)
        else: return None

    def find_element(self, by, input):
        return getattr(self, "find_element_by_"+by.replace(" ","_"))(input)
    
    def find_element_by_css_selector(self, selector):
        return self.__get_element_by_args_location(self._add_to_args(f"document.querySelector('{selector}')"))

    def find_element_by_xpath(self, path):
        return self.__get_element_by_args_location(self._add_to_args(f"document.evaluate('{path}', document, null, 9, null).singleNodeValue"))
