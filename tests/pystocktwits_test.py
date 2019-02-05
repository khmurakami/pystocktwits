from pystocktwits import Streamer

import unittest


class TestPyStockTwitsMethods(unittest.TestCase):

    def test_streamer_get_user_msgs(self):
        twit = Streamer()
        output = twit.get_user_msgs("170")
        status_code = output['response']['status']

        # Check to see if the Status code returned by the Web Call is 200 which is success
        self.assertEqual(200, status_code)

    def test_streamer_get_symbol_msgs(self):
        twit = Streamer()
        output = twit.get_symbol_msgs("AAPL")
        status_code = output['response']['status']

        # Check to see if the Status code returned by the Web Call is 200 which is success
        self.assertEqual(200, status_code)

    def test_streamer_get_specified_conversation_msgs(self):
        twit = Streamer()
        output = twit.get_specified_conversation_msgs("10349526")
        status_code = output['response']['status']

        # Check to see if the Status code returned by the Web Call is 200 which is success
        self.assertEqual(200, status_code)


if __name__ == '__main__':
    unittest.main()
