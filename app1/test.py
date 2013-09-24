from app1.models import Car,Owner
from django.test.testcases import TestCase

class FactoryTestCase(TestCase):

    def test_car_factory(self):
        car = CarFactory()
        self.assertTrue(isinstance(car, Car))

    def test_owner_factory(self):
        owner = OwnerFactory()
        self.assertTrue(isinstance(owner, Owner))
