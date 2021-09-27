# Distância entre dois pontos cod 1015
x, y = list(map(float, input().split(" ")))
z, w = list(map(float, input().split(" ")))
d = ((z-x)**2+(w-y)**2) ** (1/2)
print(round(d,4))