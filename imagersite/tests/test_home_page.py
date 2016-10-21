from django.test import TestCase
from django.urls import reverse

class HomePageTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def tearDown(self):
        pass

    def test_home_page_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_for_registration_button(self):
        """assert that the response contains a link to the registration page."""
        reg_url = reverse('registration_register')
        # expected = 'href = {}'.format(reg_url)
        self.assertContains(self.response, reg_url, status_code=200)

    def test_home_page_uses_right_template(self):
        """Assert thatt the home page view uses our template."""
        for name in [
            'imagersite/home_page_splash.html', 'imagersite/base.html'
        ]:
            self.assertTemplateUsed(
                self.response,
                'imagersite/home_page_splash.html')

    def test_home_page_context_contains_foo(self):
        self.assertTrue(b'Welcome to Pricture' in self.response.content)
