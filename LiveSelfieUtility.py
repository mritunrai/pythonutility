import random
import string
import sys

import requests
import os.path
import json
from requests.exceptions import Timeout, HTTPError

from time import sleep

hyperverge_host = "https://apac-faceid.hyperverge.co"


def listAllSelfie():
    try:
        file_path = os.path.expanduser('~') + "/" + selfie_dir
        print("User current dir" + file_path)
        result = os.path.expanduser('~') + "/" + result_dir
        listOfFiles = os.listdir(file_path)
        print(listOfFiles)
        file_count = countFiles(file_path)

        count = 0

        for files in listOfFiles:
            count += 1
            print("Individual file :" + files)
            print("Complete file path :" + file_path + "/" + files)

            print("Rest End point get called ", count, "time")

            liveness_result_response = hyperverge_api_result(file_path + "/" + files)

            # the json file where the output must be stored
            out_file = open(files + ".json", "w")

            json.dump(liveness_result_response, out_file, indent=6)

    except Exception as ex:
        print(ex)
    finally:
        print("release resources")
        # out_file.close()


def countFiles(file_path):
    totalFiles = 0
    totalDir = 0

    for base, dirs, files in os.walk(file_path):
        print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    print('Total number of files', totalFiles)
    print('Total Number of directories', totalDir)
    print('Total:', (totalDir + totalFiles))

    return totalFiles


def hyperverge_api_result(file_path):
    try:
        # files = {'file': open(file_path, 'rb')}
        # files = {
        #     'image': (file_path, open(file_path, 'rb'), 'image/jpg'),
        # }

        files = {"image": (file_path, open(file_path, "rb"), "image/jpg")}

        headers = {"appid": "4baeca",
                   "appkey": "0bf9fad52ecf5692fd46",
                   # "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
                   "transactionId": "abc"}

        url = "https://apac-faceid.hyperverge.co/v2/photo/liveness"

        # liveness_api = requests.post("{}{}".format(hyperverge_host, "/v2/photo/liveness"),
        #                              headers={"appid": "4baeca",
        #                                       "appkey": "0bf9fad52ecf5692fd46",
        #                                       "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
        #                                       "transactionId": "abc"},
        #                              files=my_img)


        liveness_api = requests.post(url, headers=headers, files=files)

        print(" Rest Endpoint Headers :", liveness_api.headers)
        print("Rest Endpoint URL :", liveness_api.url)
        print("Rest Endpoint Request :", liveness_api.request)
        print("Status Code :", liveness_api.status_code)
        print("Reason :", liveness_api.reason)

        return liveness_api.json().get("result")
    except HTTPError as ex:
        print(ex)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    print("Please enter I/O folder name")

    selfie_dir = sys.argv[1]
    print("Directory path where all Test data exists :" + selfie_dir)

    result_dir = sys.argv[2]
    print("Directory path where all Test data exists :" + selfie_dir)

    listAllSelfie()
    sys.exit()
