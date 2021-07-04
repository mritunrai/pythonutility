import base64
import json
import os
import sys

import pprint

from pathlib import Path

import requests

endpoint = 'http://spoof-classifier-26.kyc-face-anti-spoofing.models.id.s.gods.golabs.io/v1/models/spoof-classifier-26:predict'

class LivenessInHouse:

    def __init__(self, endpoint):
        self.enpoint = endpoint
        self.pp = pprint.PrettyPrinter(width=60)

    def to_base64_str(self, path):
        with path.open('rb') as f:
            content = f.read()
            content = base64.b64encode(content)
            s = content.decode()
        return s

    def get_request(self,file):
        path = Path(file)
        request = {
            # Liveness check runs on main image.
            'image': {
                'id': 'my_selfie_123',
                'base64_str': self.to_base64_str(path),
            }
        }
        return request

    def run(self, file):
        request = self.get_request(file)
        s = self.pp.pformat(request)
        print(f"Printing Request:\n{s}")

        response = requests.post(endpoint, json=request)
        response = response.json()
        self.pp.pprint(response)
        s = self.pp.pformat(response)
        print(f"Response:\n{s}")

        return s

    def listAllSelfie(self,selfie_dir,result_dir):
        try:
            file_path = os.path.expanduser('~') + "/" + selfie_dir
            print("***Use current dir to process each images***:" + file_path)
            target_dir = os.path.expanduser('~') + "/" + result_dir
            print("***Use target dir to save individual image json output***:" + target_dir)

            listOfFiles = os.listdir(file_path)
            print(listOfFiles)

            print("**********File Printing is done************")

            # self.countFiles(self,file_path)

            count = 0

            if not os.path.isdir(target_dir):
                os.mkdir(target_dir)

            for files in listOfFiles:
                count += 1
                print("Individual file :" + files)
                print("Complete file path :" + file_path + "/" + files)

                # print("Rest End point get called ", self.count, "time")

                self.liveness_result_response = self.run(file_path + "/" + files)

                # the json file where the output must be stored
                print("Saving respective Json result for the images are getting save into user's given output path")

                target_path = os.path.join(target_dir, files)

                print("**(file_path***" + target_path)

                self.out_file = open(target_path + ".json", "w")

                json.dump(self.liveness_result_response, self.out_file, indent=6)

        except Exception as ex:
            print("Exception ha been thrown" +ex)
        finally:
            print("release resources")
            # out_file.close()
if __name__ == '__main__':
    print("Please enter I/O folder name")

    selfie_dir = sys.argv[1]
    print("Directory path where all Test data exists :" + selfie_dir)

    result_dir = sys.argv[2]
    print("Directory path where all Json output exists :" + result_dir)

    if len(sys.argv) < 3:
        print
        "You must set argument!!!"
    inhouseds = LivenessInHouse(endpoint)

    inhouseds.listAllSelfie(selfie_dir,result_dir)
    sys.exit()
