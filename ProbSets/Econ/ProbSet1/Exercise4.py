from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fminbound
import scipy.optimize as opt



def getExpectedVOfW(function_V, w_grid, N):
    expectation = 0
    for i in range(N):
        expectation += (1/N) * function_V(w_grid[i])
    return expectation

def Bellman_op(V, w_grid, params):
    beta, b, mu, sigma, N = params
    V_func = interpolate.interp1d(w_grid, V, fill_value='extrapolate')
    TV = np.empty_like(V)
    PF = np.empty_like(V)
    for i in range(N):
        if (b + beta * getExpectedVOfW(V_func, w_grid, N)) >= (1/(1-beta) * w_grid[i]):
            TV[i] = (b + beta * getExpectedVOfW(V_func, w_grid, N))
            PF[i] = 0 #choose to wait here
        else:
            TV[i] = (1/(1-beta) * w_grid[i])
            PF[i] = 1 #choose to accept
    return TV, PF









def iterationWith(b):
    beta = 0.96

    mu = 0
    sigma = 0.15
    # Compute cut-off values
    N = 30  # number of grid points (will have one more cut-off point than this)
    ln_w_cutoffs = (sigma * norm.ppf(np.arange(N + 1) / N)) + mu
    ln_w_grid = ((N * sigma * (norm.pdf((ln_w_cutoffs[:-1] - mu) / sigma)- norm.pdf((ln_w_cutoffs[1:] - mu) / sigma)))+ mu)
    #Now we have cut ln_w into N intervals, each interval prob = 1/N
    w_grid = np.exp(ln_w_grid)
    #a grid of corresponding w
    params = (beta, b, mu, sigma, N)
    VFtol = 1e-6
    VFdist = 7
    VFmaxiter = 500
    VFiter = 1


    V = np.zeros(N)
    Vstore = np.zeros((N, VFmaxiter))

    while VFdist > VFtol and VFiter < VFmaxiter:
        Vstore[:, VFiter] = V
        TV, PF = Bellman_op(V, w_grid, params)
        VFdist = (np.absolute(V - TV)).max()
        #print('Iteration ', VFiter, ', distance = ', VFdist)
        V = TV
        VFiter += 1


    if VFiter < VFmaxiter:
        print('Value function converged after this many iterations:', VFiter)
    else:
        print('Value function did not converge')

    VF = V

    for cc in range(N):
        if PF[cc] == 1:
            break

    return VF, PF, w_grid, cc


#Q1: b=0.05, plot value function
VF, PF, w_grid, cutoff_wage = iterationWith(0.05)


print("When b = 0.05, the reservation wage is ", w_grid[cutoff_wage])
plt.figure(figsize = [12,5])
plt.subplot(1,2,1)
plt.plot(w_grid[1:], VF[1:])
plt.xlabel('Offered wage')
plt.ylabel('Value Function')
plt.title('Value Function - Job Searching Model')


VF1, PF1, w_grid1, cutoff_wage1 = iterationWith(0.5)
VF2, PF2, w_grid2, cutoff_wage2 = iterationWith(0.6)
VF3, PF3, w_grid3, cutoff_wage3 = iterationWith(0.7)
VF4, PF4, w_grid4, cutoff_wage4 = iterationWith(0.8)
VF5, PF5, w_grid5, cutoff_wage5 = iterationWith(0.9)
VF6, PF6, w_grid6, cutoff_wage6 = iterationWith(1.0)

b_vector = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
res_wages = [w_grid1[cutoff_wage1], w_grid2[cutoff_wage2],
             w_grid3[cutoff_wage3], w_grid4[cutoff_wage4],
             w_grid5[cutoff_wage5], w_grid6[cutoff_wage6]]
plt.subplot(1,2,2)
plt.plot(b_vector, res_wages)
plt.xlabel('Unemployment benefits')
plt.ylabel('Reservation wage')
plt.title("Reservation wage v.s. unemployment benefits")
'''
b_vector = np.linspace(0.5, 1, 0.1)
M1=[0]*len(b_vector)
M2=[0]*len(b_vector)
M3=[0]*len(b_vector)
M4=[0]*len(b_vector)
for l in b_vector:
    M1[l], M2[l], M3[l], M4[l] = iterationWith(b)

plt.subplot(1,2,2)
plt.plot(b_vector, M4)
'''
plt.show()
