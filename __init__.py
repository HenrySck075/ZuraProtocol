<<<<<<< HEAD
'Kira Kiraa Kosekiiiii'
__import__("os").environ["PYTHONDONTWRITEBYTECODE"] = "1"
__import__("logging").getLogger("KiraProtocol")
from .webdriver import Protocol, KiraOptions, Element
from .webdriverwait import Waiter, TimeoutException
from . import expected_cond as ec, exceptions
=======
__import__("os").environ["PYTHONDONTWRITEBYTECODE"] = "1"
__import__("logging").getLogger("KiraProtocol")
from .webdriver import KiraProtocol, KiraOptions, KiraElement
from .webdriverwait import Waiter, TimeoutException
from . import expected_cond as ec
>>>>>>> 32addd10427ef121cbc31aa0c729a1c92ce3fe78
