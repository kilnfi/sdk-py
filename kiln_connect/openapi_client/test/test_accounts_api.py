# coding: utf-8

"""
    Kiln API Specifications

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on. In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi. Once you have your API token, you can set it as a bearer token in your request headers.  ### Backward Compatibility  This is an experimental specification used for development and testing, do not rely on what is here unless you know the implications.  The official Kiln API specification following backward compatible changes can be found [here](/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kiln_connect.openapi_client
from kiln_connect.openapi_client.api.accounts_api import AccountsApi  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = kiln_connect.openapi_client.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account(self):
        """Test case for get_account

        Account  # noqa: E501
        """
        pass

    def test_get_account_portfolio(self):
        """Test case for get_account_portfolio

        Account Portfolio  # noqa: E501
        """
        pass

    def test_get_accounts(self):
        """Test case for get_accounts

        Accounts  # noqa: E501
        """
        pass

    def test_post_account(self):
        """Test case for post_account

        Accounts  # noqa: E501
        """
        pass

    def test_put_account(self):
        """Test case for put_account

        Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
