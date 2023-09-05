# coding: utf-8

"""
    Jellyfish Media Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import jellyfish_openapi_client
from jellyfish_openapi_client.models.peer_options_web_rtc import PeerOptionsWebRTC  # noqa: E501
from jellyfish_openapi_client.rest import ApiException

class TestPeerOptionsWebRTC(unittest.TestCase):
    """PeerOptionsWebRTC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PeerOptionsWebRTC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeerOptionsWebRTC`
        """
        model = jellyfish_openapi_client.models.peer_options_web_rtc.PeerOptionsWebRTC()  # noqa: E501
        if include_optional :
            return PeerOptionsWebRTC(
                enable_simulcast = True
            )
        else :
            return PeerOptionsWebRTC(
        )
        """

    def testPeerOptionsWebRTC(self):
        """Test PeerOptionsWebRTC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
