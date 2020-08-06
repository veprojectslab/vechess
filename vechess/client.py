import os
import requests


def run(param):
    base_uri = os.environ["VECHESS_BASE_URI"]
    return(requests.get(base_uri + "state/"))
