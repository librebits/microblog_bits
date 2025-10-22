import unittest
from app import app
from app.forms import LoginForm


class TestLoginForm(unittest.TestCase):
    """Test LoginForm validation"""

    def setUp(self):
        """Set up test client and app context"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Clean up app context"""
        self.app_context.pop()

    def test_form_fields_exist(self):
        """Test that LoginForm has all required fields"""
        form = LoginForm()
        self.assertTrue(hasattr(form, 'username'))
        self.assertTrue(hasattr(form, 'password'))
        self.assertTrue(hasattr(form, 'remember_me'))
        self.assertTrue(hasattr(form, 'submit'))

    def test_username_required(self):
        """Test that username field is required"""
        form = LoginForm(data={'password': 'test123'})
        self.assertFalse(form.validate())
        self.assertIn('username', form.errors)

    def test_password_required(self):
        """Test that password field is required"""
        form = LoginForm(data={'username': 'testuser'})
        self.assertFalse(form.validate())
        self.assertIn('password', form.errors)

    def test_valid_form(self):
        """Test that form validates with correct data"""
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'testpass',
            'remember_me': True
        })
        self.assertTrue(form.validate())

    def test_remember_me_optional(self):
        """Test that remember_me field is optional"""
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertTrue(form.validate())


if __name__ == '__main__':
    unittest.main()
