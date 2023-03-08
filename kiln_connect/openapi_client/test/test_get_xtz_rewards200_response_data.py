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
from kiln_connect.openapi_client.models.get_xtz_rewards200_response_data import GetXtzRewards200ResponseData  # noqa: E501
from kiln_connect.openapi_client.rest import ApiException

class TestGetXtzRewards200ResponseData(unittest.TestCase):
    """GetXtzRewards200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetXtzRewards200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetXtzRewards200ResponseData`
        """
        model = kiln_connect.openapi_client.models.get_xtz_rewards200_response_data.GetXtzRewards200ResponseData()  # noqa: E501
        if include_optional :
            return GetXtzRewards200ResponseData(
                var_date = 'Sun Jan 15 00:00:00 GMT 2023', 
                rewards = 27098488, 
                active_balance = '34329999165', 
                gross_apy = 36.053, 
                cycle = 271, 
                cycle_begins_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return GetXtzRewards200ResponseData(
        )
        """

    def testGetXtzRewards200ResponseData(self):
        """Test GetXtzRewards200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
