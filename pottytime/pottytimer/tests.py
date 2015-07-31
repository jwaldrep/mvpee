from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from pottytimer.views import home_page
from pottytimer.models import Sticker

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sticker_text'] = '0'

        response = home_page(request)
        self.assertIn('0', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_sticker_text':  '0'}
        )
        self.assertEqual(response.content.decode(), expected_html)

class StickerModelTest(TestCase):

    def test_saving_and_retrieving_stickers(self):
        first_sticker = Sticker()
        first_sticker.text = '2'
        first_sticker.save()

        second_sticker = Sticker()
        second_sticker.text = '0'
        second_sticker.save()

        saved_stickers = Sticker.objects.all()
        self.assertEqual(saved_stickers.count(), 2)

        first_saved_sticker = saved_stickers[0]
        second_saved_sticker = saved_stickers[1]
        self.assertEqual(first_saved_sticker.text, '2')
        self.assertEqual(second_saved_sticker.text, '0')
