from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from pottytimer.views import home_page
from pottytimer.models import Sticker, Chart

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Sticker.objects.count(), 0)


class ChartAndStickerModelTest(TestCase):

    def test_saving_and_retrieving_stickers(self):
        chart = Chart()
        chart.save()

        first_sticker = Sticker()
        first_sticker.text = '2'
        first_sticker.chart = chart
        first_sticker.save()

        second_sticker = Sticker()
        second_sticker.text = '0'
        second_sticker.chart = chart
        second_sticker.save()

        saved_chart = Chart.objects.first()
        self.assertEqual(saved_chart, chart)

        saved_stickers = Sticker.objects.all()
        self.assertEqual(saved_stickers.count(), 2)

        first_saved_sticker = saved_stickers[0]
        second_saved_sticker = saved_stickers[1]
        self.assertEqual(first_saved_sticker.text, '2')
        self.assertEqual(first_saved_sticker.chart, chart)
        self.assertEqual(second_saved_sticker.text, '0')
        self.assertEqual(second_saved_sticker.chart, chart)

class ChartViewTest(TestCase):

    def test_uses_chart_template(self):
        response = self.client.get('/charts/lone-chart/')
        self.assertTemplateUsed(response, 'chart.html')


    def test_displays_all_stickers(self):
        chart = Chart.objects.create()
        Sticker.objects.create(text='2!', chart=chart)
        Sticker.objects.create(text='1!', chart=chart)

        response = self.client.get('/charts/lone-chart/')

        self.assertContains(response, '2!')
        self.assertContains(response, '1!')

class NewChartTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/charts/new',
            data={'sticker_text': '0'}
        )
        self.assertEqual(Sticker.objects.count(), 1)
        new_sticker = Sticker.objects.first()
        self.assertEqual(new_sticker.text, '0')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/charts/new',
            data={'sticker_text': '0'}
        )

        self.assertRedirects(response, '/charts/lone-chart/')

