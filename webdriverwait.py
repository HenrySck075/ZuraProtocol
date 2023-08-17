from datetime import datetime
from typing import Callable
from .webdriver import Protocol
from .webelement import Element
class TimeoutException(Exception):
    "nya"
condition = Callable[[Protocol],Element]
boolean = Callable[[Protocol],bool]
class Waiter:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def until(self, condi:condition|boolean):
        time = int(datetime.now().timestamp()+self.timeout)
        while datetime.now().timestamp() < time:
            x = condi(self.driver)
            if x is not None: 
                if x != False:
                    return x
        raise TimeoutException(f"waited {self.timeout} seconds and nothing happened")
