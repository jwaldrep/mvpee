from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_log_a_potty_training_cycle(self):
        # Joan has heard about a cool new potty-training app to use with her toddler.
        # She visits the site with her potty-training son, Harold
        self.browser.get('http://localhost:8000')

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
                'Did you go 1 or 2? (0 = try)'
        )

        # After a few seconds, she selects 0, and hits enter
        inputbox.send_keys('0')
        inputbox.send_keys(Keys.ENTER)


        # This makes a flushing noise and starts a (20 minute) countdown timer
        # FIXME: How to test flushing noise?
        timer_text = self.browser.find_element_by_tag_name('h4').text
        self.assertRegex(timer_text,r'\d\d:\d\d:\d\d')


        # It also logs the entry as a sticker in the chart
        table = self.browser.find_element_by_id('id_sticker_chart')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: #0', [row.text for row in rows])
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
        table = self.browser.find_element_by_id('id_sticker_chart')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2: #1', [row.text for row in rows])
        # TODO: Replace index with timestamp



        # After the timer expires, the entire process starts again

if __name__ == '__main__':
    unittest.main()
