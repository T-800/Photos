#! /usr/bin/python

from PIL import Image


def Photo_to_matice(path):
    """
        Ouvre l'image et renvoi la matrice des pixels
    """
    im = Image.open(path)
    width, height = im.size
    tab = list(im.getdata())
    return [[tab[x*y] for x in range(width)] for y in range(height)]


image = "/media/data/git/Photos/Data/Capture.PNG"
photo = Photo_to_matice(image)
print(photo)
