import json
import os.path
import sys
import time

import requests
from requests.exceptions import HTTPError

hyperverge_host = "https://apac-faceid.hyperverge.co"


def listAllSelfie():
    try:
        file_path = os.path.expanduser('~') + "/" + selfie_dir
        print("***Use current dir to process each images***:" + file_path)
        target_dir = os.path.expanduser('~') + "/" + result_dir
        print("***Use target dir to save individual image json output***:" + target_dir)

        listOfFiles = os.listdir(file_path)
        print(listOfFiles)

        countFiles(file_path)

        count = 0

        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

        for files in listOfFiles:
            count += 1
            print("Individual file :" + files)
            print("Complete file path :" + file_path + "/" + files)

            print("Rest End point get called ", count, "time")

            liveness_result_response = hyperverge_api_result(file_path + "/" + files)

            # the json file where the output must be stored
            print("Saving respective Json result for the images are getting save into user's given output path")

            target_path = os.path.join(target_dir, files)

            print("**(file_path***"+target_path)

            out_file = open(target_path + ".json", "w")

            json.dump(liveness_result_response, out_file, indent=6)

    except Exception as ex:
        print(ex)
    finally:
        print("release resources")
        out_file.close()


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


        files = {"image": (file_path, open(file_path, "rb"), "image/jpg")}

        headers = {"appid": "4baeca",
                   "appkey": "0bf9fad52ecf5692fd46",
                   # "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
                   "transactionId": "abc"}

        url = "https://apac-faceid.hyperverge.co/v2/photo/liveness"

        time.sleep(3)
        liveness_api = requests.post(url, headers=headers, files=files)

        print("***Rest Endpoint Headers :", liveness_api.headers)
        print("***Rest Endpoint URL :", liveness_api.url)
        print("***Rest Endpoint Request :", liveness_api.request)
        print("***Status Code :", liveness_api.status_code)
        print("***Reason :", liveness_api.reason)

       # return liveness_api.json().get("result")

        return  liveness_api.json()
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
    print("Directory path where all Json output exists :" + result_dir)

    if len(sys.argv) < 3:
        print
        "You must set argument!!!"

    listAllSelfie()
    sys.exit()