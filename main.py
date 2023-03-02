from math import factorial as fat


# coeficientes k pré-calculados
k = [-0.16666666666666666, 0.008333333333333333, -0.0001984126984126984, 2.7557319223985893e-06, -2.505210838544172e-08]


def taylor(x):
    global k

    seno = x * (1 + x**2 * (k[0] + x**2 * (k[1] + x**2 * (k[2] + x**2 * (k[3] + k[4] * x**2)))))

    return seno


def pade():
    pass
