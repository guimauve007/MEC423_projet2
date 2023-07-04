import numpy as py
from numpy.linalg import solve
import matplotlib.pyplot as plt
import matplotlib.tri as tri

pi = py.pi # Nombre 3.14159...

def calculParoiMinceCylindre(e1, p, R):
    # Paramètres pour "cylindre à paroi mince sous pression interne"
    #e1:100 épaisseur en mm, à déterminer
    #p: pression interne MPa
    #R: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    Rm = R+e1/2
    s_y = p*R**2/(2*Rm*e1)
    s_th = p*R/e1
    s_r = -0.5*p # contrainte radiale au milieu de l'épaisseur
    s_VonMises_moy = py.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)
    print("Von Mises Moyen: ", round(s_VonMises_moy, 2))

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -p # contrainte radiale au rayon intérieur de l'épaisseur
    s_VonMises_max = py.sqrt(s_y**2+s_th**2+s_r**2-s_y*s_th-s_th*s_r-s_r*s_y)
    print("Von Mises Max  : ", round(s_VonMises_max, 2))

def calculParoiMinceSphere(e2, p, R):
    # Paramètres pour "sphère à paroi mince sous pression interne"
    #e2: épaisseur en mm, à déterminer
    #p: pression interne MPa
    #R: rayon intérieur mm

    # Calcul de Contrainte Von-Mises moyenne dans la paroi
    Rm = R + e2 / 2
    s_y = p * R ** 2 / (2 * Rm * e2)
    s_th = s_y
    s_r = -0.5 * p  # contrainte radiale au milieu de l'épaisseur
    s_VonMises_moy = py.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)
    print("Von Mises Moyen: ", round(s_VonMises_moy, 2))

    # Calcul de Contrainte Von-Mises moyenne+flexion max dans la paroi
    s_r = -p  # contrainte radiale au rayon intérieur de l'épaisseur
    s_VonMises_max = py.sqrt(s_y ** 2 + s_th ** 2 + s_r ** 2 - s_y * s_th - s_th * s_r - s_r * s_y)
    print("Von Mises Max  : ", round(s_VonMises_max, 2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("cylindre:")
    calculParoiMinceCylindre(55, 6, 1850)
    print("sphere:")
    calculParoiMinceSphere(30, 6, 1850)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
