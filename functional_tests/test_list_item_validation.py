from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to the home page and accidentally submits
        # an empty list item. User hists Enter key

        # The home page refreshes with an error message

        # User enters some text and tries again. Now it works

        # User submits another empty list item.

        # An error message is shown again.

        # User enters some text and now it works.
        self.fail('Complete the test!')
