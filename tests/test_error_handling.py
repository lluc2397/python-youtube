import unittest

from requests import Response

from pyyoutube.error import ErrorCode, ErrorMessage, PyYouTubeException


class ErrorTest(unittest.TestCase):
    base_path = "testdata/"
    with open(f"{base_path}error_response.json", "rb") as f:
        ERROR_DATA = f.read()

    with open(f"{base_path}error_response_simple.json", "rb") as f:
        ERROR_DATA_SIMPLE = f.read()

    def testResponseError(self) -> None:
        response = Response()
        response.status_code = 400
        response._content = self.ERROR_DATA

        ex = PyYouTubeException(response=response)

        self.assertEqual(ex.status_code, 400)
        self.assertEqual(ex.message, "Bad Request")
        self.assertEqual(ex.error_type, "YouTubeException")
        error_msg = "YouTubeException(status_code=400,message=Bad Request)"
        self.assertEqual(repr(ex), error_msg)
        self.assertTrue(str(ex), error_msg)

    def testResponseErrorSimple(self) -> None:
        response = Response()
        response.status_code = 400
        response._content = self.ERROR_DATA_SIMPLE

        ex = PyYouTubeException(response=response)
        self.assertEqual(ex.status_code, 400)

    def testErrorMessage(self):
        response = ErrorMessage(status_code=ErrorCode.HTTP_ERROR, message="error")

        ex = PyYouTubeException(response=response)

        self.assertEqual(ex.status_code, 10000)
        self.assertEqual(ex.message, "error")
        self.assertEqual(ex.error_type, "PyYouTubeException")
