from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	@classmethods
	def teardownClass(cls):
		cls.driver.quit()
