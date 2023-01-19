# import json 

# class configManager(object):
#     def __init__(self, config_file='config.json'):
#         self.config_file = config_file
        
#         self.data = {}
#         self.load()
        
#     def get(self, key):
#         return self.data.get(key)
    
#     def set(self, key, value):
#         self.data[key] = value
        
#     def load(self):
#         with open(self.config_file) as f:
#             self.data = json.load(f)
            
#     def save(self):
#         with open(self.config_file, 'w') as f:
#           json.dump(self.data, f)

# #save and load data
# config = configManager()

# config.set('some_key', 'some_value')
# print(config.get('some_key'))

# config.save()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from Base.BaseElement import Singleton


class SeleniumConfigManager(object):

    def __init__(self, driver_name):

        self.driver_name  = driver_name
        self.url = 'https://demoqa.com/'
        

    def get_config(self):
       
        if self.driver_name == 'chrome':

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=chrome_options)
          
            driver.get(self.url)
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            return driver

