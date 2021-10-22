import requests

from PySender.request import Request

r = requests.get("https://reqres.in/api/users").json()

