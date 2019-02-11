from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        successful_user_info = {
            'email': 'test@ezmeetup.ca',
            'password': 'testpass123',
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'phone_number': '123-456-7890'
        }

        user = get_user_model().objects.create_user(**successful_user_info)

        self.assertEqual(user.email,
                         successful_user_info['email'])
        self.assertEqual(user.first_name,
                         successful_user_info['first_name'])
        self.assertEqual(user.last_name,
                         successful_user_info['last_name'])
        self.assertEqual(user.phone_number,
                         successful_user_info['phone_number'])

        self.assertTrue(user.check_password(successful_user_info['password']))

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'admin@ezmeetup.ca',
            'adminPass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
