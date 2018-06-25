# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'Problem 1'
import numpy as np
A = np.array( [ [3, -1, 4],[1, 5, -9]])
B = np.array( [ [2, 6, -5, 3],[5, -8, 9, 7] , [9 , -3, -2, -3]])
AB = A@B
print(AB)

'Problem 2'

A = np.array( [ [3, 1, 4],[1, 5, 9], [-5, 3, 1]])
C = -np.linalg.matrix_power(A, 3) + 9*np.linalg.matrix_power(A, 2) - 15*A
print(C)

'Problem 3'

E = np.ones((7,7), dtype=np.int)
B = np.ones((7,7), dtype=np.int)
T = -5*np.triu(E,1)
D = -1*np.tril(B)
B = T+D
A  = np.triu(E)
Y = A@B@A

'Problem 4'
def p4(X):
    M = X
    mask = M < 0
    M[mask] = 0
    print(M)
    return M

'Problem 5'
'''def  p5():
     J = np.array([ [0, 2, 4],[1, 3, 5]])
     O = np.tril(3*np.ones(3,3))
     P = -2*np.eye(3)
     LHS = np.vstack((np.zeros(3,3),J,O))
     MHS = np.vstack((np.transpose(J),np.zeros(2,2),np.zeros(3,2)))
     RHS = np.vstack((np.eye(3),np.zeros(2,3),P))
     output = np.hstack((LHS,MHS,RHS))
     print(output)
     return'''
def p5():
     J = np.array([ [0, 2, 4],[1, 3, 5]])
     O = np.ones((3,3))
     O = 3*np.tril(O)
     P = -2*np.eye(3,dtype=np.int)
     T = np.vstack((J,O,P))
     L = np.vstack((np.transpose(J),np.zeros([2,2],dtype=np.int),np.zeros([3,2],dtype=np.int)))
     Z = np.vstack((np.eye(3),np.zeros([2,3],dtype=np.int),P))
     X = np.hstack((T,L,Z))
     print(X)
     return

'Problem 6'

def p6(X):
    A = X.sum(axis=1)
    Y = X/A[:,np.newaxis]
    print(Y)
    return(Y)

'Problem 7'
def p7():
    grid =  np.load("/Users/suleymangozen/Desktop/bootcamp/BootCamp2018/Computation/Wk1_PyIntro/grid.npy")
    hmax =  np.max(grid[:,:-3]*grid[:,1:-2]*grid[:,2:-1]*grid[:,3:])
    ss   =  np.max(grid[:-3,:]*grid[1:2,:]*grid[2:-1,:]*grid[3:,:])
    pri  =  np.max(grid[:-3,:-3]*grid[1:-2,1:-2]*grid[2:-1:,2:-1]*grid[:-3,:-3])
    ll   =  np.max(grid[3:,:-3]*grid[2:-1,1:-2]*grid[1:-2,2:-1]*grid[:-3,3:])
    print(hmax)
    print(ss)
    print(pri)
    print(ll)
    return

p7()
    
    


