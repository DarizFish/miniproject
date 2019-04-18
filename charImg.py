from PIL import Image
import argparse


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
input_image = Image.open(r'C:\Users\12104\OneDrive\desktop\sheep.png')
input_image = input_image.resize((180, 60), Image.NEAREST)
def get_char(r, g, b, alpha=256):

    if 0 == alpha:
        return ' '

    length = len(ascii_char)

    gray = int (0.2 * r + 0.7 * g + 0.07 * b)

    unit = (256.0 + 1)/length

    return ascii_char[int(gray/unit)]


def get_charImage(img):

    width, height = img.size
    txt = ''
    for i in range(height):
        for j in range(width):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'
    print(txt)
    return txt

if __name__ == '__main__':
    get_charImage(input_image)