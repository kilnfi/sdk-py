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
from kiln_connect.openapi_client.models.ethereum_kiln_stats_gross_apy import EthereumKilnStatsGrossApy  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestEthereumKilnStatsGrossApy(unittest.TestCase):
    """EthereumKilnStatsGrossApy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EthereumKilnStatsGrossApy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthereumKilnStatsGrossApy`
        """
        model = kiln_connect.openapi_client.models.ethereum_kiln_stats_gross_apy.EthereumKilnStatsGrossApy()  # noqa: E501
        if include_optional :
            return EthereumKilnStatsGrossApy(
                last_1d = 1.337, 
                last_7d = 1.337, 
                last_30d = 1.337
            )
        else :
            return EthereumKilnStatsGrossApy(
        )
        """

    def testEthereumKilnStatsGrossApy(self):
        """Test EthereumKilnStatsGrossApy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
