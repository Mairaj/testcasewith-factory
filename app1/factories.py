import factory
from app1.models import Owner, Car
class OwnerFactory(factory.Factory):
	FACTORY_FOR = Owner
	name='Mairaj'
	phone='+91955540'
class CarFactory(factory.Factory):
	FACTORY_FOR = Car
	name='jeep'
	owner = factory.lazy_attribute(lambda a: OwnerFactory())
