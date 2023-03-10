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
from kiln_connect.openapi_client.models.tezos_stake import TezosStake  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestTezosStake(unittest.TestCase):
    """TezosStake unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TezosStake
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TezosStake`
        """
        model = kiln_connect.openapi_client.models.tezos_stake.TezosStake()  # noqa: E501
        if include_optional :
            return TezosStake(
                stake_address = 'tz1VZ4iC4wzTR7iK2Q7PoQGVDAojuY42fDxD', 
                baker_address = 'tz2FCNBrERXtaTtNX6iimR1UJ5JSDxvdHM93', 
                state = 'active', 
                activated_at = '2023-01-14T01:13:59Z', 
                activated_cycle = 542, 
                delegated_at = '2023-01-14T01:13:59Z', 
                delegated_cycle = 542, 
                delegated_block = '16397387', 
                balance = '32076187808000000000', 
                rewards = '76187808000000000', 
                gross_apy = 3.407, 
                updated_at = '2023-01-14T01:13:59Z'
            )
        else :
            return TezosStake(
        )
        """

    def testTezosStake(self):
        """Test TezosStake"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()