import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Utility.configManager import *
from pages.home import *
from pages.Iframe import * 
from pages.handle import * 
from Logging.logs import * 
import time 
from selenium.webdriver.common.alert import Alert


class DemoQA(unittest.TestCase):

  logger = LogGen.logged()

  def setUp(self):

    browser = ""
    option = input('Please choose the Browser. \n 1. Chome  \n 2. firefox \n type : ')
    if option == '1':
      browser = "chrome"
    elif option == '2':
      browser = "firefox"
    else:
      print('Invalid input')
        
    mydriver  = SeleniumConfigManager(browser)
    self.driver = mydriver.get_config()

  def test_1(self):

    hmp = HomePage(self.driver)
    hmp.alert_button_locator()
    time.sleep(5)
    hmp.Alert_nav_li()
  
    time.sleep(5)

    alert_click_text = hmp.Alert_click_text("Click Button to see alert ")
    assert alert_click_text.text == "Click Button to see alert", "Unable to find (Click Button to see alert )"
    hmp.Alert_click_button()
    time.sleep(2)

    alert_click_confirm_button = hmp.Alert_click_confirm_text("On button click, confirm box will appear")
    assert alert_click_confirm_button.text == "On button click, confirm box will appear", "Unable to find (On button click, confirm box will appear)"
    hmp.Alert_click_confirm_button()
    time.sleep(2)
    hmp.Alert_box_prompt()
    time.sleep(2)
    hmp.Alert_confirmed_result().text == "You selected Ok" , "unable to see (You selected OK) "
    time.sleep(2)

    alert_click_prompt_text = hmp.Alert_click_prompt_text("On button click, prompt box will appear")
    assert alert_click_prompt_text.text == "On button click, prompt box will appear",  "Unable to find (On button click, prompt box will appear)"
    hmp.Alert_click_prompt_button()
    time.sleep(2)
    data = "hello world"
    hmp.Alert_box_args(data)
    assert hmp.Alert_prompt_result().text == "You entered "+data, "unable to see (Prompt Data) "
    time.sleep(2)
    hmp.save_to_json()

  def test_2(self):
    self.logger.info('------ Starting DDT Test Case---------')
    utl = Utility_QA()

    for i in utl.data_json_load():

      self.logger.info('------ 1) Home Page---------')
    

      hmp = HomePage(self.driver)
      hmp.alert_button_locator()
      self.logger.info('------ 2) Clicking Alert Button ---------')

      time.sleep(1)
      hmp.Alert_nav_li()
      self.logger.info('------ 3) Clicking Alert Navigation Button ---------')

      time.sleep(1)
      alert_click_text = hmp.Alert_click_text(str(i["text1"]+" "))
      self.logger.info('------ 4) Verifying Matching Text On Browser ---------')

      assert alert_click_text.text == i['text1'], "Unable to find (Click Button to see alert )"
      self.logger.info('------ 5) Asserting Text  ---------')

      print(type(i["text1"]))
      hmp.Alert_click_button()
      time.sleep(2)

      alert_click_confirm_button = hmp.Alert_click_confirm_text(i['text2'])
      assert alert_click_confirm_button.text == i['text2'], "Unable to find (On button click, confirm box will appear)"
      hmp.Alert_click_confirm_button()
      time.sleep(2)
      hmp.Alert_box_prompt()
      hmp.Alert_confirmed_result().text == i['text1_result'], "unable to see (You selected OK)"

      alert_click_prompt_text = hmp.Alert_click_prompt_text(i['text3'])
      assert alert_click_prompt_text.text == i['text3'],  "Unable to find (On button click, prompt box will appear)"
      hmp.Alert_click_prompt_button()
      time.sleep(2)
      data = "hello world"
      hmp.Alert_box_args(data)
      assert hmp.Alert_prompt_result().text == "You entered "+data, "unable to see (Prompt Data) "
     

  def test_3(self):

    hmp = Iframe(self.driver)

    hmp.alert_button_locator()
   
    hmp.Alert_nav_li()

    hmp.parent_frame()

    hmp.child_frame()

    parent_text = hmp.parent_content()
    
    print(parent_text)

    child_text = hmp.child_content()

    print(child_text)
 
    hmp.save_to_json()


  def test_4(self):

    self.logger.info('------ Starting DDT Test Case---------')

    utl = Utility_QA()

    for i in utl.data_json_load_iframe():

      self.logger.info('------ 1) Home Page---------')

      hmp = Iframe(self.driver)

      self.logger.info('------ 2) Clicking Alert Button ---------')

      hmp.alert_button_locator()
    
      hmp.Alert_nav_li()

      self.logger.info('------ 3) Parent IFrame ---------')

      hmp.parent_frame()

      self.logger.info('------ 4) Child IFrame ---------')

      hmp.child_frame()

      self.logger.info('------ 5) Asserting parent & child content with json data ---------')

      parent_text = hmp.parent_content()

      if i['parent_text']:
        

        assert parent_text == i['parent_text']

        child_text = hmp.child_content()

        assert child_text == i['child_text']
  
        self.logger.info('------  Ended DDT Test Case---------')


  def test_5(self):

    hmp = Handle(self.driver)

    hmp.alert_button_locator()

    time.sleep(5)

    hmp.Alert_nav_li()

    hmp.Tab_button()

    time.sleep(3) 

    hmp.Elements()

    time.sleep(3) 
    
    hmp.save_to_json()


  def test_6(self):
      
      self.logger.info('------ Starting DDT Test Case---------')

      utl = Utility_QA()

      for i in utl.data_json_load_handle():

        self.logger.info('------ 1) Home Page---------')

        hmp = Handle(self.driver)

        self.logger.info('------ 2) Clicking Alert Button ---------')

        hmp.alert_button_locator()

        hmp.Alert_nav_li()

        self.logger.info('------ 3) Tab Button  ---------')

        page_text = hmp.Tab_button()

        self.logger.info('------ 4) asserting page_text with json data ---------')

        assert i['page_text'] == page_text

        hmp.Elements()

      
  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()
