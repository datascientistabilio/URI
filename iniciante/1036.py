# Fórmula de Bhaskara 1036
a, b, c = list(map(float, input().split(" ")))

if a == 0 or (b ** 2 - 4 * a * c) < 0:
  print("Impossivel calcular")
else:
  x1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
  x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
  print("R1 =",round(x1,5))
  print("R2 =",round(x2,5))