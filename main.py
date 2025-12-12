# точки 
A = (1, 1, 1) 
B = (2, 2, 0) 
C = (0, 2, 2) 
D = (2, 0, 2) 
P = (1, 2, 1) 

FACES = [
    ("ABC", A, B, C, D),  # грань ABC, противоположная D
    ("ABD", A, B, D, C),  # грань ABD, противоположная C
    ("ACD", A, C, D, B),  # грань ACD, противоположная B
    ("BCD", B, C, D, A)   # грань BCD, противоположная A
]

# вспомогательные функции
def make_vector(A, B):
    a = A
    b = B
    res = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    
    return res

def normal_vector(AB, CD):
    """
    посчитать вектор нормали. AB это точки первого вектора, CD точки второго вектора
    """
    v1x, v1y, v1z = AB
    v2x, v2y, v2z = CD 
    i = v1y * v2z - v1z * v2y 
    j = v1z * v2x - v1x * v2z
    k = v1x * v2y - v1y * v2x

    return (i, j, k)

def plane_equation(v1, v2, v3):
    """
    получить коэффициенты уравнения плоскости и найти D
    """
    vec_a = make_vector(v1, v2)
    vec_b = make_vector(v1, v3)
    A, B, C = normal_vector(vec_a, vec_b)
    x, y, z = v1
    D = -(A * x + B * y + C * z)

    return A, B, C, D

def main():
    for name, v1, v2, v3, opposite in FACES:
        a, b, c, d = plane_equation(v1, v2, v3)
        # TODO сделать проверку на отрицательное число в уравнении для инвертирования
        # TODO сделать сравнение знаков
main()
