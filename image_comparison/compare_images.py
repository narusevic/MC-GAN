# -*- coding: utf-8 -*-
import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

def main():
    fonts = [
        'AlegreyaSansSC-MediumItalic.ttf.0.0',
        'PT_Serif-Web-Regular.ttf.0.0',
        'IBMPlexSerif-Light.ttf.0.0',
        'NotoSerif-Regular.ttf.0.0',
        'OpenSans-BoldItalic.ttf.0.0',
        'FiraSansCondensed-ExtraBold.ttf.0.0',
        'Montserrat-Regular.ttf.0.0',
        'Pattaya-Regular.ttf.0.0'
    ]

    for font_file in fonts:
        print font_file
        # file1, file2 = sys.argv[1:1 + 2] # nuskaityti piešinukų failus
        # Piešinukai nuskaitomi 2D (juodai baltu formatu)
        imgReal = to_grayscale(imread('../results/GlyphNet_pretrain/images_100/' + font_file + '_real_B.png').astype(float))
        img100 = to_grayscale(imread('../results/GlyphNet_pretrain/images_100/' + font_file + '_fake_B.png').astype(float))
        img200 = to_grayscale(imread('../results/GlyphNet_pretrain/images_200/' + font_file + '_fake_B.png').astype(float))
        img300 = to_grayscale(imread('../results/GlyphNet_pretrain/images_300/' + font_file + '_fake_B.png').astype(float))
        img400 = to_grayscale(imread('../results/GlyphNet_pretrain/images_400/' + font_file + '_fake_B.png').astype(float))
        n_m_100, n_0_100 = compare_images(imgReal, img100) # vykdomas palyginimas
        n_m_200, n_0_200 = compare_images(imgReal, img200) # vykdomas palyginimas
        n_m_300, n_0_300 = compare_images(imgReal, img300) # vykdomas palyginimas
        n_m_400, n_0_400 = compare_images(imgReal, img400) # vykdomas palyginimas
        print '<p>', str(round(n_m_100 * 100 / 255 / imgReal.size, 2)), '</p><p>', str(round(100 - (n_0_100 * 100.0 / imgReal.size), 2)), '</p>'
        print '<p>', str(round(n_m_200 * 100 / 255 / imgReal.size, 2)), '</p><p>', str(round(100 - (n_0_200 * 100.0 / imgReal.size), 2)), '</p>'
        print '<p>', str(round(n_m_300 * 100 / 255 / imgReal.size, 2)), '</p><p>', str(round(100 - (n_0_300 * 100.0 / imgReal.size), 2)), '</p>'
        print '<p>', str(round(n_m_400 * 100 / 255 / imgReal.size, 2)), '</p><p>', str(round(100 - (n_0_400 * 100.0 / imgReal.size), 2)), '</p>'
        print ''

def compare_images(img1, img2):
    diff = img1 - img2  # masyvų skirtumas
    m_norm = sum(abs(diff))  # Manhattan normalizacija
    z_norm = norm(diff.ravel(), 0)  # Nulinė normalizacija
    print img1
    print diff
    print m_norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    # Jeigu piešinukas yra spalvotas (3D masyvas), konvertuoti į juodai baltą (2D masyvas)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # paimti paskutinio spalvos kanalą
    else:
        return arr

if __name__ == "__main__":
    main()

