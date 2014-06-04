class Kickbox(object):

    """
    """

    def __init__(self, client):
        self.client = client

    def verify(self, email, options={}):
        """Email Verification

        '/verify?email=:email' GET

        Args:
            email: Email address to verify
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/verify?email=' + email + '', body, options)

        return response

