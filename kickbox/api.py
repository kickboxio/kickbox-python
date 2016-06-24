import requests
from .errors import ErrorHandler
from .response_handler import ResponseHandler


class Client(object):

    # Define base url
    BASE_URL = "https://api.kickbox.io"

    def make_request(self, url, method='get', params={}):
        headers = {
            'user-agent':
                'kickbox-python/3.0.0 (https://github.com/kickboxio/kickbox-python)'
        }

        url = "%s%s" % (self.BASE_URL, url)

        if method is 'get':
            response = requests.get(
                url, headers=headers, params=params, hooks=dict(
                    response=ErrorHandler.check_error
                )
            )
        else:
            response = requests.post(url, headers=headers, params=params)

        return ResponseHandler.get_body(response)


class Verification(Client):

    """Verification."""

    def __init__(self, api_key, version='v2'):
        """ad.

        Args:
            api_key: API key of the authentication app
        """
        self.api_key = api_key
        self.version = version

    def verify(self, email, timeout=6000):
        """Verify an Email address.

        Args:
            email: email to be verified
        """
        url = "/%s/verify" % (self.version)

        response = self.make_request(
            url=url, method="get", params={
                'email': email, 'api_key': self.api_key, 'timeout': timeout
            }
        )
        return response


class Authentication(Client):

    def __init__(self, app_code, api_key):
        """
        Args:
            app_code: The code for the authentication app
            api_key: Your API key of the authentication app
        """
        self.app_code = app_code
        self.api_key = api_key
        super(Authentication, self).__init__()

    def authenticate(self, fingerprint):
        """Send the authentication email.

        Args:
            fingerprint: The fingerprint for the email address
        """
        url = "/v2/authenticate/%s" % (self.app_code)
        params = {'api_key': self.api_key, 'fingerprint': fingerprint}
        response = self.make_request(url=url, method='post', params=params)
        return response

    def getStatus(self, id):
        """Get the status of an authentication.

        Args:
            id: Authentication id returned from the authenticate request
        """
        url = "/v2/authenticate/%s/%s" % (self.app_code, id)
        params = {'api_key': self.api_key}
        response = self.make_request(url=url, method='get', params=params)
        return response
