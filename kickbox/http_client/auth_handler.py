class AuthHandler(object):

    """AuthHandler takes care of devising the auth type and using it"""

    HTTP_HEADER = 1

    def __init__(self, auth):
        self.auth = auth

    def get_auth_type(self):
        """Calculating the Authentication Type"""

        if 'http_header' in self.auth:
            return self.HTTP_HEADER

        return -1

    def set(self, request):
        if len(self.auth.keys()) == 0:
            raise StandardError("Server requires authentication to proceed further. Please check")

        auth = self.get_auth_type()
        flag = False

        if auth == self.HTTP_HEADER:
            request = self.http_header(request)
            flag = True

        if not flag:
            raise StandardError("Unable to calculate authorization method. Please check")

        return request

    def http_header(self, request):
        """Authorization with HTTP header"""
        request['headers']['Authorization'] = 'token ' + self.auth['http_header']
        return request

