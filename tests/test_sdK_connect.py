import unittest

from kiln_connect import sdk


class TestApiUrl(unittest.TestCase):

    def test_devnet(self):
        self.assertEqual(
            'https://api.devnet.kiln.fi/', sdk.get_api_url('devnet'))

    def test_testnet(self):
        self.assertEqual(
            'https://api.testnet.kiln.fi/', sdk.get_api_url('testnet'))

    def test_mainnet(self):
        self.assertEqual(
            'https://api.kiln.fi/', sdk.get_api_url('mainnet'))

    def test_invalid_env(self):
        with self.assertRaises(sdk.InvalidEnvError):
            sdk.get_api_url('goerli')


if __name__ == '__main__':
    unittest.main()
