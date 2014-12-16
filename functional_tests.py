from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She
        # goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box (she
        # likes to tie fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and the list
        # includes her new to-do item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item does not appear in table"
        )

        # A second text-box invites her to add another item to the
        # list, so she enters "use feathers to make a fly"

        self.fail('Finish the tests!')

        # The page updates again, showing both items in the list

        # Edith wonders if the site will remember her list. The site has
        # generated what looks like a unique URL and there is some help
        # text affirming that her list is safe.

        # She visits the unique URL and sees her list

        # Done. Sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
