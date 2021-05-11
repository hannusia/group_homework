import json
import requests

class TwitterAPIParser:
    """
    """

    def __init__(self, url, token="AAAAAAAAAAAAAAAAAAAAAAwUNAEAAAAAqVWSjH39LC2XWMTFCI3sytyH5jQ%3DgcBL1mnf2nonHiEhpLlNuCk0p3oIzC9sbzIaLuQ93DuQ4NiJpY"):
        """
        initializes TwitterAPIParser

        all necessary functions are executed, in __init__
        Tweet text can be accessed as self.text after initialization of instance

        :param url: Tweet url
        :param token: bearer token
        """
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAAwUNAEAAAAAqVWSjH39LC2XWMTFCI3sytyH5jQ%3DgcBL1mnf2nonHiEhpLlNuCk0p3oIzC9sbzIaLuQ93DuQ4NiJpY"
        self.id = url.split('/')[-1]
        self.url = url

        self.get_twitter_response()
        self.get_text()

    def get_twitter_response(self):
        """
        gets Twitter API response using bearer token
        """
        base_url = "https://api.twitter.com/"

        bearer_token = self.bearer_token

        search_url = '{}2/tweets/{}'.format(base_url, self.id)

        search_headers = {
            'Authorization': 'Bearer {}'.format(bearer_token)
        }

        search_params = {}

        response = requests.get(search_url, headers = search_headers, params=search_params)
        self.response = response
        return response

    def get_text(self):
        """
        gets text field from Twiiter json file
        """
        self.text = self.response.json()['data']['text']
        return self.text
