'''
Task:
1. Open a page http://SunInJuly.github.io/execute_script.html.
2. Read the value for the variable x.
3. Calculate the mathematical function of x.
4. Scroll down the page.
5. Enter the answer in the text field.
6. Select the checkbox "I'm the robot".
7. Switch the radiobutton "Robots rule!".
8. Click on the "Submit" button.
'''

from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    x_text = browser.find_element_by_id('input_value')
    x = int(x_text.text)
    result = math.log((abs(12*math.sin(x))))

    input = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(str(result))
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
   time.sleep(30)
   browser.quit()
   
    
