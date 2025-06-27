# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated for dgfgfdg by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import os
import unittest
from tests.http_response_catcher import HttpResponseCatcher
from apimaticcalculator.configuration import Configuration, Environment
from apimaticcalculator.apimaticcalculator_client import ApimaticcalculatorClient


class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ControllerTestBase.create_configuration()
        cls.client = ApimaticcalculatorClient(config=cls.config)

    @staticmethod
    def create_configuration():
        environment = os.getenv('APIMATICCALCULATOR_ENVIRONMENT')

        if environment is not None:
            environment = Environment[environment.upper()]

        config = Configuration(http_call_back=HttpResponseCatcher())
        return config.clone_with(environment=environment)

