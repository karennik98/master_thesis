import cv2 as cv
import numpy
from PIL import ImageFont, ImageDraw, Image

out_folder_path = 'outputimages/'
font_path = "FreeMono-Regular-8975.ttf"
file_path="Armenian.unicharset.txt"

def get_symbol_list(doc_path):
    with open(doc_path) as f:
        symbols = f.readlines()
    return symbols

def create_blank(width, height, rgb_color=(0, 0, 0)):
    image = numpy.zeros((height, width, 3), numpy.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image

if __name__ == '__main__':
    symbols = get_symbol_list(file_path)
    withe_image = numpy.ones((100, 100, 1), numpy.uint8) * 255
    cv.imwrite("test.jpg", withe_image)
    for el in symbols:
        width, height = 50, 50
        white = (255, 255, 255)
        img = create_blank(width, height, rgb_color=white)
        b, g, r, a = 0, 0, 0, 0
        font = ImageFont.truetype(font_path, 20)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((width/2, height/2), el, font=font, fill=(b, g, r, a))
        img = numpy.array(img_pil)
        cv.imwrite(out_folder_path + el +".png", img)