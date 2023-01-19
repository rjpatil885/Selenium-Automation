
from selenium.webdriver.common.by import By

from Base.BaseElement import *


class Iframe(Base_Element):

    text_alert1 = None 
    alert_button_home =  "//div[@class='card-body']//child::h5[text()='Alerts, Frame & Windows']"
    nav_alert_li_sl = "//*[text()='Nested Frames']"
    
    frame1 = "//iframe[@id='frame1']"
    frame2 = "//iframe[@id='frame2']"
    Frame = "//span[text()='Frames']"

    def __init__(self, driver):

      self.driver = driver
      
      super(Iframe, self).__init__(driver)
    
    def alert_button_locator(self):
     
      val =  self.click(selector=self.alert_button_home)
      
      val.click()

    def Alert_nav_li(self):

      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      nav_ul =  self.click(selector=self.nav_alert_li_sl)

      nav_ul.click()

# ------------------------------ FRAME ------------------------

    def parent_frame(self):

      iframe_text= self.is_displayed(self.frame1)
      self.driver.switch_to.frame(iframe_text)
      parent_text = self.driver.find_element(By.TAG_NAME, 'body').text

      print("------------------",parent_text,"-------------------")

    def child_frame(self):

      iframe_text= self.driver.find_element(By.TAG_NAME, "iframe")
      self.driver.switch_to.frame(iframe_text)
      child_text = self.driver.find_element(By.TAG_NAME, 'body').text
      print("------------------",child_text,"-------------------")
      self.driver.switch_to.default_content()

    def parent_content(self):
      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      frames= self.driver.find_element(By.XPATH, self.Frame)
      frames.click()
      parent_text_frame= self.is_displayed(self.frame1)
      self.driver.switch_to.frame(parent_text_frame)
      self.parent_text_fm = self.driver.find_element(By.TAG_NAME, 'body').text
      print("------------------",self.parent_text_fm,"-------------------")
      self.driver.switch_to.default_content()

      return self.parent_text_fm 

    def child_content(self):
      child_text_frame= self.is_displayed(self.frame2)
      self.driver.switch_to.frame(child_text_frame)
      self.child_text_fm = self.driver.find_element(By.TAG_NAME, 'body').text
      print("------------------",self.child_text_fm,"-------------------")
      self.driver.switch_to.default_content()
      child_text = self.child_text_fm
      return child_text
      

    def save_to_json(self):

      utl_qa = Utility_QA()
      dic_data ={
        'parent_text':self.parent_text_fm,
        'child_text': self.child_text_fm ,
      }

      utl_qa.set_data_iframe (
        dic_data
      )