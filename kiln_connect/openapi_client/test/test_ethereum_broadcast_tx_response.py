# coding: utf-8

"""
    Kiln API Specifications

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on. In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi. Once you have your API token, you can set it as a bearer token in your request headers.  ### Backward Compatibility  Kiln considers the following changes to be backwards-compatible:  - Adding new API routes. - Adding new optional request parameters to existing API methods. - Adding new properties to existing API responses. - Changing the order of properties in existing API responses. - Adding new event types in existing enums.  Non-breaking changes may be introduced silently in our API and subject to modifications before being officialy communicated and documented here. Your application should not depend on them until part of this specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kiln_connect.openapi_client
from kiln_connect.openapi_client.models.ethereum_broadcast_tx_response import EthereumBroadcastTxResponse  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestEthereumBroadcastTxResponse(unittest.TestCase):
    """EthereumBroadcastTxResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EthereumBroadcastTxResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthereumBroadcastTxResponse`
        """
        model = kiln_connect.openapi_client.models.ethereum_broadcast_tx_response.EthereumBroadcastTxResponse()  # noqa: E501
        if include_optional :
            return EthereumBroadcastTxResponse(
                tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94'
            )
        else :
            return EthereumBroadcastTxResponse(
        )
        """

    def testEthereumBroadcastTxResponse(self):
        """Test EthereumBroadcastTxResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
