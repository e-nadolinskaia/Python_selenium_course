'''
Task:
1. Open the page
2. Enter the correct answer
3. Click the "Send"
4. Button wait for the feedback that the answer is correct
5. Check that the text in the optional feedback completely matches "Correct!"
The dropped tests contain pieces of the message. The test should fail if the text in the optional feedback does not match the line " Correct!"'''

import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture(scope ='function')
def browser():
	print('\nStart browser')
	browser = webdriver.Chrome()
	yield browser
	print('\nQuit browser')
	browser.quit()


@pytest.mark.parametrize('links', ['236895','236896','236897','236898','236899','236903','236904','236905'])
def test_search(browser,links):
	browser.implicitly_wait(5)
	link = f'https://stepik.org/lesson/{links}/step/1'
	browser.get(link)

	answer = browser.find_element_by_tag_name('textarea')
	answer.send_keys(str(math.log(int(time.time()))))

	submit_button = browser.find_element_by_css_selector('.submit-submission')
	submit_button.click()

	message_row = browser.find_element_by_css_selector('.smart-hints__hint')
	message = message_row.text
	print(message)

	assert message == "Correct!", "The answer is wrong"
