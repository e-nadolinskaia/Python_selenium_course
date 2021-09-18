'''To run the test with the desired label, you need to pass the -m parameter and the desired label on the command line:
pytest -s -v -m smoke fixtures_with_marks.py'''


import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
@pytest.fixture(scope='function')
def browser():
	print('\nstart browser for test..')
	browser = webdriver.Chrome()
	yield browser
	print('\nquit browser..')
	browser.quit()

class TestMainPage():

	@pytest.mark.smoke
	def test_guest_should_see_login_link(self,browser):
		browser.get(link)
		browser.find_element_by_css_selector("#login_link")

	@pytest.mark.regression
	def test_guest_should_see_basket_link_on_the_main_page(self,browser):
		browser.get(link)
		browser.find_element_by_css_selector(".basket-mini .btn-group > a")
