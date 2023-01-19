import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DriverUtils:

	def __init__(self, driver):
		self.driver = driver
			

	def wait_element_clickable(self, selector, time = 5):
		try:
			return  WebDriverWait(self.driver, time).until(
				EC.element_to_be_clickable((By.XPATH, selector))
			)
		
		except TimeoutException:
	
			return "Waiting for element to be clickable timeout"

	# wait for an element to be visible
	def wait_element_visible(self, selector, time = 10):
		try:
			return WebDriverWait(self.driver, time).until(
				EC.visibility_of_element_located((By.XPATH, selector))
			)
		except TimeoutException:

			return "Waiting for element to be visible timeout"

	def wait_element_visible_bytext(self, selector, time = 10):
		
		try:
			return WebDriverWait(self.driver, time).until(
				EC.visibility_of_element_located((By.XPATH, f"//*[text()='{selector}']"))
			)

		except TimeoutException:

			return "Waiting for element to be visible timeout"









































