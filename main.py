from math import factorial as fat
from math import pi
from math import sin
from time import time


# coeficientes k pré-calculados
k = [-0.16666666666666666, 0.008333333333333333, -0.0001984126984126984, 2.7557319223985893e-06, -2.505210838544172e-08]


def taylor(x):
    global k

    t0 = time()

    seno = x * (1 + x**2 * (k[0] + x**2 * (k[1] + x**2 * (k[2] + x**2 * (k[3] + k[4] * x**2)))))

    t1 = time()

    print(f"tempo taylor: {t1 - t0} s")

    return seno


def pade(x):
    t0 = time()

    seno = (0 + 1*x + 0*x**2 + (1/72 - 1/fat(3))*x**3 + (0 + 0)*x**4 + ((1/72) * (-1/fat(3)))*x**5 + ((1/72) * (1/fat(5)) + (-1/fat(7)))*x**7) / (1 + (1/72)*x**2)

    t1 = time()

    print(f"tempo pade: {t1 - t0} ")

    return seno

x = -pi/4
while x <= pi/4:
    # print(f"pade = {pade(x)}, taylor = {taylor(x)}, real = {sin(x)}")
    print(f"sin({x}): taylor errou por {sin(x) - taylor(x)}, pade por {pade(x) - sin(x)}")

    x += 0.1
