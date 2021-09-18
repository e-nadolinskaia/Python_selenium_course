'''
Task:
1. Open a page http://suninjuly.github.io/file_input.html
2. Fill in the text fields: first name, last name, email
3. Upload the file. The file must have an extension .txt and can be empty
4. Click the"Submit" button.
'''

from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    
    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys('Kate')

    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Korvusova')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'file.txt') 

    load_button = browser.find_element_by_css_selector("[type ='file']")       
    load_button.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector('.btn')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
