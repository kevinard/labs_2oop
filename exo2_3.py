# 2.3
#
# RECHERCHE D’UN ELEMENT DANS UNE LISTE
#
# Ecrire une fonction indiquant si un élément est présent ou non dans une liste. S’il est présent cette fonction
# retournera l’indice de la case où il se trouve pour la première fois, et s’il est absent elle retournera -1.


def recherche(l, x):
    if x in l:
        for i in l:
            if l[i] == x:
                return i
    else:
        return -1


maListe = [1, 2, 3, 4, 5]
print(recherche(maListe, 3))
print(recherche(maListe, 6))
