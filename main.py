import numpy as np
import re


def crammer3x3(A,B) :
    A_d = np.linalg.det(A)
    Ax = np.array([B[:], A[:,1:2].flatten(),A[:,2:].flatten()]).T
    Ax_d = np.linalg.det(Ax)
    Ay = np.array([A[:,:1].flatten(), B[:],A[:,2:].flatten()]).T
    Ay_d = np.linalg.det(Ay)
    Az = np.array([A[:,:1].flatten(), A[:,1:2].flatten(),B[:]]).T
    Az_d = np.linalg.det(Az)
    return [Ax_d/A_d, Ay_d/A_d,Az_d/A_d]

def crammer2x2(A,B) :
    A_d = np.linalg.det(A)
    Ax = np.array([B[:], A[:,1:].flatten()])
    Ax_d = np.linalg.det(Ax)
    Ay = np.array([ A[:,0].flatten(),B[:]])
    Ay_d = np.linalg.det(Ay)
    return [Ax_d/A_d, Ay_d/A_d]


def get_matrices(eqs:str,ord:int):
    p = re.compile(r"([+-]?\d*)x([+-]?\d*)y(?:([+-]?\d*)?z)?=([+-]?\d+)",re.I)
    L = []
    for (a,b,c,d) in p.findall(eqs):
        if ord == 3:
            L.append([int(a),int(b),int(c),int(d)])
        else:
            L.append([int(a),int(b),int(d)])
    L = np.array(L)
    return (L[:,:2],L[:,2:].flatten()) if ord == 2 else (L[:,:3],L[:,3:].flatten())

if __name__ == "__main__":
    order = int(input("Enter Order(2,3):- "))
    matrices = get_matrices(input("Enter Equations(Separated By Space):\n"),order)
    if order == 2:
        print(crammer2x2(matrices[0],matrices[1]))
    else:
        print(crammer3x3(matrices[0],matrices[1]))

