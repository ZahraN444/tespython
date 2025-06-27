# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated for dgfgfdg by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from apimaticcalculator.api_helper import APIHelper


class SimpleCalculatorControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(SimpleCalculatorControllerTests, cls).setUpClass()
        cls.controller = cls.client.simple_calculator
        cls.response_catcher = cls.controller.http_call_back

    # Check if multiplication works
    def test_multiply(self):
        # Parameters for the API call
        options = {}
        options['operation'] = 'MULTIPLY'
        options['x'] = 4
        options['y'] = 5

        # Perform the API call through the SDK function
        result = self.controller.get_calculate(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        assert '20' == self.response_catcher.response.text

