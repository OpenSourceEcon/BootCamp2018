"""
Sorry I really don't know how to do this problem. I worked through the notebooks and lecture notes.
I can see the logic but I just don't know how to implement it.
I tried to modify the code of a similar problem on quantecon. However the iteration does not converge.
It blows up at some iteration and never converges to the soln againself.
I wish to see the solution code.
"""


# Import packages
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fminbound
import scipy.optimize as opt
import ar1_approx as ar1


def utility(production, investment, gamma):
    """
    Per period utility function
    """
    C = production - investment
    if gamma == 1:
        U = np.log(C)
    else:
        U = (C ** (1 - gamma)) / (1 - gamma)
    return U

from scipy.optimize import fminbound


"""
def bellman_operator(w, grid, β, u, f, shocks, Tw=None, compute_policy=0):

    The approximate Bellman operator, which computes and returns the
    updated value function Tw on the grid points.  An array to store
    the new set of values Tw is optionally supplied (to avoid having to
    allocate new arrays at each iteration).  If supplied, any existing data in
    Tw will be overwritten.

    Parameters
    ----------
    w : array_like(float, ndim=1)
        The value of the input function on different grid points
    grid : array_like(float, ndim=1)
        The set of grid points
    β : scalar
        The discount factor
    u : function
        The utility function
    f : function
        The production function
    shocks : numpy array
        An array of draws from the shock, for Monte Carlo integration (to
        compute expectations).
    Tw : array_like(float, ndim=1) optional (default=None)
        Array to write output values to
    compute_policy : Boolean, optional (default=False)
        Whether or not to compute policy function

    # === Apply linear interpolation to w === #
    w_func = lambda x: np.interp(x, grid, w)

    # == Initialize Tw if necessary == #
    if Tw is None:
        Tw = np.empty_like(w)

    if compute_policy:
        σ = np.empty_like(w)

    # == set Tw[i] = max_c { u(c) + β E w(f(y  - c) z)} == #
    for i, y in enumerate(grid):
        def objective(c):
            return - u(c) - β * np.mean(w_func(f(y - c) * shocks))
        c_star = fminbound(objective, 1e-10, y)
        if compute_policy:
            σ[i] = c_star
        Tw[i] = - objective(c_star)

    if compute_policy:
        return Tw, σ
    else:
        return Tw


"""
#v～N（0， sigma_v)
N = 8
num_sigma = 4
step = (num_sigma * sigma_z) / (N / 2)
pi_R, z_grid_R = ar1.rouwen(rho, mu, step, N)

gamma = 0.5
beta = 0.96
delta = 0.05
alpha =0.4
sigma_z = 0.2
params = (gamma, beta, delta, alpha, sigma_z)
#function domain
y_size = 200
y_grid = np.linspace(1, 2, y_size)

VFtol = 1e-5
VFdist = 7
VFmaxiter = 500
VFiter = 1
