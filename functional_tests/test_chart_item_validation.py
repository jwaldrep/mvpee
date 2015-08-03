from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_chart_items(self):
        # Joan goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that chart items cannot be blank

        # She tries again with an entry for the item, which now works

        # Perversely, she now decides to submit a second blank chart item

        # She receives a similar warning on the chart page

        # And she can correct it by filling some text in
        self.fail('write me!')
