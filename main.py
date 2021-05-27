import cv2 as cv
import os
import numpy
from PIL import ImageFont, ImageDraw, Image
import argparse
import subprocess

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

def pass_to_the_tesseract(all_path):
    os.environ["TESSDATA_PREFIX"] = "./"
    output=str()
    for path_pair in all_path:
        # tesseract Ա.png output --oem 1 --psm 10 -l hye
        bash_cmd = ["tesseract", path_pair[0], output, "--oem", "1", "--psm", "10", "-l", "hye"]
        process = subprocess.Popen(bash_cmd, stdout=subprocess.PIPE)
        # output, error = process.communicate()
        print(output)

def parse_args():
    parser = argparse.ArgumentParser(description='Get image width and height.')
    parser.add_argument('--w', default=100, help='width of created image (default: find the 100)')
    parser.add_argument('--h', default=100, help='height of created image (default: find the 100)')

    args = parser.parse_args()
    return args.w, args.h

if __name__ == '__main__':
    args = parse_args()
    width = int(args[0])
    height = int(args[1])
    symbol_size = int(width/2)
    white = (255, 255, 255)
    b, g, r, a = 0, 0, 0, 0
    symbols = get_symbol_list(file_path)
    # Iterate over the string
    out_folder_path = 'input_png' + '_' + str(width) + '_' + str(height) + '/'
    if not os.path.exists(out_folder_path):
        os.mkdir(out_folder_path)
    all_path = list()
    for i, v in enumerate(str(symbols)):
        v.replace('\n', '')
        if not os.path.exists(out_folder_path + v):
            os.mkdir(out_folder_path + v)
        img = create_blank(width, height, rgb_color=white)
        font = ImageFont.truetype(font_path, symbol_size)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((((width - symbol_size)/2, (height-symbol_size)/2)), v, font=font, fill=(b, g, r, a))
        img = numpy.array(img_pil)
        image = out_folder_path + v + '/'+ v +".png"
        text = out_folder_path + v + '/' + v + ".txt"
        cv.imwrite(image, img)
        file = open(text, "w")
        all_path.append((image, text))
        file.write(v)
        file.close()

    pass_to_the_tesseract(all_path)