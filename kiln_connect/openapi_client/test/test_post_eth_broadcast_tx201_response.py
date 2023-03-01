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
import datetime

import kiln_connect.openapi_client
from kiln_connect.openapi_client.models.post_eth_broadcast_tx201_response import PostEthBroadcastTx201Response  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestPostEthBroadcastTx201Response(unittest.TestCase):
    """PostEthBroadcastTx201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostEthBroadcastTx201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostEthBroadcastTx201Response`
        """
        model = kiln_connect.openapi_client.models.post_eth_broadcast_tx201_response.PostEthBroadcastTx201Response()  # noqa: E501
        if include_optional :
            return PostEthBroadcastTx201Response(
                data = kiln_connect.openapi_client.models.ethereum_broadcast_tx_response.EthereumBroadcastTxResponse(
                    tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94', )
            )
        else :
            return PostEthBroadcastTx201Response(
        )
        """

    def testPostEthBroadcastTx201Response(self):
        """Test PostEthBroadcastTx201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()