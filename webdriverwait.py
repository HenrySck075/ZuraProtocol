from datetime import datetime
class TimeoutError(Exception):
    "nya"

class Waiter:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def until(self, condition):
        time = int(datetime.now().timestamp()+self.timeout)
        while datetime.now().timestamp() < time:
            if x:=condition(driver) is not None: return x
        raise TimeoutError(f"waited {self.time} seconds and nothing happened")
