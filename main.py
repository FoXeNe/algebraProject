# точки
A = (1, 1, 1)
B = (2, 2, 0)
C = (0, 2, 2)
D = (2, 0, 2)
P = (1, 2, 1)


def make_vector(A, B):
    a = A
    b = B
    res = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    return res

def normal_vector(A, B, C, D):
    """
    посчитать вектор нормали. AB это точки первого вектора, CD точки второго вектора
    """
    v1x, v1y, v1z = make_vector(A, B) 
    v2x, v2y, v2z = make_vector(C, D)
    i = v1y * v2z - v1z * v2y
    j = v1z * v2x - v1x * v2z
    k = v1x * v2y - v1y * v2x
    return (i, j, k)

def plane_equationn(nVec, point):
    """
    получить коэффициенты уравнения плоскости и найти D
    """
    A, B, C = nVec
    x0, y0, z0 = point
    
    D = -(A * x0 + B * y0 + C * z0)
    
    return A, B, C, D

def plane_equation(nVec):
    '''
    подаем вектор нормали, получаем уравнение плоскости
    '''
    # находим D
    D = -nVec[0] - nVec[1] - nVec[2]
    return nVec[0], nVec[1], nVec[2], D
print(plane_equationn((2, 0, 2), P))
