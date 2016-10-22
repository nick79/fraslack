from unittest.case import TestCase
from slack import is_file_type_supported

FILE_URL_POSITIVE = 'https://fraslack.herokuapp.com/data/test.txt'
FILE_URL_NEGATIVE = 'https://fraslack.herokuapp.com/data/test.png'
FILE_PATH_POSITIVE = 'G:/test.jpg'
FILE_PATH_NEGATIVE = 'G:/test.py'


class TestSlack(TestCase):
    def test_is_file_type_supported_from_url_positive(self):
        self.assertTrue(is_file_type_supported(FILE_URL_POSITIVE))

    def test_is_file_type_supported_from_url_negative(self):
        self.assertFalse(is_file_type_supported(FILE_URL_NEGATIVE))

    def test_is_file_type_supported_from_path_positive(self):
        self.assertTrue(is_file_type_supported(FILE_PATH_POSITIVE))

    def test_is_file_type_supported_from_path_negative(self):
        self.assertFalse(is_file_type_supported(FILE_PATH_NEGATIVE))
