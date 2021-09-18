'''The script uses unique selectors to find, fill in the form fields, and send data.
1. The test passes on the page http://suninjuly.github.io/registration1.html.
2. The test fails with a NoSuchElementException error on the page 
http://suninjuly.github.io/registration2.html.
'''

import unittest
from selenium import webdriver

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_name = browser.find_element_by_css_selector("input.first[required]")
        input_name.send_keys('Kate')

        input_lastname = browser.find_element_by_css_selector('input.second[required]')
        input_lastname.send_keys('Korvusova')

        input_email = browser.find_element_by_css_selector('input.third[required]')
        input_email.send_keys('@gmail.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
  
        welcome_text_row = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_row.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration is failed')
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_name = browser.find_element_by_css_selector("input.first[required]")
        input_name.send_keys('Kate')

        input_lastname = browser.find_element_by_css_selector('input.second[required]')
        input_lastname.send_keys('Korvusova')

        input_email = browser.find_element_by_css_selector('input.third[required]')
        input_email.send_keys('@gmail.com')
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration is failed')
        browser.quit()



if __name__ == '__main__':
    unittest.main()


