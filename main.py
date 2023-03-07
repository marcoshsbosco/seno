from math import factorial as fat
from math import pi
from math import sin
from time import time
import matplotlib.pyplot as plt


# coeficientes k pré-calculados
k = [-0.16666666666666666, 0.008333333333333333, -0.0001984126984126984,
     2.7557319223985893e-06, -2.505210838544172e-08]

um_setentadois_avos = 1/72  # pré-calculado para padé


def taylor(x):
    global k

    t0 = time()

    x2 = x**2

    seno = x * (1 + x2 * (k[0] + x2 * (k[1] +
                x2 * (k[2] + x2 * (k[3] + k[4] * x2)))))

    t1 = time()

    return (seno, t1 - t0)


def pade(x):
    global um_setentadois_avos

    t0 = time()

    x2 = x ** 2
    x3 = x * x2
    x5 = x3 * x2
    x7 = x5 * x2

    seno = (x + ((um_setentadois_avos + k[0]) * x3) + ((um_setentadois_avos * k[0]) * x5) + (um_setentadois_avos * k[1]) + (k[2] * x7)) / (1 + um_setentadois_avos * x2)

    t1 = time()

    return (seno, t1 - t0)


def grafico_tempo(dados):
    fig, ax = plt.subplots()

    ax.set_xlabel("x")
    ax.set_ylabel("tempo (s)")

    ax.plot(dados["x"], dados["taylor"]["t"], 'b', label="taylor")
    ax.plot(dados["x"], dados["pade"]["t"], 'r', label="pade")

    ax.legend()

    fig.savefig('tempo.png')


def grafico_erro(dados):
    fig, ax = plt.subplots()

    ax.set_xlabel("x")
    ax.set_ylabel("erro")

    plt.yscale('symlog', linthresh=10e-18)

    ax.plot(dados["x"], dados["taylor"]["e"], 'b', label="taylor")
    ax.plot(dados["x"], dados["pade"]["e"], 'r', label="pade")

    ax.legend()

    fig.savefig('erro.png')


dados = {"x": [], "taylor": {"t": [], "e": []}, "pade": {"t": [], "e": []}}

x = -pi/4
while x <= pi/4:
    pade_res = pade(x)
    taylor_res = taylor(x)

    real = sin(x)

    dados["x"].append(x)

    dados["pade"]["e"].append(abs(real - pade_res[0]))
    dados["taylor"]["e"].append(abs(real - taylor_res[0]))

    dados["taylor"]["t"].append(taylor_res[1])
    dados["pade"]["t"].append(pade_res[1])

    x += 0.1

grafico_tempo(dados)
grafico_erro(dados)
