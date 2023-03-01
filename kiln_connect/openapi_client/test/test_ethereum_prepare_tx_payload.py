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
from kiln_connect.openapi_client.models.ethereum_prepare_tx_payload import EthereumPrepareTxPayload  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestEthereumPrepareTxPayload(unittest.TestCase):
    """EthereumPrepareTxPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EthereumPrepareTxPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthereumPrepareTxPayload`
        """
        model = kiln_connect.openapi_client.models.ethereum_prepare_tx_payload.EthereumPrepareTxPayload()  # noqa: E501
        if include_optional :
            return EthereumPrepareTxPayload(
                unsigned_tx_serialized = '0x20a40259b763d549dfa1c082776a036dd8dabbe8b5e32ee721be017512dc', 
                r = 'de28e9efee4c8de422a3c64bfaaee11a32f7cf12bdd3f00dcce41a79fe776c65', 
                s = '3f233eb69495fa4741ad28ef0ba40612bacaf08331fd76041c371f5a2ecc2ab5', 
                v = 0
            )
        else :
            return EthereumPrepareTxPayload(
                unsigned_tx_serialized = '0x20a40259b763d549dfa1c082776a036dd8dabbe8b5e32ee721be017512dc',
                r = 'de28e9efee4c8de422a3c64bfaaee11a32f7cf12bdd3f00dcce41a79fe776c65',
                s = '3f233eb69495fa4741ad28ef0ba40612bacaf08331fd76041c371f5a2ecc2ab5',
                v = 0,
        )
        """

    def testEthereumPrepareTxPayload(self):
        """Test EthereumPrepareTxPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
