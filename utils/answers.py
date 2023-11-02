import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from utils import constants as C

###########################################
#### Session 1
###########################################

def v0_components_1(v0, theta):
    # theta in radians
    vx0 = np.cos(theta) * v0
    vy0 = np.sin(theta) * v0

    return vx0, vy0


def position_x_1(t, vx0, x0):
    return x0 + vx0 * t


def position_y_1(t, vy0, y0):
    return y0 + vy0 * t - 0.5 * C.G0 * (t ** 2)


def t_star_1(vy0):
    return 2 * vy0 / C.G0


def sdot_1(s):
    xdot = s[2]
    ydot = s[3]
    xddot = 0
    yddot = -C.G0

    sdot = np.array([xdot, ydot, xddot, yddot])
    return sdot


def calc_e_1(theta, v0, dstar):
    return (v0 ** 2) * np.sin(2 * theta) / C.G0 - dstar


def calc_eprime_1(theta, v0, dstar):
    return 2 * (v0 ** 2) * np.cos(2 * theta) / C.G0


def calc_newton_iter_1(theta, v0, dstar):
    step = calc_e_1(theta, v0, dstar) / calc_eprime_1(theta, v0, dstar)
    return theta - step


def make_figure_flat(xmax=None, ymax=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    if xmax is not None:
        ax.set_xlim(-5, xmax)

    if ymax is not None:
        ax.set_ylim(-1, ymax)

    ax.add_artist(ptc.Rectangle((-1000,-.5), 2000, .5, facecolor="k"))

    return ax
