import json
import inspect
import requests


DEFAULT_HOST = 'http://47.254.135.164/translate'
DEFAULT_API_KEY = 'pyecharts-0-5-0-rocks'


class Python2Javascript:
    @staticmethod
    def translate(obj):
        source_lines, _ = inspect.getsourcelines(obj)
        headers = {
            "Content-Type": "application/json",
            "Authorization": DEFAULT_API_KEY
        }
        r = requests.post(
            DEFAULT_HOST,
            headers=headers,
            data=json.dumps({"source": ''.join(source_lines)}))
        if r.status_code == 200:
            content = r.json()
            return content['response']
        else:
            raise IOError("Cannot connect to the online compiler")
