from numpy import *

vector1 = mat([1, 2, 3])
vector2 = mat([4, 5, 6])
print(sqrt((vector1 - vector2) * (vector1 - vector2).T))
