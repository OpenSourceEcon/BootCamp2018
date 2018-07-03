import numpy as np
import scipy.stats as st
from scipy.stats import norm
import scipy.integrate as integrate

def rouwen(rho, mu, step, num):
    '''
    Adapted from Lu Zhang and Karen Kopecky. Python by Ben Tengelsen.
    Construct transition probability matrix for discretizing an AR(1)
    process. This procedure is from Rouwenhorst (1995), which works
    well for very persistent processes.

    INPUTS:
    rho  - persistence (close to one)
    mu   - mean and the middle point of the discrete state space
    step - step size of the even-spaced grid
    num  - number of grid points on the discretized process

    OUTPUT:
    dscSp  - discrete state space (num by 1 vector)
    transP - transition probability matrix over the grid
    '''

    # discrete state space
    dscSp = np.linspace(mu - (num - 1) / 2 * step, mu + (num - 1) / 2 * step,
                        num).T

    # transition probability matrix
    q = p = (rho + 1)/2.
    transP = np.array([[p**2, p*(1-q), (1-q)**2],
                      [2*p*(1-p), p*q+(1-p)*(1-q), 2*q*(1-q)],
                      [(1-p)**2, (1-p)*q, q**2]]).T

    while transP.shape[0] <= num - 1:

        # see Rouwenhorst 1995
        len_P = transP.shape[0]
        transP = p*np.vstack((np.hstack((transP, np.zeros((len_P, 1)))), np.zeros((1, len_P+1)))) \
        + (1 - p)*np.vstack((np.hstack((np.zeros((len_P, 1)), transP)), np.zeros((1, len_P+1)))) \
        + (1 - q)*np.vstack((np.zeros((1, len_P+1)), np.hstack((transP, np.zeros((len_P, 1)))))) \
        + q * np.vstack((np.zeros((1, len_P+1)), np.hstack((np.zeros((len_P, 1)), transP))))

        transP[1:-1] /= 2.

    # ensure columns sum to 1
    if np.max(np.abs(np.sum(transP, axis=1) - np.ones(transP.shape))) >= 1e-12:
        print('Problem in rouwen routine!')
        return None
    else:
        return transP.T, dscSp


def tauchenhussey(N, mu, rho, sigma, baseSigma):
    """
    Function tauchenhussey

    Purpose:    Finds a Markov chain whose sample paths
                approximate those of the AR(1) process
                    z(t+1) = (1-rho)*mu + rho * z(t) + eps(t+1)
                where eps are normal with stddev sigma

    Format:     {Z, Zprob} = TauchenHussey(N,mu,rho,sigma,m)

    Input:      N         scalar, number of nodes for Z
            mu        scalar, unconditional mean of process
            rho       scalar
            sigma     scalar, std. dev. of epsilons
            baseSigma scalar, std. dev. used to calculate Gaussian
            quadrature weights and nodes, i.e. to build the
            grid. I recommend that you use
            baseSigma = w*sigma +(1-w)*sigmaZ where sigmaZ = \
                    sigma/sqrt(1-rho^2),
                and w = 0.5 + rho/4. Tauchen & Hussey recommend
                baseSigma = sigma, and also mention baseSigma = sigmaZ.

    Output:     Z       N*1 vector, nodes for Z
                Zprob   N*N matrix, transition probabilities

    Author:     Benjamin Tengelsen, Carnegie Mellon University (python)
                Martin Floden, Stockholm School of Economics (original)
                January 2007 (updated August 2007)

    This procedure is an implementation of Tauchen and Hussey's
    algorithm, Econometrica (1991, Vol. 59(2), pp. 371-396)
    """

    Z = np.zeros((N, 1))
    Zprob = np.zeros((N, N))
    [Z, w] = gaussnorm(N, mu, baseSigma ** 2)
    for i in range(N):
        for j in range(N):
            EZprime = (1 - rho) * mu + rho * Z[i]
            Zprob[i, j] = (w[j] * st.norm.pdf(Z[j], EZprime, sigma) /
                           st.norm.pdf(Z[j], mu, baseSigma))

    for i in range(N):
        Zprob[i, :] = Zprob[i, :] / sum(Zprob[i, :])

    return Z.T, Zprob


