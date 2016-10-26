import unittest
from unittest import TestCase
from frame import file_exist

FILE_URL_POSITIVE = 'https://fraslack.herokuapp.com/data/test.txt'
FILE_URL_NEGATIVE = 'https://fraslack.herokuapp.com/data/test.png'


class TestForte(TestCase):
    def test_file_exist_negative(self):
        self.assertFalse(file_exist(FILE_URL_NEGATIVE))

    def test_file_exist_positive(self):
        self.assertTrue(file_exist(FILE_URL_POSITIVE))


if __name__ == "__main__":
    unittest.main()
