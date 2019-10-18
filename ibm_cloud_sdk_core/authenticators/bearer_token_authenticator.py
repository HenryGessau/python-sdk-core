# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .authenticator import Authenticator
from requests import Request

class BearerTokenAuthenticator(Authenticator):
    """The BearerTokenAuthenticator will add a user-supplied bearer token
    to requests.

    The bearer token will be sent as an Authorization header in the form:

         Authorization: Bearer <bearer-token>

    Args:
        bearer_token: The user supplied bearer token.

    Raises:
        ValueError: Bearer token is none.
    """
    authentication_type = 'bearerToken'

    def __init__(self, bearer_token: str):
        self.bearer_token = bearer_token
        self.validate()

    def validate(self):
        """Validate the bearer token.

        Ensures the bearer token is valid for service operations.

        Raises:
            ValueError: The bearer token is not valid for service operations.
        """
        if self.bearer_token is None:
            raise ValueError('The bearer token shouldn\'t be None.')

    def authenticate(self, req: Request):
        """Adds bearer authentication information to the request.

        The bearer token will be added to the request's headers in the form:

            Authorization: Bearer <bearer-token>

        Args:
            req: The request to add bearer authentication information too. Must contain a key to a dictionary
            called headers.
        """
        headers = req.get('headers')
        headers['Authorization'] = 'Bearer {0}'.format(self.bearer_token)

    def set_bearer_token(self, bearer_token: str):
        """Set a new bearer token to be sent in subsequent service operations.

        Args:
            bearer_token: The bearer token that will be sent in service requests.
        """
        self.bearer_token = bearer_token