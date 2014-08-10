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
        moy += int(elt[0])
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


def nombre_boules(liste):
    """
    """
    TEINTE = []
    for elt in liste:
        MAX = max(elt)
        MIN = min(elt)
        C = MAX - MIN

        if MAX == MIN:
            TEINTE += [0]
        elif elt[0] == MAX:  # ROUGE
            A = elt[1] - elt[2]  # VERT - BLEU
            TEINTE += [((60 * (A/C))) % 360]
        elif elt[1] == MAX:  # VERT
            A = elt[2] - elt[0]  # BLEU - ROUGE
            TEINTE += [(60 * (A/C) + 120)]
        elif elt[2] == MAX:  # BLEUa
            A = elt[0] - elt[1]  # ROUGE - VERT
            TEINTE += [(60 * (A/C) + 240)]

    TEINTE_MOYENNE = sum(TEINTE)//len(TEINTE)

    print("° : "+str(TEINTE_MOYENNE))


if __name__ == '__main__':

    dossier = "/media/nas/Multimedia/Image/Images/"
    dossier0 = "./Data/"
    photos = os.listdir(dossier0)
    for elt in photos:
        if elt.endswith("jpg") or elt.endswith("JPG") or elt.endswith("jpeg"):
            print(elt)
            photo = Photo_to_list(dossier0+elt)
            nombre_boules(photo)
            print(" ")
