from typing import Callable, Any, Tuple
from .webdriver import KiraProtocol
from .webelement import KiraElement
import re
__all__ = ("title_is","presence_of_element_located")
# todo: ok
condition = Callable[[KiraProtocol],KiraElement]
boolean = Callable[[KiraProtocol],bool]

def title_is(title:str) -> boolean:
    def pred(driver):
        return driver.title == title
    return pred

def title_contains(title:str) -> boolean:
    def pred(driver):
        return title in driver.title
    return pred

def presence_of_element_located(locator: Tuple[str, str]) -> condition:
    def pred(driver):
        return driver.find_element(*locator)
    return pred

def url_contains(url:str) -> boolean:
    def pred(driver):
        return url in driver.current_url
    return pred

def url_matches(pattern:str) -> boolean:
    def pred(driver):
        return re.search(pattern, driver.current_url) is not None
    return pred

def url_to_be(url:str) -> boolean:
    def pred(driver):
        return url == driver.current_url
    return pred

def url_changes(url:str) -> boolean:
    def pred(driver):
        return url == driver.current_url
    return pred

def visibility_of_element_located(locator: Tuple[str, str]) -> condition:
    def pred(driver):
        a = driver.find_element(*locator)
        return a
    return pred
