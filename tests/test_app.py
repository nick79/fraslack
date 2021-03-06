import unittest
from unittest import TestCase
from itsdangerous import Signer
import app
import globals
from const import SLACK_PATH, UNSUPPORTED_MESSAGE, FRAME_PATH

FILE_URL_POSITIVE = 'https://fraslack.herokuapp.com/data/test.txt'
FILE_URL_NEGATIVE = 'https://fraslack.herokuapp.com/data/test.png'


class TestApp(TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.post('/')
        self.assertEqual(result.status_code, 200)
        assert 'Index' in result.data

    def test_slack_without_token(self):
        result = self.app.post(SLACK_PATH, data=dict(text=FILE_URL_POSITIVE))
        self.assertEqual(result.status_code, 401)

    def test_slack_negative(self):
        result = self.app.post(SLACK_PATH, data=dict(token=globals.SLACK_TOKEN, text=FILE_URL_NEGATIVE))
        self.assertEqual(result.status_code, 200)
        assert UNSUPPORTED_MESSAGE in result.data

    def test_slack_positive(self):
        result = self.app.post(SLACK_PATH, data=dict(token=globals.SLACK_TOKEN, text=FILE_URL_POSITIVE))
        self.assertEqual(result.status_code, 200)
        assert FILE_URL_POSITIVE in result.data

    def test_frame_bad_link(self):
        result = self.app.get(FRAME_PATH, query_string=dict(file_url=FILE_URL_POSITIVE), follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        assert 'Error Page' in result.data

    def test_frame_positive(self):
        signer = Signer(globals.SECRET_KEY)
        file = signer.sign(FILE_URL_POSITIVE)
        result = self.app.get(FRAME_PATH, query_string=dict(file_url=file), follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        assert 'Frame Integration' in result.data


if __name__ == "__main__":
    unittest.main()
