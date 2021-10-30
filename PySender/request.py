import requests

# from PySender.errors import NoValidUrl


class Request:
    def __init__(self, url, rtype="GET", **kwargs):
        self.request = None
        self.auth = (None, None)
        self.type = rtype
        self.url = url
        self.kwargs = kwargs

    def set_type(self, type):
        self.type = type

    def set_url(self, url):
        self.url = url

    def set_auth(self, user, passwd):
        self.auth = (user, passwd)

    def send(self):
        pass
        # if self.type == "GET":
            # try:
            #     self.request = requests.get(self.url)
            # except requests.exceptions.MissingSchema:
                # NoValidUrl()
