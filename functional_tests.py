from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User visits an online to-do app
        self.browser.get('http://localhost:8000')

        # User checks that 'To-Do' is in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a to-do item

        # User types "Buy peacock feathers" into a text box

        # When user hits <Enter>, the page updates and lists
        # "1: Buy peacock feathers"

        # The text box still allows the user to enter more items
        # User adds "Use peacock feathers to make a fly"

        # The page updates and lists both items

        # The site has generated a unique URL to access the to-do list

        # User visits that URL and confirms the list

        # User is done with the site

if __name__ == '__main__':
    unittest.main()
