
import requests
import logging
import pytest
import json

class TestRequests(object):
    logging.getLogger().setLevel(logging.INFO)
    # logging.basicConfig(level=logging.INFO)
    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(r.json())
        # print(r.json())
        print(json.dumps(r.json(),indent=2))
