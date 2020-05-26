# -*- coding: utf-8 -*-
import string
import glob
import csv
from PIL import ImageFont, ImageDraw, Image

image_width = 32 # raidės plotis - pikselių skaičius
image_height = 32 # raidės aukštis - pikselių skaičius
characters = list('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ') # raidės, sudarančios lietuvišką abėcėlę
ttf_files = glob.glob('./google-fonts/*.ttf') # nuskaitomi šrifto failai

for font_file in ttf_files: # iteruojama per kiekvieną nuskaitomą failą
    font_name = font_file.split("/")[-1] # nuskaitomas šrifto vardas
    font = ImageFont.truetype(font_file, 32, encoding="unic") # nuskaitytas šrifto failas perverčiamas į truetype tipą
    leftOffset = 0 # atstumas nuo piešinuko pradžios
    image = Image.new('L', (image_width * 32,image_height), "white") # sukuriamas piešinukas
    draw = ImageDraw.Draw(image) # Sukuriamas piešimo srautas
    for character in characters: # iteruojama per kiekvieną lietuviškos abėcėlės raidę
        text_width, text_height = draw.textsize(character, font=font) # gaunamas sukurtos raidės plotis ir aukštis pikseliais 
        offset = font.getoffset(character) # suskaičiuojamas atstumas nuo raidės krašto
        draw.text(
            (((image_width-(text_width+offset[0]))/2) + leftOffset,(image_height-(text_height+offset[1]))/2), 
            character, 
            fill='black', 
            font=font
        ) # raidė nupiešiama, pagal nuskaitytą dydį, atstumą nuo piešinuko pradžios, raidės atstumą nuo krašto
        leftOffset += image_width # padidinamas atstumas nuo piešinuko krašto kitai raidei
    image.save("./font-images/" + font_name + ".0.0.png", "PNG") # išsaugojamas piešinukas


    