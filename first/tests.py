from django.contrib.auth.models import User

from django.test import TestCase, Client

from django.urls import reverse


from first.models import CalcHistory


class IndexTest(TestCase):


    def test_index_response(self):

        response = self.client.get(reverse('index'))


        self.assertEqual(response.status_code, 200)


    def test_index_context(self):

        response = self.client.get(reverse('index'))


        self.assertEqual(response.context['pages'], 3)

        self.assertEqual(response.context['auth'], 'Andrew')

        self.assertIn('cr_date', response.context)