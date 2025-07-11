# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated for dgfgfdg by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimaticcalculator.api_helper import APIHelper
from apimaticcalculator.configuration import Server
from apimaticcalculator.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from apimaticcalculator.http.http_method_enum import HttpMethodEnum


class SimpleCalculatorController(BaseController):

    """A Controller to access Endpoints in the apimaticcalculator API."""
    def __init__(self, config):
        super(SimpleCalculatorController, self).__init__(config)

    def get_calculate(self,
                      options=dict()):
        """Does a GET request to /{operation}.

        Calculates the expression using the specified operation.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    operation -- OperationType -- The operator to apply on the
                        variables
                    x -- float -- The LHS value
                    y -- float -- The RHS value

        Returns:
            float: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.CALCULATOR)
            .path('/{operation}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('operation')
                            .value(options.get('operation', None))
                            .should_encode(True))
            .query_param(Parameter()
                         .key('x')
                         .value(options.get('x', None)))
            .query_param(Parameter()
                         .key('y')
                         .value(options.get('y', None)))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()
