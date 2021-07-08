import base64
import pprint
from pathlib import Path

import requests

selfie = '/Users/mkrai/Desktop/fileinput/Multipleface.jpg'
syncendpoint = 'https://eve.idfy.com/v3/tasks/sync/check_photo_liveness/face'
asyncendpoint = 'https://eve.idfy.com/v3/tasks/sync/check_photo_liveness/face'


class IDfyLiveness:
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
            'task_id': '74f4c926-250c-43ca-9c53-453e87ceacd1',
            'group_id': "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
            'data': {
                'document1': self.to_base64_str(path),
            }
        }
        return request

    def run(self):
        request = self.get_request()
        s = self.pp.pformat(request)
        print(f"Printing Request:\n{s}")

        headers = {"api-key": "7d2be589-6f24-4d4e-8e5c-a7efc7c41340 ",
                   "account-id": "2cd0fb2a059c/5f2134c8-f3c6-41d9-ae89-c1b3faf94f54",
                   "Content-Type": "application/json",
                   }

        response = requests.post(syncendpoint, json=request, headers=headers)
        response = response.json()
        self.pp.pprint(response)
        s = self.pp.pformat(response)
        print(f"Response:\n{s}")


if __name__ == '__main__':
    idfy = IDfyLiveness(syncendpoint)

    idfy.run()
