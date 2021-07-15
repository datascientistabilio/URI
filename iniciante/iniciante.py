#Hellow world cod 1000
print("Hello World!")

#Soma cod 1001
a = int(input())
b = int(input())
X = a + b
print("X =", X)

#Área do circulo cod 1002
n=3.14159
raio = float(input())
print(f"A={n*(raio*raio):.4f}")

#Soma simples cod 1003
A = int(input())
B = int(input())
SOMA = A+B
print("SOMA =",SOMA)

#Produto simples cod 1004
A = int(input())
B = int(input())
PROD = A*B
print("PROD =",PROD)

#Média simples cod 1005
A = float(input())
B = float(input())
MEDIA = (A*3.5+B*7.5)/11
print(f"MEDIA = {MEDIA:.5f}")

#Média com 3 variáveis cod 1006
A = float(input())
B = float(input())
C = float(input())
MEDIA = (A*2+B*3+C*5)/10
print(f"MEDIA = {MEDIA:.1f}")

#Diferença cod 1007
A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = (A*B-C*D)
print("DIFERENCA =",DIFERENCA)

#Calculado o salário por hora trabalhada cod 1008
NUMBER = int(input())
HOURS = int(input())
VALUE = float(input())
SALARY = HOURS*VALUE
print("NUMBER =",NUMBER)
print(f"SALARY = U$ {SALARY:.2f}")

#SÁLARIO COM BONUS cod 1009
NOME = input()
SALARIO = float(input())
TOTAL_VENDAS = float(input())
print(f"TOTAL = R$ {TOTAL_VENDAS*0.15+SALARIO:.2f}")

#CALCULO SIMPLES cod 1010
linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)

# Calculando o volume cod 1011
raio = float(input())
pi = 3.14159

print(f"VOLUME = {4/3*pi*raio**3:.3f}")

#Área cod 1012
linha = input().split(" ")
a, b, c = linha
print(f"TRIANGULO: {float(a)*float(c)/2:.3f}")
print(f"CIRCULO: {3.14159*float(c)**2:.3f}")
print(f"TRAPEZIO: {((float(a)+float(b))/2)*float(c):.3f}")
print(f"QUADRADO: {float(b)*float(b):.3f}")
print(f"RETANGULO: {float(a)*float(b):.3f}")

# Maior cod 1013
A, B, C = list(map(int, input().split(" ")))
maior = max(A,B,C)
print(maior, "eh o maior")

# Consumo cod 1014
x = int(input())
y = float(input())
print(f"{x/y:.3f}","km/l")

# Distância entre dois pontos cod 1015
x, y = list(map(float, input().split(" ")))
z, w = list(map(float, input().split(" ")))
d = ((z-x)**2+(w-y)**2) ** (1/2)
print(round(d,4))

# Distância cod 1016
km_min = 2
distancia = int(input())
print(distancia*km_min,"minutos")

# Gasto de combustivel cod 1017
t = int(input());
v = int(input());
print(f'{(v*t)/12:.3f}')

# Cédulas cod 1018
valor = int(input())
print(valor)
cedulas = [100, 50, 20 , 10 , 5, 2, 1]

for cedula in cedulas:
  qtd_cedulas = int(valor/cedula)
  print("{} nota(s) de R$ {},00".format(qtd_cedulas, cedula))
  valor -= qtd_cedulas * cedula

# Conversão de tempo cod 1019
num = int(input())
hora = num // 60**2
num = num - hora * 60**2
minuto = num // 60
num = num - minuto*60
segundo = num
print('{}:{}:{}'.format(hora, minuto, segundo))


# cod 1020




















