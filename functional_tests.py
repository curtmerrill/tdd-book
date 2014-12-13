from selenium import webdriver
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
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "buy peacock feathers" into a text box (she
        # likes to tie fly-fishing lures)

        # When she hits enter, the page updates and the list
        # includes her new to-do item

        # A second text-box invites her to add another item to the
        # list, so she enters "use feathers to make a fly"

        # The page updates again, showing both items in the list

        # Edith wonders if the site will remember her list. The site has
        # generated what looks like a unique URL and there is some help
        # text affirming that her list is safe.

        # She visits the unique URL and sees her list

        # Done. Sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
