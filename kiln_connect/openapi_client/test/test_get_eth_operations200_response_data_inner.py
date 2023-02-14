# coding: utf-8

"""
    Kiln Connect

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on.  In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi.  Once you have your API token, you can set it as a bearer token in your request headers.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kiln_connect.openapi_client
from kiln_connect.openapi_client.models.get_eth_operations200_response_data_inner import GetEthOperations200ResponseDataInner  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestGetEthOperations200ResponseDataInner(unittest.TestCase):
    """GetEthOperations200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEthOperations200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEthOperations200ResponseDataInner`
        """
        model = kiln_connect.openapi_client.models.get_eth_operations200_response_data_inner.GetEthOperations200ResponseDataInner()  # noqa: E501
        if include_optional :
            return GetEthOperations200ResponseDataInner(
                type = 'execution_reward', 
                var_date = '2023-01-14T01:13:59Z', 
                validator_address = '0x95373bcf8e2c64e1c373a6e534c002f210adbcc84c5abda3b6306677e171430ae50781a51c9f579a47622e334dba2412', 
                tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94', 
                tx_gas_used = '2700999916653262', 
                tx_sender = '0x41bf25fc8c52d292bd66d3bcecd8a919ecb9ef88', 
                proxied_by = '0x1e68238cE926DEC62b3FBC99AB06eB1D85CE0270', 
                block = 15955054, 
                withdrawal_credentials = '010000000000000000000000e1f4acc0affb36a805474e3b6ab786738c6900a2', 
                amount = '3467036438000000000', 
                fee_recipient = '0x1e68238cE926DEC62b3FBC99AB06eB1D85CE0270', 
                mev_payout_tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94', 
                mev_payout_tx_sender = '0x1e68238cE926DEC62b3FBC99AB06eB1D85CE0270'
            )
        else :
            return GetEthOperations200ResponseDataInner(
        )
        """

    def testGetEthOperations200ResponseDataInner(self):
        """Test GetEthOperations200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()