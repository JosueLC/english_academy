import unittest

from app.core.services.eslfast import parse_home, parse_course, parse_class

class ScrapperTest(unittest.TestCase):
    # test to parse_home. Check if the result is a list
    def test_parse_home(self):
        self.assertIsInstance(parse_home(), list)

    # test to parse_course. Check if the result is a list
    def test_parse_course(self):
        self.assertIsInstance(parse_course('https://www.eslfast.com/beginners/'), list)

    # test to parse_class. Check if the result is a tuple
    def test_parse_class(self):
        self.assertIsInstance(parse_class('https://www.eslfast.com/beginners/index1.htm'), tuple)