import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, DeepSeek Harness!")

    def test_custom_name(self):
        self.assertEqual(greet("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
