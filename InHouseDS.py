import base64
from pathlib import Path
import pprint

import requests

selfie = '/Users/mkrai/Desktop/fileinput/Multipleface.jpg'
document = 'https://www.wilddigital.com/upload/img/media/image/1776/standard/KevinAluwi-Gojek(2).png'
endpoint = 'http://spoof-classifier-38.kyc-face-anti-spoofing.models.id.s.gods.golabs.io/v1/models/spoof-classifier-38:predict'


class InHouseDS:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.pp = pprint.PrettyPrinter(width=60)

    def to_base64_str(self, path):
        with path.open('rb') as f:
            content = f.read()
            content = base64.b64encode(content)
            s = content.decode()
        return s

    def get_request(self):
        path = Path(selfie)
        request = {
            # Liveness check runs on main image.
            'image': {
                'id': 'my_selfie_123',
                'base64_str': self.to_base64_str(path),
            }
        }
        return request

    def run(self):
        request = self.get_request()
        s = self.pp.pformat(request)
        print(f"Printing Request:\n{s}")

        response = requests.post(endpoint, json=request)
        response = response.json()
        self.pp.pprint(response)
        s = self.pp.pformat(response)
        print(f"Response:\n{s}")

if __name__ == '__main__':
    InHouseDS(endpoint).run()