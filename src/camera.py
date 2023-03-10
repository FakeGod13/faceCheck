import cv2 as cv
from PIL import Image, ImageTk

""" 相机 """

# 照片路径
def getImagePath():

    from time import strftime, localtime
    time_str = strftime("%Y-%m-%d-%Hhh-%Mmm-%Sss", localtime())
    path = r"img/" + time_str + ".jpg"

    return path

# 摄像机
capture = cv.VideoCapture(0) # 相机编号 默认为0

def closeCamera():
    capture.release()


def tkImage(width, height):
    ref, frame = capture.read()
    cv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cv_image)
    pilImage = pilImage.resize((width, height), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage

def cameraShutter():
    ref, frame = capture.read()
    # 相片存放路径
    path = getImagePath()
    cv.imwrite(path, frame)
    return path