def gaussnorm(n, mu, s2):
    """
    Find Gaussian nodes and weights for the normal distribution
    n  = # nodes
    mu = mean
    s2 = variance
    """
    [x0, w0] = gausshermite(n)
    x = x0 * np.sqrt(2. * s2) + mu
    # print(s2,mu)
    # print(x)
    w = w0 / np.sqrt(np.pi)
    return [x, w]


def gausshermite(n):
    """
    Gauss Hermite nodes and weights following 'Numerical Recipes for C'
    """

    MAXIT = 10
    EPS = 3e-14
    PIM4 = 0.7511255444649425

    x = np.zeros((n, 1))
    w = np.zeros((n, 1))

    m = int((n + 1) / 2)
    for i in range(m):
        if i == 0:
            z = np.sqrt((2. * n + 1) - 1.85575 * (2. * n+1) ** (-0.16667))
        elif i == 1:
            z = z - 1.14 * (n ** 0.426) / z
        elif i == 2:
            z = 1.86 * z - 0.86 * x[0]
        elif i == 3:
            z = 1.91 * z - 0.91 * x[1]
        else:
            z = 2 * z - x[i - 1]

        for iter in range(MAXIT):
            p1 = PIM4
            p2 = 0.
            for j in range(n):
                p3 = p2
                p2 = p1
                p1 = (z * np.sqrt(2. / (j + 1)) * p2 - np.sqrt(float(j) /
                                                               (j + 1)) * p3)
            pp = np.sqrt(2. * n) * p2
            z1 = z
            z = z1 - p1 / pp
            if np.absolute(z - z1) <= EPS:
                break

        if iter > MAXIT:
            error('too many iterations'), end
        x[i, 0] = z
        x[n - i - 1, 0] = -z
        w[i, 0] = 2. / pp / pp
        w[n - i - 1, 0] = w[i]

    x = x[::-1]
    return [x, w]


def integrand(x, sigma_z, sigma, rho, mu, z_j, z_jp1):
    """
    Integrand in the determination of transition probabilities from the Adda-
    Cooper method.
    """
    val = (np.exp((-1 * ((x - mu) ** 2)) / (2 * (sigma_z ** 2)))
           * (norm.cdf((z_jp1 - (mu * (1 - rho)) - (rho * x)) / sigma)
               - norm.cdf((z_j - (mu * (1 - rho)) - (rho * x)) / sigma)))

    return val


def addacooper(N, mu, rho, sigma):
    """
    Function addacooper

    Purpose:    Finds a Markov chain whose sample paths
                approximate those of the AR(1) process
                    z(t+1) = (1-rho)*mu + rho * z(t) + eps(t+1)
                where eps are normal with stddev sigma

    Format:     {Z, Zprob} = addacooper(N, mu, rho, sigma)

    Input:      N     = scalar, number of nodes for Z
                mu    = scalar, unconditional mean of process
                rho   = scalar, persistence of the AR(1) process
                sigma = scalar, std. dev. of epsilons

    Output:     z_grid = N*1 vector, nodes for Z
                pi     = N*N matrix, transition probabilities

    Author:     Jason DeBacker, University of South Carolina (python)
                Jerome Adda ( Bocconi) and Russell Cooper (Penn State)
                (original)


    This procedure is an implementation of a modified version of Tauchen
    and Hussey's algorithm, Econometrica (1991, Vol. 59(2), pp. 371-396),
    this modification appears in Adda, Jerome and Russell Cooper, *Dynamic
    Economics: Quantitative Methods and Applications, MIT Press (2003)
        """
    # Compute std dev of the stationary distribution of z
    sigma_z = sigma / ((1 - rho ** 2) ** (1 / 2))

    # Compute cut-off values
    z_cutoffs = (sigma_z * norm.ppf(np.arange(N + 1) / N)) + mu

    # compute grid points for z
    z_grid = ((N * sigma_z * (norm.pdf((z_cutoffs[:-1] - mu) / sigma_z)
                              - norm.pdf((z_cutoffs[1:] - mu) / sigma_z)))
              + mu)

    # compute transition probabilities
    pi = np.empty((N, N))
    for i in range(N):
        for j in range(N):
            results = integrate.quad(integrand, z_cutoffs[i], z_cutoffs[i + 1],
                                     args=(sigma_z, sigma, rho, mu,
                                           z_cutoffs[j], z_cutoffs[j + 1]))
            pi[i, j] = (N / np.sqrt(2 * np.pi * sigma_z ** 2)) * results[0]

    return z_grid, pi
