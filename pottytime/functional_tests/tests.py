from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_sticker_chart(self, row_text):
        """Helper function to find a given sticker within the chart"""
        table = self.browser.find_element_by_id('id_sticker_chart')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_log_a_potty_training_cycle(self):
        # Joan has heard about a cool new potty-training app to use with her toddler.
        # She visits the site with her potty-training son, Harold
        self.browser.get(self.live_server_url)

        # She notices the page title and header are potty-centric
        self.assertIn('Potty', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Potty', header_text)

        # She is presented with an item to discuss during PottyTime,
        factoid_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Factoid:', factoid_text)

        # along with a running timer of the current potty session
        timer_text = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(timer_text,r'\d\d:\d\d:\d\d')

        # and an option to select 0 (try), 1 (pee), or 2 (poo).
        inputbox = self.browser.find_element_by_id('id_new_sticker')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Did you go 1 or 2 (or 0)?'
        )

        # After a few seconds, she selects 0, and hits enter
        inputbox.send_keys('0')
        inputbox.send_keys(Keys.ENTER)


        # This makes a flushing noise and starts a (20 minute) countdown timer
        # FIXME: How to test flushing noise?
        timer_text = self.browser.find_element_by_tag_name('h4').text
        self.assertRegex(timer_text,r'\d\d:\d\d:\d\d')


        # It also logs the entry as a sticker in the chart
        joan_chart_url = self.browser.current_url
        self.assertRegex(joan_chart_url, '/charts/.+')
        self.check_for_row_in_sticker_chart('1: #0')
        # TODO: Replace index with timestamp

        # also visible at an API endpoint
        # TODO: Add API test

        # and starts the 20 minute timer again
        timer_text = self.browser.find_element_by_tag_name('h4').text
        self.assertRegex(timer_text,r'\d\d:\d\d:\d\d')

        # Surprise! A couple second after entering the 0, a #1 sneaks up
        # out of nowhere, so Joan enters the 1
        import time
        time.sleep(2)
        inputbox = self.browser.find_element_by_id('id_new_sticker')
        inputbox.send_keys('1')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again to show both entries
        self.check_for_row_in_sticker_chart('1: #0')
        self.check_for_row_in_sticker_chart('2: #1')
        # TODO: Replace index with timestamp


        # After the timer expires, the entire process starts again

        # Now a new user, Francis, comes along to the site. His child's
        # potty needs are quite urgent.


        ## We use a new browser session to make sure that no information
        ## of Joan's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page.  There is no sign of Joan's chart
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: #0', page_text)

        # Francis starts a new chart by entering a new sticker entry
        inputbox = self.browser.find_element_by_id('id_new_sticker')
        inputbox.send_keys('2')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_chart_url = self.browser.current_url
        self.assertRegex(francis_chart_url, '/charts/.+')
        self.assertNotEqual(francis_chart_url, joan_chart_url)

        # Again, there is no trace of Joan's chart
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: #0', page_text)
        self.assertIn('1: #2', page_text)

        # Satisfied, they both go back to sleep

    def test_layout_and_styling(self):
        # Joan goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox=self.browser.find_element_by_id('id_new_sticker')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # She starts a new chart and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_sticker')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

if __name__ == '__main__':
    unittest.main()
