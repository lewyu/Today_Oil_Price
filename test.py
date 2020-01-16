import requests
import time
import numpy as np
from captcha.image import ImageCaptcha  # 验证码库
import matplotlib.pyplot as plt
from PIL import Image
import random

# 生成验证码文本
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           '', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def get_vcode_text(char_set=mumbers, size=4):  # char_set为候选集，size为验证码长度
    vcode_text = []
    for i in range(size):
        char = random.choice(char_set)
        vcode_text.append(char)
    return vcode_text


# 生成验证码
def get_vcode_image():
    image = ImageCaptcha()
    vcodetext = get_vcode_text()
    vcodetext = ''.join(vcodetext)

    images = image.generate(vcodetext)
    images = Image.open(images)
    images = np.array(images)
    return vcodetext, images


def get_text(url):
    """获取金山词霸每日励志精句"""
    r = requests.get(url)
    note = r.json()['note']
    content = r.json()['content']
    return note, content


def get_vcode_show():
    # show the vcode image
    text, image = get_vcode_image()
    print("验证码：", text)
    box = plt.figure()
    ax = box.add_subplot(111)
    ax.text(0.1, 0.9, text)
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    myurl = "http://open.iciba.com/dsapi/"
    print(get_text(myurl), time.ctime())

    get_vcode_show()
