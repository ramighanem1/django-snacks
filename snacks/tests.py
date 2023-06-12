from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_url_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_usage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')  


class AboutPageTest(TestCase):
    def test_about_url_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_template_usage(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')  
