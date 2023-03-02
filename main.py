from math import factorial as fat


# coeficientes k pré-calculados
k = [-1 / fat(3), 1 / fat(5), -1 / fat(7), 1 / fat(9), -1 / fat(11)]


def taylor(x):
    global k

    seno = x * (1 + x**2 * (k[0] + x**2 * (k[1] + x**2 * (k[2] + x**2 * (k[3] + k[4] * x**2)))))

    return seno


def pade():
    pass
