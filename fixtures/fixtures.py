'''The script demonstrates the differences between the work of the fixtures for the class
 and methods setup and teardown.'''

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n Decorator start browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("Decorator quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('def1 in Class1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('def2 in Class1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('def1 in Class2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('def2 in Class2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


