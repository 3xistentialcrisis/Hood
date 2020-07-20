from django.test import TestCase
from .models import Neighbourhood, Profile, Business

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighbourhood_name = 'Westlands')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))