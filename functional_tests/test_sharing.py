from selenium import webdriver
from .base import FunctionalTest

def quit_if_possible(browser):
    try: browser.quit()
    except: pass

class SharingTest(FunctionalTest):

    def test_can_share_a_list_with_another_user(self):
        # User 1 is a logged-in user
        self.create_pre_authenticated_session('some.one@example.com')
        user1_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(user1_browser))

        # User 2 is also hanging out on the site
        user2_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(user2_browser))
        self.browser = user2_browser
        self.create_pre_authenticated_session('another.one@example.com')

        # User 1 goes to the page and starts a list
        self.browser = user1_browser
        self.browser.get(self.live_server_url)
        self.add_list_item('Get help')

        # User 1 notices a "Share this list" option
        share_box = self.browser.find_element_by_css_selector(
            'input[name="sharee"]'
        )
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
