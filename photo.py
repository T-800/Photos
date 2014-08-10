#! /usr/bin/python

from PIL import Image
import os


def Photo_to_list(path):
    """
        Ouvre l'image et renvoi la liste des pixels
    """
    im = Image.open(path)
    width, height = im.size
    return list(im.getdata())


def moyenne_RGB(liste):
    moyenne = [0]*3
    for elt in liste:
        moyenne[0] += int(elt[0])
        moyenne[1] += int(elt[1])
        moyenne[2] += int(elt[2])

    return [x//len(liste) for x in moyenne]


def nombre_boules(liste):

    P = moyenne_RGB(liste)
    TEINTE = 0
    MAX = max(P)
    MIN = min(P)
    C = MAX - MIN

    if MAX == MIN:
        TEINTE += 360
    elif P[0] == MAX:  # ROUGE
        A = P[1] - P[2]  # VERT - BLEU
        TEINTE = ((60 * (A/C))) % 360
    elif P[1] == MAX:  # VERT
        A = P[2] - P[0]  # BLEU - ROUGE
        TEINTE = (60 * (A/C) + 120)
    elif P[2] == MAX:  # BLEUa
        A = P[0] - P[1]  # ROUGE - VERT
        TEINTE = (60 * (A/C) + 240)

    TEINTE = round(TEINTE)
    print("° : "+str(TEINTE))

    T = abs(TEINTE - 240)
    print("DIFF° : "+str(T))
    T = round(T // 18)
    print("DIFF : "+str(T))
    BOULE = 20 - T
    print("Boule :"+str(BOULE))


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
