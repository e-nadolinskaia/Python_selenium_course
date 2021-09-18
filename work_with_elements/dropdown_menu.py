'''
In this task, the program executes the following scenario:

1. Open a page http://suninjuly.github.io/selects1.html
2. Calculate the sum of the given numbers
3. Select a value equal to the calculated amount from the drop-down list
4. Click the"Submit" button.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum(num1,num2):
    return num1+num2

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    num1_text = browser.find_element_by_id('num1')
    num1 = int(num1_text.text)

    num2_text = browser.find_element_by_id('num2')
    num2 = int(num2_text.text)

    sum_of_num = sum(num1,num2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_of_num))
    submit = browser.find_element_by_css_selector('.btn.btn-default')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
    
	

