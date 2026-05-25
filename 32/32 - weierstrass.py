import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


def show_seq(x, y):

    fig, ax = plt.subplots()
    ax.grid(visible=True, which="both", axis="both")
    ax.scatter(x, y)
    fig.set_dpi(200)
    # fig.set_size_inches(1,1)

    # ax.set_aspect("equal")
    # ax.minorticks_on()
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    plt.show()


def rec_sequence(u0, f, nb):
    l = [u0]
    for i in range(0, nb - 1):
        l.append(f(l[-1]))
    print(l)
    return l


n = 10

a = np.array([(i, math.sqrt(i)) for i in range(0, n)])
e1 = list(map(lambda x: x[0], a))
e2 = list(map(lambda x: x[1], a))


r1 = rec_sequence(-4, lambda x: 1 + x / 2, n)

r2 = rec_sequence(10, lambda x: (-2 / 3) * x, n)

show_seq(e1, r1)
show_seq(e1, r2)
