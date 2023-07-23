import numpy as np

pi = np.pi  # Nombre 3.14159...
RAYON_INTERNE = 1750  # mm
PRESSION_INTERNE = 4.75  # MPa
SIGMA_Y = 300  # contrainte d'écoulement (MPa)


def calcul_paroi_mince_cylindre(epaisseur, pression_interne, rayon_interieur):
    # Paramètres pour "cylindre à paroi mince sous pression interne"
    # epaisseur: épaisseur en mm, à déterminer
    # pression_interne: pression interne MPa
    # rayon_interieur: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    rm = rayon_interieur + epaisseur / 2
    s_y = pression_interne * rayon_interieur ** 2 / (2 * rm * epaisseur)
    s_th = pression_interne * rayon_interieur / epaisseur
    s_r = -0.5 * pression_interne  # contrainte radiale au milieu de l'épaisseur
    s_von_mises_moy = np.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -pression_interne  # contrainte radiale au rayon intérieur de l'épaisseur
    s_von_mises_max = np.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)

    return s_von_mises_moy, s_von_mises_max


def calcul_paroi_mince_sphere(epaisseur, pression_interne, rayon_interieur):
    # Paramètres pour "sphère à paroi mince sous pression interne"
    # epaisseur: épaisseur en mm, à déterminer
    # pression_interne: pression interne MPa
    # rayon_interieur: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    rm = rayon_interieur + epaisseur / 2
    s_y = pression_interne * rayon_interieur ** 2 / (2 * rm * epaisseur)
    s_th = s_y
    s_r = -0.5 * pression_interne  # contrainte radiale au milieu de l'épaisseur
    s_von_mises_moy = np.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -pression_interne  # contrainte radiale au rayon intérieur de l'épaisseur
    s_von_mises_max = np.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)

    return s_von_mises_moy, s_von_mises_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("calcul en cours...")

    dict_sol = []
    for e1 in np.arange(2, 75, 0.1):
        for e2 in np.arange(2, 75, 0.1):
            if e2 < e1:
                von_mises_cylindre = calcul_paroi_mince_cylindre(e1, PRESSION_INTERNE, RAYON_INTERNE)
                von_mises_sphere = calcul_paroi_mince_sphere(e2, PRESSION_INTERNE, RAYON_INTERNE)

                # Respect des critères de conception
                if von_mises_cylindre[0] <= 0.6 * SIGMA_Y and von_mises_sphere[0] <= 0.6 * SIGMA_Y and \
                        von_mises_cylindre[1] <= 0.9 * SIGMA_Y and von_mises_cylindre[1] <= 0.9 * SIGMA_Y:
                    dict_sol.append((e1, e2, von_mises_cylindre, von_mises_sphere))

    # print("solutions: ", dict_sol)
    sol_finale = min(dict_sol, key=lambda e: e[0])

    print("solution optimale qui minimise l'épaisseur (poids de l'eau & accélérations négligés): ")
    print("epaisseur e1 = ", round(sol_finale[0], 2))
    print("epaisseur e2 = ", round(sol_finale[1], 2))
    print("von mises moy cylindre = ", round(sol_finale[2][0], 2))
    print("von mises moy + flex cylindre = ", round(sol_finale[2][1], 2))
    print("von mises moy sphere = ", round(sol_finale[3][0], 2))
    print("von mises moy + flex sphere = ", round(sol_finale[3][1], 2))
