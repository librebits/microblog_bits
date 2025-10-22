import unittest
import os
from config import Config


class TestConfig(unittest.TestCase):
    """Test application configuration"""

    def test_secret_key_exists(self):
        """Test that SECRET_KEY is set"""
        self.assertIsNotNone(Config.SECRET_KEY)

    def test_secret_key_fallback(self):
        """Test that SECRET_KEY has a fallback value"""
        # Remove env var if it exists
        old_value = os.environ.get('SECRET_KEY')
        if 'SECRET_KEY' in os.environ:
            del os.environ['SECRET_KEY']

        # Reload config
        from importlib import reload
        import config
        reload(config)

        self.assertEqual(config.Config.SECRET_KEY, 'you-will-never-guess')

        # Restore old value
        if old_value:
            os.environ['SECRET_KEY'] = old_value

    def test_secret_key_from_environment(self):
        """Test that SECRET_KEY can be loaded from environment"""
        test_key = 'test-secret-key-123'
        os.environ['SECRET_KEY'] = test_key

        # Reload config
        from importlib import reload
        import config
        reload(config)

        self.assertEqual(config.Config.SECRET_KEY, test_key)

        # Cleanup
        del os.environ['SECRET_KEY']


if __name__ == '__main__':
    unittest.main()
