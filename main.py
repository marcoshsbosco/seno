from math import factorial as fat
from math import pi
from math import sin
from time import time
import matplotlib.pyplot as plt


# coeficientes k pré-calculados
k = [-0.16666666666666666, 0.008333333333333333, -0.0001984126984126984,
     2.7557319223985893e-06, -2.505210838544172e-08]


def taylor(x):
    global k

    t0 = time()

    x2 = x**2
    seno = x * (1 + x2 * (k[0] + x2 * (k[1] +
                x2 * (k[2] + x2 * (k[3] + k[4] * x2)))))

    t1 = time()

    return (seno, t1 - t0)


def pade(x):
    t0 = time()

    seno = (0 + 1*x + 0*x**2 + (1/72 - 1/fat(3))*x**3 + (0 + 0)*x**4 + ((1/72) *
            (-1/fat(3)))*x**5 + ((1/72) * (1/fat(5)) + (-1/fat(7)))*x**7) / (1 + (1/72)*x**2)

    t1 = time()

    return (seno, t1 - t0)


def pade_reduzido(x):
    t0 = time()

    fatorial = [0]*8
    fatorial[0] = 1
    fatorial[1] = fatorial[0]*1
    fatorial[2] = fatorial[1]*2
    fatorial[3] = fatorial[2]*3
    fatorial[4] = fatorial[3]*4
    fatorial[5] = fatorial[4]*5
    fatorial[6] = fatorial[5]*6
    fatorial[7] = fatorial[6]*7

    x2 = x**2
    x3 = x * x2
    x5 = x3 * x2
    x7 = x5 * x2

    um_setentadois_avos = 1/72
    um_sobre_fatorial_tres = 1/fatorial[3]
    um_sobre_fatorial_cinco = 1/fatorial[5]
    um_sobre_fatorial_sete = 1/fatorial[7]

    termo1 = x
    termo2 = (um_setentadois_avos - um_sobre_fatorial_tres) * x3
    termo3 = (um_setentadois_avos * (-um_sobre_fatorial_tres)) * x5
    termo4 = (um_setentadois_avos * um_sobre_fatorial_cinco)
    termo5 = (-um_sobre_fatorial_sete) * x7

    denominador = 1 + um_setentadois_avos * x2
    numerador = termo1 + termo2 + termo3 + termo4 + termo5
    seno = numerador / denominador

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

    pade_res_t = pade_reduzido(x)

    real = sin(x)

    dados["x"].append(x)

    dados["pade"]["e"].append(abs(real - pade_res[0]))
    dados["taylor"]["e"].append(abs(real - taylor_res[0]))

    dados["taylor"]["t"].append(taylor_res[1])
    dados["pade"]["t"].append(pade_res[1])

    x += 0.1

grafico_tempo(dados)
grafico_erro(dados)
