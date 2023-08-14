from .sock import HatsuneMiku as DevTools
from . import enumerations as enum

class KiraElement:
    def __init__(self, **kwargs):
        """
        Args:
        :param kwargs: Maybe you shouldn't know much about how open my parameters are
        """
        self.window_handle = kwargs["handle"]
        "The window handle this element belong to"

        self.arg_location = kwargs["location"]
        "Key name of the object in __arguments__ (for interactive actions like clicking)"

        self.nodeId = kwargs["nodeId"]

        self.__socket = kwargs["socket"]

    def click(self):
        self.__socket.execute(enum.Runtime.method_Evaluate, expression = f"__arguments__[{self.arg_location}].click()")
    
    @property
    def text(self) -> str:
        return self.__socket.execute(enum.Runtime.method_Evaluate, expression = f"__arguments__[{self.arg_location}].innerText")["result"]["result"]["value"]
