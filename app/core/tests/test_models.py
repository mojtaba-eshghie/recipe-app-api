
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@mojtaba.com"
        password = "this is password!!"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    
    def test_new_user_email_normalized(self):
        """Test the email to see if a new user email is normalized"""
        email = "test@LONDonApp.coM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
    

    def test_new_user_invalid_email(self):
        """Test creating email with no email raises error"""
        with self.assertRaises(ValueError):
            # WE CRAVE FOR A VALUEERROR!, and if it does not raise a value error,
            # then this test will fail
            get_user_model().objects.create_user(None, 'test123')
