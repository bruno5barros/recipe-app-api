from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='barroscorreiabruno@gmail.com', password='12345'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new User with an email is successful"""
        email = 'bruno5barros@hotmail.com'
        password = 'test12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""
        email = "bruno5barros@HOTMAIL.com"
        user = get_user_model().objects.create_user(
            email=email,
            password='test12345'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12345')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'bruno5barros@hotmail.com',
            'test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingridient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingridient), ingridient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom souce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
