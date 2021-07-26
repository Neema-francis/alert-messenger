import factory
from faker import Factory

from django.contrib.auth.models import User

from app.models import AlertNotification

fake = Factory.create() # generates fake data


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{}@gmail.com'.format(n))
    email = factory.SelfAttribute('username')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_active = True

    class Meta:
        model = User
        django_get_or_create = ('username',)


class AlertNotificationFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    alert_msg = factory.LazyAttribute(lambda x: fake.text())

    class Meta:
        model = AlertNotification