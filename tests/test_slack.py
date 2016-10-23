import unittest
from unittest import TestCase
from itsdangerous import TimestampSigner
from const import UNSUPPORTED_MESSAGE, SECRET_KEY, LINK_DURATION
from slack import is_file_type_supported, process_command

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

    def test_process_command_positive(self):
        signer = TimestampSigner(SECRET_KEY)
        to_be_unsigned = process_command(FILE_URL_POSITIVE).split("?file_url=")[1]
        got = signer.unsign(to_be_unsigned, max_age=LINK_DURATION)
        self.assertEqual(FILE_URL_POSITIVE, got)

    def test_process_command_negative(self):
        self.assertEqual(UNSUPPORTED_MESSAGE, process_command(FILE_URL_NEGATIVE))


if __name__ == '__main__':
    unittest.main()
