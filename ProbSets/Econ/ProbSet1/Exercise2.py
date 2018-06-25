# Import packages
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fminbound
import scipy.optimize as opt

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




def expected_production(sigma_z, capital, alpha):
    # Since we know ln(z) follows a normal distribution, we can directly calculate
    #the expected value of z using probability theory
    return (capital**alpha) * math.exp(0.5* (sigma_z**2))



def capital_tomorrow(delta, capital, investment):
    return (1-delta)*capital + investment

def expected_production_tomorrow(i_today, k_today, params):
    gamma, beta, delta, alpha, sigma_z = params
    k_tomorrow = capital_tomorrow(delta, k_today, i_today)
    return expected_production(sigma_z, k_tomorrow, alpha)



def Bellman_op(V, y_grid, params, capital_today):
    #interpolate a function based on current guess of V
    V_func = interpolate.interp1d(y_grid, V, fill_value='extrapolate')

    gamma, beta, delta, alpha, sigma_z = params
    #initialize new V guess and consum choice investment choice
    TV = np.empty_like(V)
    optInv = np.empty_like(V)
    optCon = np.empty_like(V)

    for i, y in enumerate(y_grid):
        def objective(investment):
            arg = expected_production_tomorrow(investment, capital[i], params)
            #arg = expected_production_tomorrow(investment, params, capital[i])
            #(1-delta)*capital[i] + investment)**alpha * math.exp(0.5* (sigma_z**2))
            return -utility(y, investment, gamma) - beta * V_func(arg)
        investment_star = fminbound(objective, 1e-6, y - 1e-6)
        optInv[i] = investment_star
        optCon[i] = y_grid[i] - investment_star
        TV[i] = -objective(investment_star)
    return TV, optInv, optCon



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

#initial guess
V = np.zeros_like(y_grid)
capital = np.zeros_like(y_grid) + 0.05
Vstore = np.zeros((y_size, VFmaxiter))

while VFdist > VFtol and VFiter < VFmaxiter:
    Vstore[:, VFiter] = V
    TV, optInv, optCon = Bellman_op(V, y_grid, params, capital)
    VFdist = (np.absolute(V - TV)).max()
    print('Iteration ', VFiter, ', distance = ', VFdist)
    V = TV
    capital = capital_tomorrow(delta, capital, optInv)
    VFiter += 1

if VFiter < VFmaxiter:
    print('Value function converged after this many iterations:', VFiter)
else:
    print('Value function did not converge')

VF = V

plt.figure(figsize = [18, 5])

plt.subplot(1,3,1)
plt.plot(y_grid[1:], VF[1:])
plt.xlabel('Initial output endownment')
plt.ylabel('Value Function')
plt.title('Value Function - Neoclassical Growth Model')

plt.subplot(1,3,2)
plt.plot(y_grid[1:], optInv[1:])
plt.xlabel('Initial output endownment')
plt.ylabel('Optimal choice of investment')
plt.title('Policy Function - choice of investment')

plt.subplot(1,3,3)
plt.plot(y_grid[1:], optCon[1:])
plt.xlabel('Initial output endownment')
plt.ylabel('Optimal choice of consumption')
plt.title('Policy Function - choice of consumption')
'''
plt.plot(y_grid[1:], VF[1:])
plt.xlabel('Initial output endownment')
plt.ylabel('Value Function')
plt.title('Value Function - deterministic cake eating')
'''

plt.show()
