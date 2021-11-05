import json

import requests


class Request:
    def __init__(self, url, method, user, passwd, params=None):
        self.url = url
        self.method = method
        self.user = user
        self.passwd = passwd
        self.params = params

    def send(self):
        request = getattr(requests, self.method)(self.url,
                                                 auth=(self.user, self.passwd),
                                                 **{"params" if self.method == "GET" else "data": self.params})
        res = json.dumps(request.json(), indent=2, sort_keys=True)
        status_code = request.status_code
        return res, status_code
