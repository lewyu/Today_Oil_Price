import requests
import time
import numpy as np
from captcha.image import ImageCaptcha  # 验证码库
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract  # 验证码识别库
import random

# 配置验证码文本
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           '', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
vcode_size = 4


# 生成验证码文本
def get_vcode_text(char_set=mumbers, size=vcode_size):  # char_set为候选集，vcode_size为验证码长度
    vcode_text = []
    for i in range(size):
        char = random.choice(char_set)
        vcode_text.append(char)
    return vcode_text


# 生成验证码图片
def get_vcode_image():
    image = ImageCaptcha()
    vcodetext = get_vcode_text()
    vcodetext = ''.join(vcodetext)

    images = image.generate(vcodetext)
    images = Image.open(images)
    images = np.array(images)
    return vcodetext, images


# 测试显示验证码图片
def get_vcode_show():
    # show the vcode image
    text, image = get_vcode_image()
    print("验证码：", text)
    box = plt.figure()
    ax = box.add_subplot(111)
    ax.text(0.1, 0.9, text)
    plt.imshow(image)
    plt.show()


# 验证码识别
def de_vcode():
    imageObject = Image.open('img/showvcode.png')  # 测试图片存放路径
    print(imageObject)
    # https://blog.csdn.net/qq_42184699/article/details/92575404  to solve err
    # You need to install Tesseract-OCR && configure the EXE file path firstly
    print(pytesseract.image_to_string(imageObject))


# 其他功能展示
def get_message(url):
    """获取金山词霸每日励志精句"""
    r = requests.get(url)
    note = r.json()['note']
    content = r.json()['content']
    return note, content


if __name__ == "__main__":
    myurl = "http://open.iciba.com/dsapi/"
    print(get_message(myurl), time.ctime())

    get_vcode_show()
    de_vcode()
