from .response_handler import ResponseHandler


class Error(Exception):
    def __init__(self, message, code):
        super(Error, self).__init__()
        self.message = message
        self.code = code


class ErrorHandler(object):
    @staticmethod
    def check_error(response, *args, **kwargs):
        code = response.status_code
        content_type = response.headers.get('content-type')

        if code in range(500, 600):
            raise Error('Error ' + str(code), code)

        # handle rate limit
        elif code is 429:
            raise Error('Rate limit exceeded.')
        elif code in range(400, 500):
            body = ResponseHandler.get_body(response)
            message = body

            if content_type.find('json') != -1:
                message = body['message']

            raise Error(message, code)
