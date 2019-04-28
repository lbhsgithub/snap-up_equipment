from PIL import Image
from pytesseract import *


def binarize():
    code_savepath = './code.jpeg'
    img = Image.open(code_savepath)
    # image process
    # traverse every pixel
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            # content
            # get value
            data = (img.getpixel((i, j)))
            # binarized by 140
            if sum(data[0:3])/3 >= 140:  # a simple way, or each value > 140
                img.putpixel((i, j), (255, 255, 255, 255))
            else:
                img.putpixel((i, j), (0, 0, 0, 0))
    # just one statement to identify
    return image_to_string(img, lang='eng', config='-psm 10')


if __name__ == "__main__":
    print(binarize)
