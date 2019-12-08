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

	@classmethods
	def setUp(self):
		self.driver.get("http://travel.agileway.net")

	@classmethds
	def tearDown(self):
		self.driver.find_element_by_link_text('Sign off').click()

	def test_first_case(self):
		self.assertEqual('Agile Travel', self.driver.title)
		self.driver.find_element_by_name('username').send_keys('agileway')

	def test_second_case(self):
		self.driver.find_element_by_id('register_link').click()
		self.assertIn('register', self.driver.find_element_by_tag_name('body').text)
