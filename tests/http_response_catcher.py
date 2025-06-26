# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated for dgfgfdg by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimaticcalculator.http.http_call_back import HttpCallBack

class HttpResponseCatcher(HttpCallBack):

    """A class used for catching the HttpResponse object from controllers.
    
    This class inherits HttpCallBack and implements the on_after_response
    method to catch the HttpResponse object as returned by the HttpClient
    after a request is executed.

    """

    @property
    def response(self):
        return self._response

    def __init__(self):
        self._response = None

    def on_before_request(self, request):
        pass

    def on_after_response(self, response):
        self._response = response



