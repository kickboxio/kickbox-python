from .http_client import HttpClient

# Assign all the api classes
from .api.kickbox import Kickbox


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def kickbox(self):
        """
        """
        return Kickbox(self.http_client)

