import requests
import base64
from pprint import pprint
import os

# URL
base_url = "https://aip.baidubce.com/"

# 密钥
ak = 'N4ha9M5RmPCLOdO92K8rOwlK'
sk = 'B4a98YyIq68b4FEAVwc6XS4LVn10qQaO'

# 从百度智能云API获取token
def access_taken(ak, sk):
    url = base_url + 'oauth/2.0/token?grant_type=client_credentials&client_id=' + \
        ak + '&client_secret=' + sk
    response = requests.get(url)
    token = response.json()['access_token']
    return token


def imageToBase64(path):
    with open(path, mode='rb') as f:
        code = base64.b64encode(f.read())
    return code


def faceCheck(code):
    try:
        params = {
            'image': code,
            'image_type': 'BASE64',
            'answer': 'beauty',
        }

        request_url = base_url + "rest/2.0/face/v3/detect" + "?access_token=" + access_taken(ak, sk)
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)

        face_num = response.json()['result']['face_num']  # 取出返回数据中人脸数
        # pprint(response.json())
        if face_num>=1:
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    print("this faceCheck")
