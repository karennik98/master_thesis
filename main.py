import cv2 as cv
import os
import numpy
from PIL import ImageFont, ImageDraw, Image

out_folder_path = 'output_png/'
font_path = "FreeMono-Regular-8975.ttf"
file_path="Armenian.unicharset.txt"

def get_symbol_list(doc_path):
    with open(doc_path) as f:
        symbols = f.readline()
    return symbols

def create_blank(width, height, rgb_color=(0, 0, 0)):
    image = numpy.zeros((height, width, 3), numpy.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image

def pass_to_the_tesseract():
    pass

if __name__ == '__main__':
    symbol_size = 20
    width, height = 50, 50
    white = (255, 255, 255)
    b, g, r, a = 0, 0, 0, 0
    symbols = get_symbol_list(file_path)
    # Iterate over the string
    withe_image = numpy.ones((100, 100, 1), numpy.uint8) * 255
    cv.imwrite("test.jpg", withe_image)
    for i, v in enumerate(str(symbols)):
        v.replace('\n', '')
        os.mkdir(out_folder_path + v)
        img = create_blank(width, height, rgb_color=white)
        font = ImageFont.truetype(font_path, symbol_size)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((20, 8), v, font=font, fill=(b, g, r, a))
        img = numpy.array(img_pil)
        cv.imwrite(out_folder_path + v + '/'+ v +".png", img)
        file = open(out_folder_path + v + '/' + v + ".txt", "w")
        file.write(v)
        file.close()

    pass_to_the_tesseract()