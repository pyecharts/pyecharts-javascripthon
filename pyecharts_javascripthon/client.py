import os
import json
import inspect
import requests

ENV_KEY_HOST = "SCRIPTHON_HOST"
ENV_KEY_API_TOKEN = "SCRIPTHON_API_TOKEN"

DEFAULT_HOST = '47.254.144.94'
DEFAULT_API_KEY = 'pyecharts-0-5-0-rocks'
DEFAULT_API_ENDPOINT = 'http://{0}/translate'


class Python2Javascript:

    @staticmethod
    def translate(obj):
        source_lines, _ = inspect.getsourcelines(obj)
        host_name = get_host_name()
        host = DEFAULT_API_ENDPOINT.format(host_name)
        api_token = get_api_token()
        headers = {
            "Content-Type": "application/json", "Authorization": api_token
        }
        r = requests.post(
            host,
            headers=headers,
            data=json.dumps({"source": ''.join(source_lines)}),
        )
        if r.status_code == 200:
            content = r.json()
            return content['response']

        else:
            raise IOError("Cannot connect to the online compiler")


def get_host_name():
    host = os.environ.get(ENV_KEY_HOST)
    if host is None:
        host = DEFAULT_HOST
    return host


def get_api_token():
    api_token = os.environ.get(ENV_KEY_API_TOKEN)
    if api_token is None:
        api_token = DEFAULT_API_KEY
    return api_token
