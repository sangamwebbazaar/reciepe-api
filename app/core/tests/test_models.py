from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succeddfull(self):
        """Test creating new user with email is successfull """
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
              email=email,
              password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized """
        email = "test@LONDONAPPDEV.COM"
        user = get_user_model().objects.create_user(email, "test@123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating new user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test create new superuser """
        user = get_user_model().objects.create_superuser(
               'test@india.com',
               'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
