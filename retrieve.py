import requests

import auth
import config

consumer_key = auth.get_consumer_key()
access_token = auth.get_access_token()

def get_whole_archive():

    requestData = {
        "consumer_key": consumer_key,
        "access_token": access_token,
        "state": "archive",
        "sort": "newest",
        "detailType": "simple"
    }

    response = requests.post(
        config.base_url + "/get",
        json=requestData
    )

    if response.status_code == 200:

        return response.content.decode('utf-8')
