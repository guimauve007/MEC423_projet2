import numpy as py

pi = py.pi  # Nombre 3.14159...


def calcul_paroi_mince_cylindre(e1, pression_interne, rayon_interieur):
    # Paramètres pour "cylindre à paroi mince sous pression interne"
    # e1: épaisseur en mm, à déterminer
    # p: pression interne MPa
    # R: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    rm = rayon_interieur + e1 / 2
    s_y = pression_interne * rayon_interieur ** 2 / (2 * rm * e1)
    s_th = pression_interne * rayon_interieur / e1
    s_r = -0.5 * pression_interne  # contrainte radiale au milieu de l'épaisseur
    s_von_mises_moy = py.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -pression_interne  # contrainte radiale au rayon intérieur de l'épaisseur
    s_von_mises_max = py.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)

    return s_von_mises_moy, s_von_mises_max


def calcul_paroi_mince_sphere(e2, pression_interne, rayon_interieur):
    # Paramètres pour "sphère à paroi mince sous pression interne"
    # e2: épaisseur en mm, à déterminer
    # p: pression interne MPa
    # R: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    rm = rayon_interieur + e2 / 2
    s_y = pression_interne * rayon_interieur ** 2 / (2 * rm * e2)
    s_th = s_y
    s_r = -0.5 * pression_interne  # contrainte radiale au milieu de l'épaisseur
    s_von_mises_moy = py.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -pression_interne  # contrainte radiale au rayon intérieur de l'épaisseur
    s_von_mises_max = py.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)

    return s_von_mises_moy, s_von_mises_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("cylindre:")
    print(calcul_paroi_mince_cylindre(55, 6, 1850))
    print("sphere:")
    print(calcul_paroi_mince_sphere(30, 6, 1850))
