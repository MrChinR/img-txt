#-*- coding = utf-8 -*-
#@Time : 2020/10/28 15:31
#@Author : Chin
#@File : img_txt_transport.py
#@Software : PyCharm


#  为一张图片生成对应的字符集图片

from PIL import Image




ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    a = input("输入您要转换的图片路径：")
    chang = int(input("输入图片的长："))
    kuan = int(input("输入图片的宽："))
    im = Image.open(r'%s'%a)
    im = im.resize((kuan, chang), Image.NEAREST)

    txt = ""

    for i in range(chang):
        for j in range(kuan):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    with open("output.txt", 'w') as f:
        f.write(txt)