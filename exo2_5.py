# 2.5
#
# RECHERCHE D’UN ELEMENT DANS UNE LISTE (BIS)
#
# Ecrire une fonction récursive indiquant si un élément est présent ou non dans une liste. Cette fonction retournera
# un booléen. On fera un test sur le premier élément, puis si besoin est l’appel récursif se fera sur la « fin »
# de la liste.


def recherche_recursive(l, x):
    if l[0] == x:
        return True
    elif len(l) > 1:
        return recherche_recursive(l[1:], x)
    else:
        return False


maListe = [1, 2, 3, 4, 5]
print(recherche_recursive(maListe, 3))
print(recherche_recursive(maListe, 6))
