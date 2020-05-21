# -*- coding: utf-8 -*-

import string
import glob
import csv
from PIL import ImageFont, ImageDraw, Image



image_width = 32
image_height = 32

characters = list('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ') # Characters to consider, ignoring symbols
# characters = list(string.ascii_letters) # Characters to consider, ignoring symbols

ttf_files = glob.glob('./google-fonts/*.ttf')           # create the list of file


with open("./csv_dataset/google_fonts_dataset.csv", 'w', newline='') as file:
    writer = csv.writer(file, dialect="excel")
    
    for font_file in ttf_files:
        print(font_file)

        font_name = font_file.split("/")[-1]

        font = ImageFont.truetype(font_file, 32, encoding="unic")

        leftOffset = 0
        image = Image.new('L', (image_width * 32,image_height), "white")
        draw = ImageDraw.Draw(image)

        for character in characters:
            text_width, text_height = draw.textsize(character, font=font)

            offset = font.getoffset(character)
            
            draw.text(
                (((image_width-(text_width+offset[0]))/2) + leftOffset,(image_height-(text_height+offset[1]))/2), 
                character, 
                fill='black', 
                font=font
            )

            leftOffset += image_width
            
        image.save("./font-images/" + font_name + ".0.0.png", "PNG")