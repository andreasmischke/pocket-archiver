import json
import requests

import config

access_token = None

def get_consumer_key():
    return config.pocket_consumer_key

def get_access_token():
    global access_token

    if access_token is None:
        access_token = _obtain_access_token()

    return access_token

def _load_access_token():
    with open(config.access_token_file) as f:
        return f.read()

def _store_access_token(token):
    with open(config.access_token_file, 'w') as f:
        f.write(token)

def _request_access_token():

    headers = {
        "X-Accept": "application/json"
    }
    requestData = {
        "consumer_key": get_consumer_key(),
        "redirect_uri": config.redirect_uri
    }

    response = requests.post(
        config.base_url + "/oauth/request",
        json=requestData,
        headers=headers
    )

    sc = response.status_code
    if sc > 400:
        print("Sorry, something went wrong, HTTP Status:", sc)
    else:
        response_json = response.content.decode('utf-8')
        request_token = json.loads(response_json)['code']

    print('Please open the following URL in your favorite browser',
          'and give access to this application:')
    print('https://getpocket.com/auth/authorize' +
          '?request_token={}&redirect_uri={}'.format(request_token,
                                                     config.redirect_uri))
    input("After that come back here and press <Enter>: ")

    del requestData['redirect_uri']
    requestData['code'] = request_token

    response = requests.post(
        config.base_url + "/oauth/authorize",
        json=requestData,
        headers=headers
    )

    sc = response.status_code
    if sc == 200:
        response_json = response.content.decode('ascii')
        response_obj = json.loads(response_json)

        access_token = response_obj['access_token']
        _store_access_token(access_token)

        username = response_obj['username']
        print("successfully obtained access_token for user", username)
    else:
        print('Sorry, something went wrong while obtaining the access_token.',
              'HTTP Status:', sc)

    return access_token

def _obtain_access_token():

    try:
        return _load_access_token()
    except FileNotFoundError:
        return _request_access_token()

