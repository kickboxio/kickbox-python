import six

class Kickbox(object):

    """
    """

    def __init__(self, client):
        self.client = client

    def verify(self, email, options={}):
        """Email Verification

        '/verify?email=:email&timeout=:timeout' GET

        Args:
            email: Email address to verify
        """
        body = options['query'] if 'query' in options else {}

        email   = six.moves.urllib.parse.quote(email)
        timeout = options['timeout'] if 'timeout' in options else 6000

        response = self.client.get('/verify?email=' + email + '&timeout=' + str(timeout), body, options)

        return response

