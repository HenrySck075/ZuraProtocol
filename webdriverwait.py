from datetime import datetime
class TimeoutException(Exception):
    "nya"

class Waiter:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def until(self, condition):
        time = int(datetime.now().timestamp()+self.timeout)
        while datetime.now().timestamp() < time:
            x = condition(self.driver)
            if x is not None: 
                if x != False:
                    return x
        raise TimeoutException(f"waited {self.timeout} seconds and nothing happened")
