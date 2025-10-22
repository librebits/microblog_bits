import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    """Test Flask application setup"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_app_exists(self):
        """Test that app instance exists"""
        self.assertIsNotNone(app)

    def test_app_is_flask_instance(self):
        """Test that app is a Flask instance"""
        from flask import Flask
        self.assertIsInstance(app, Flask)

    def test_secret_key_configured(self):
        """Test that SECRET_KEY is configured"""
        self.assertIsNotNone(app.config.get('SECRET_KEY'))

    def test_testing_mode(self):
        """Test that testing mode can be enabled"""
        self.assertTrue(self.app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
