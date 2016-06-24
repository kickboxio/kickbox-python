class ResponseHandler(object):

    """ResponseHandler takes care of decoding the response body into suitable type."""

    @staticmethod
    def get_body(response):
        body = response.text
        content_type = response.headers.get('content-type')

        if content_type.find('json') != -1:
            body = response.json()

        return body
