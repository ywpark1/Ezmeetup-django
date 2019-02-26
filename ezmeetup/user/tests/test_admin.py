from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.admin_user = get_user_model().objects.create_superuser(
            email='admin@ezmeetup.ca',
            password='password123'
        )

        cls.user = get_user_model().objects.create_user(
            email='user1@ezmeetup.ca',
            first_name='User',
            last_name='One',
            phone_number='123-456-7890',
            password='password123'
        )

    def setUp(self):
        self.client.force_login(self.admin_user)

    def test_users_listed(self):
        """ Test that users are listed on user page """
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test that user edit page works """
        url = reverse('admin:user_user_change', args=[self.user.id])
        # /admin/user/user/:id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that user create page works """
        url = reverse('admin:user_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
