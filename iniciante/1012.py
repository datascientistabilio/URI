#Área cod 1012
linha = input().split(" ")
a, b, c = linha
print(f"TRIANGULO: {float(a)*float(c)/2:.3f}")
print(f"CIRCULO: {3.14159*float(c)**2:.3f}")
print(f"TRAPEZIO: {((float(a)+float(b))/2)*float(c):.3f}")
print(f"QUADRADO: {float(b)*float(b):.3f}")
print(f"RETANGULO: {float(a)*float(b):.3f}")