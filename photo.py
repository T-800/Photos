#! /usr/bin/python

from PIL import Image
import os


def Photo_to_matice(path):
    """
        Ouvre l'image et renvoi la matrice des pixels
    """
    im = Image.open(path)
    width, height = im.size
    tab = list(im.getdata())
    return [[tab[x*y] for x in range(width)] for y in range(height)]


def Photo_to_list(path):
    """
        Ouvre l'image et renvoi la liste des pixels
    """
    im = Image.open(path)
    width, height = im.size
    return list(im.getdata())


def min_moy_max_Rouge(liste):
    moy = 0
    mini = 0
    maxi = 0
    for elt in liste:
        moy += elt[0]
        if elt[0] <= mini:
            mini = elt[0]
        if elt[0] > maxi:
            maxi = elt[0]
    return mini, moy//len(liste), maxi


def min_moy_max_Vert(liste):
    moy = 0
    mini = 0
    maxi = 0
    for elt in liste:
        moy += elt[1]
        if elt[1] <= mini:
            mini = elt[1]
        if elt[1] > maxi:
            maxi = elt[1]
    return mini, moy//len(liste), maxi


def min_moy_max_Bleu(liste):
    moy = 0
    mini = 0
    maxi = 0
    for elt in liste:
        moy += elt[2]
        if elt[2] <= mini:
            mini = elt[2]
        if elt[2] > maxi:
            maxi = elt[2]
    return mini, moy//len(liste), maxi

if __name__ == '__main__':
    photos = os.listdir("./Data/")
    for elt in photos:
        if elt.endswith("jpg"):
            print(elt)
            photo = Photo_to_list("./Data/"+elt)
            print("Rouge : "+str(min_moy_max_Rouge(photo)))
            print("Vert : "+str(min_moy_max_Vert(photo)))
            print("Bleu : "+str(min_moy_max_Bleu(photo)))


image = "./Data/Dirge_of_Winter_by_probotech.jpg"
