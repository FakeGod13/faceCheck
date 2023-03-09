import requests
import base64
import os


ak = 'N4ha9M5RmPCLOdO92K8rOwlK'
sk = 'B4a98YyIq68b4FEAVwc6XS4LVn10qQaO'


def access_taken(ak, sk):
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
        ak + '&client_secret=' + sk
    response = requests.get(url)
    return response.json()['access_token']


token = access_taken(ak, sk)


def appearance(file_path, token):
    url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token={taken}'
    with open(file_path, mode='rb') as f:
        data = base64.b64encode(f.read())

    params = {
        'picture': data,
        'picture_type': 'BASE64',
        'answer': 'people',
    }

    response = requests.post(url, data=params)
    people = response.json()['result']['face_num']

    return people


if __name__ == "__main__":

    img = './img'
    appearance(img, token)
    path = './img'
    # 储存照片的文件夹地址
    img_list = os.listdir(path)
