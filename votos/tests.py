"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from votos.models import Voto
from votos.models import User

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
