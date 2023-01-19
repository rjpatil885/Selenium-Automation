from xml.dom.minidom import Element
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from PageObject.Locators import *
from Utility.utilityDriver import * 
from selenium.webdriver.common.alert import Alert
from Utility.Utility import * 


class Singleton:
    def __init__(self, driver):
        self.driver = driver
    @classmethod
    def get(cls, driver):
        if not hasattr(cls, 'instance'):
            cls.instance = Singleton(driver)
        return cls.instance.driver

class Base_Element(object):
    def __init__(self, driver):
        self.locator = None
        self.util = DriverUtils(self.driver)
    
    
    def click(self, selector):

        clickable_check  = self.util.wait_element_clickable(selector=selector)
        if clickable_check == True:
            element = self.util.wait_element_visible(selector=selector)
        else : 
            element = clickable_check 
        return element

    def send_keys_alert(self, text):
        element = Alert(self.driver)
        element.send_keys(text)
        element.accept()

    def send_keys(self, text):
        element = Alert(self.driver)
        element.send_keys(text)
        element.accept()

    def is_displayed(self, selector):
        element = self.util.wait_element_visible(selector=selector)
        return element

    def is_displayed_text(self,text):
        element = self.util.wait_element_visible_bytext(selector=text)
        return element

    def alert_box(self):
        alert3 = Alert(self.driver)
        alert3.accept()

  
