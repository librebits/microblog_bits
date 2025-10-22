import unittest
from app import app


class TestRoutes(unittest.TestCase):
    """Test application routes"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_index_route(self):
        """Test that /index route returns 200"""
        response = self.client.get('/index')
        self.assertEqual(response.status_code, 200)

    def test_root_route(self):
        """Test that / route returns 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_user(self):
        """Test that index page contains username"""
        response = self.client.get('/index')
        self.assertIn(b'Fenix', response.data)

    def test_index_contains_posts(self):
        """Test that index page contains posts"""
        response = self.client.get('/index')
        self.assertIn(b'Juan', response.data)
        self.assertIn(b'Bonito d', response.data)  # Partial match for Spanish chars
        self.assertIn(b'Susan', response.data)
        self.assertIn(b'Tron', response.data)

    def test_index_title(self):
        """Test that index page has correct title"""
        response = self.client.get('/index')
        self.assertIn(b'Home', response.data)

    def test_login_route(self):
        """Test that /login route returns 200"""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_contains_form(self):
        """Test that login page contains form elements"""
        response = self.client.get('/login')
        self.assertIn(b'username', response.data)
        self.assertIn(b'password', response.data)
        self.assertIn(b'Sign In', response.data)

    def test_login_title(self):
        """Test that login page has correct title"""
        response = self.client.get('/login')
        self.assertIn(b'Sign In', response.data)


if __name__ == '__main__':
    unittest.main()
