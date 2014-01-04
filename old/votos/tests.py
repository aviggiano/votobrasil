"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import django
from django.test import TestCase
from django.test import LiveServerTestCase
from django.test.client import Client
from django.test.client import RequestFactory
from selenium.webdriver.firefox.webdriver import WebDriver
from rebar.testing import flatten_to_dict
from votos.models import Voto
from votos.models import User
from votos.views import *
from votos import forms

import django.http
import django.utils.unittest as unittest2

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class UserTest(TestCase):
    """User test cases"""
    
    def test_str(self):

        user = User(username='toonhao', email='toonhao@gmail.com')

        self.assertEquals(
            str(user),
            'toonhao,toonhao@gmail.com',
        )

class VotoTest(TestCase):
    """Voto test cases"""
    
    def test_str(self):

        voto = Voto(partido='PT', num_votos='9')

        self.assertEquals(
            str(voto),
            'PT,9',
        )

class UserListViewTests(TestCase):
    """User list view tests."""

    def test_users_in_the_context(self):
        
        django.test.utils.setup_test_environment() # needed to see response context

        client = Client()
        response = client.get('/users/')

        self.assertEquals(list(response.context['user_list']), [])

        User.objects.create(username='foo', email='foo@bar.com')
        response = client.get('/users/')
        self.assertEquals(response.context['user_list'].count(), 1)

    def test_users_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/users/')

        response = ListUsersView.as_view()(request)

        self.assertEquals(list(response.context_data['user_list']), [])

        User.objects.create(username='foo', email='foo@bar.com')
        response = ListUsersView.as_view()(request)
        self.assertEquals(response.context_data['user_list'].count(), 1)

class UserListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(UserListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UserListIntegrationTests, cls).tearDownClass()

    def test_user_listed(self):

        # create a test user
        User.objects.create(username='foo', email='foo@bar.com')

        # make sure it's listed as <first> <last> on the list
        self.selenium.get('%s%s' % (self.live_server_url, '/users/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.user')[0].text,
            'foo,foo@bar.com (edit)' # mudar esse teste! ele esta horrivel
        )

    def test_add_user_linked(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/new'))
        self.assert_(
            self.selenium.find_element_by_link_text('back to list')
        )

    def test_add_user(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/new'))

        self.selenium.find_element_by_id('id_username').send_keys('test')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')
        self.selenium.find_element_by_id('id_confirm_email').send_keys('test@example.com')

        self.selenium.find_element_by_id("save-user").click()
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.user')[-1].text,
            'test,test@example.com (edit)' # mudar esse teste! ele esta horrivel
        )

class EditUserFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(forms.UserForm())
        form_data['username'] = 'Foo'
        form_data['email'] = 'foo@bar.com'
        # form_data['owner'].selected = self.owner
        form_data['confirm_email'] = 'x@y.com'

        bound_form = forms.UserForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(forms.UserForm())
        form_data['username'] = 'Foo'
        form_data['email'] = 'foo@bar.com'
        # form_data['owner'].selected = self.owner
        form_data['confirm_email'] = 'foo@bar.com'
        bound_form = forms.UserForm(data=form_data)
        self.assert_(bound_form.is_valid())

class LocaleMiddlewareTests(unittest2.TestCase):

    def test_request_not_processed(self):

        middleware = LocaleMiddle()
        response = django.http.HttpResponse()
        middleware.process_response(none, response)

        self.assertFalse(response.cookies)

class TestClient(TestCase):

    def test_client(self):

        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)

        response = c.post('/login/', {'username': 'root', 'password': 'root'})
