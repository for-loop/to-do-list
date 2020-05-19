from .my_lists_page import MyListsPage
from .list_page import ListPage
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
        list_page = ListPage(self).add_list_item('Get help')

        # User 1 notices a "Share this list" option
        share_box = list_page.get_share_box()
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )

        # User 1 shares the list
        # The page updates to say that it's shared with User 2
        list_page.share_list_with('another.one@example.com')

        # User 2 now goes to the lists page
        self.browser = user2_browser
        MyListsPage(self).go_to_my_lists_page()

        # User 2 sees User 1's list!
        self.browser.find_element_by_link_text('Get help').click()

        # On the list page, User 2 verifies that it's User 1's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'some.one@example.com'
        ))

        # User 2 adds an item to the list
        list_page.add_list_item('Hi Some One!')

        # When User 1 refreshes the page, User 2's new item can be seen
        self.browser = user1_browser
        self.browser.refresh()
        list_page.wait_for_row_in_list_table('Hi Some One!', 2)
