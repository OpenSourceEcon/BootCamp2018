"""
The graph looks really strange.
"""


# Import packages
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fminbound
import scipy.optimize as opt
import ar1_approx as ar1


def utility(consumption_vector, gamma):
    """
    Per period utility function
    """

    if gamma == 1:
        U = np.log(consumption_vector)
    else:
        U = (consumption_vector ** (1 - gamma)) / (1 - gamma)
    return U



gamma = 0.5
beta = 0.96
delta = 0.05
alpha = 0.4
sigma_z = 0.2

size_z = 4
mu_z = 0
rho_z = 0.8
sigma_v = sigma_z * np.sqrt(1 - rho_z)



# Use the Adda Cooper method suggested by Jason
ln_z_grid, pi_t =  ar1.addacooper(size_z, mu_z,rho_z ,sigma_v)
z_grid = np.exp(ln_z_grid)
pi = np.transpose(pi_t)



lb_k = 0.1
ub_k = 1.1
size_k = 100
k_grid = np.linspace(lb_k, ub_k, size_k)

C = np.zeros((size_k, size_k, size_z))

for i1 in range(size_k):
    for i2 in range(size_k):
        for i3 in range(size_z):
            C[i1, i2, i3] = z_grid[i3]* k_grid[i1]**alpha - k_grid[i2] + (1 - delta)*k_grid[i1]

C[C<=0] = 1e-15

U = utility(C, gamma)
U[C<0] = -9999999


VFtol = 1e-4
VFdist = 7
VFmaxiter = 500
V = np.zeros((size_k, size_z))
Vmat = np.zeros((size_k, size_k, size_z))
Vstore = np.zeros((size_k, size_z, VFmaxiter))
VFiter = 1

while VFdist > VFtol and VFiter < VFmaxiter:
    for i in range(size_k):
        for j in range(size_k):
            for m in range(size_z):
                EV = 0
                for n in range(size_z):
                    EV += V[j, n] * pi[m, n]
                Vmat[i, j, m] = U[i, j, m] + beta * EV

    TV = Vmat.max(1)
    PF = np.argmax(Vmat, axis=1)
    VFdist = (np.absolute(V - TV)).max()
    print('Iteration ', VFiter, ', distance = ', VFdist)
    Vstore[:,:, VFiter] = V.reshape(size_k, size_z,)
    V = TV

    VFiter += 1

if VFiter < VFmaxiter:
    print('Value function converged after this many iterations:', VFiter)
else:
    print('Value function did not converge')


VF = V

optInv = k_grid[PF]
#print(optInv)



plt.figure(figsize = [18, 5])
plt.subplot(1,3,1)
plt.plot(k_grid[1:], VF[1:, 0], label='$z$ = ' + str(z_grid[0]))
plt.plot(k_grid[1:], VF[1:, 1], label='$z$ = ' + str(z_grid[1]))
plt.plot(k_grid[1:], VF[1:, 2], label='$z$ = ' + str(z_grid[2]))
plt.plot(k_grid[1:], VF[1:, 3], label='$z$ = ' + str(z_grid[3]))
plt.legend(loc='lower right')
plt.xlabel("Capital Endowment")
plt.ylabel("Value Function")
plt.title("Value Function")



plt.subplot(1,3,2)
plt.plot(k_grid[:], optInv[:,0], label = '$z$ = ' + str(z_grid[0]))
plt.plot(k_grid[:], optInv[:,1], label = '$z$ = ' + str(z_grid[0]))
plt.plot(k_grid[:], optInv[:,2], label = '$z$ = ' + str(z_grid[0]))
plt.plot(k_grid[:], optInv[:,3], label = '$z$ = ' + str(z_grid[0]))
plt.legend(loc='lower right')
plt.xlabel("Capital Endowment")
plt.ylabel("Investment")
plt.title("Investment")
plt.show()
