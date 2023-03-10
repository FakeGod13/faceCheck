import tkinter as tk
from camera import tkImage, getImagePath, cameraShutter
from faceCheck import imageToBase64, faceCheck
from threading import Thread

""" root窗口 """

# 窗口参数
window_width = 640
window_height = 480


# 画布参数
image_width = int(window_width*0.6)
image_height = int(window_height*0.6)
image_pos_x = int(window_width*0.2)
image_pos_y = int(window_height*0.1)


""" 按钮 """

# 按钮位置
button_pos_x = 250
button_pos_y = 350

""" 信息栏 """

# 参数
label_pos_x = 250
label_pos_y = 350 + 75



# 回调函数

def callback_saveImage():
    path = cameraShutter()
    # 测试faceCheck
    isTrue = faceCheck(imageToBase64(path))
    print(isTrue)
    if isTrue:
        label_text.set('检测到学生正在学习')
    else:
        label_text.set('未检测到学生')


""" 并行 """

# 定时器
def timer():
    while(True):
        callback_saveImage()
        from time import sleep
        sleep(10)


# 视频更新器
def updater():
    while (True):
        picture = tkImage(image_width, image_height)
        canvas.create_image(0, 0, anchor='nw', image=picture)
        root.update()
        # root.after(10)
        from time import sleep
        sleep(1)
        callback_saveImage()

# 线程
t1 = Thread(target=timer, args=('第1个线程 定时器', 1))
t2 = Thread(target=updater, args=('第2个线程 视频更新器', 2))


if __name__ == "__main__":

    """根窗口"""

    root = tk.Tk()
    root.wm_title("face recognition")
    root.geometry(str(window_width)+'x'+str(window_height))

    """摄像头"""

    # 画布声明
    canvas = tk.Canvas(root, bg='white', width=image_width,
                       height=image_height)
    # 画布放置
    canvas.place(x=image_pos_x, y=image_pos_y)

    """ 按钮 """

    # 按钮声明
    button = tk.Button(root, text='保存图片', width=15,
                       height=2, command=callback_saveImage)
    # 按钮放置
    button.place(x=button_pos_x, y=button_pos_y)

    """ 信息栏 """
    # 文本信息
    label_text = tk.StringVar()

    label = tk.Label(root, textvariable=label_text)
    label.place(x=label_pos_x, y=label_pos_y)

    # 死循环更新画布上的图像
    updater()

    root.mainloop()
