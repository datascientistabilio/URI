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


# Idade em dias cod 1020
dia = int(input())
ano = int(dia/365)
dia -= ano*365
meses = int(dia/30)
dia -= meses*30
print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dia} dia(s)')

# Notas e Moedas 1021
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtd_cedulas = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, nota))
    valor -= qtd_cedulas * nota

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = int(round(valor,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    valor -= round(qtd_moedas * moeda, 2)


# Teste de seleção 1035
A, B, C, D = list(map(int, input().split(" ")))

if B > C and D > A and C+D > A+B and A>0 and B>0 and C>0 and D>0 and A%2==0:
  print("Valores aceitos")
else:
  print("Valores nao aceitos")

# Fórmula de Bhaskara 1036
a, b, c = list(map(float, input().split(" ")))

if a == 0 or (b ** 2 - 4 * a * c) < 0:
  print("Impossivel calcular")
else:
  x1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
  x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
  print("R1 =",round(x1,5))
  print("R2 =",round(x2,5))

# Intervalo 1037
num = float(input())

if  num >=0 and num <=25:
  print("Intervalo [0,25]")
elif num >25 and num <=50:
  print("Intervalo (25,50]")
elif num >50 and num <=75:
  print("Intervalo (50,75]")
elif num >75 and num <=100:
  print("Intervalo (75,100]")
else:
  print("Fora de intervalo")

# 1047
hora_inicial, minuto_inicial, hora_final, minuto_final = list(map(int,input().split(" ")))

if hora_inicial < hora_final:
    h = hora_final - hora_inicial
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
    if minuto_inicial > minuto_final:
        h = h - 1
        m = (60 - minuto_inicial) + minuto_final
    if minuto_inicial == minuto_final:
        m = 0

if hora_inicial > hora_final:
    h = (24 - hora_inicial) + hora_final
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
    if minuto_inicial > minuto_final:
        h = h - 1
        m = (60 - minuto_inicial) + minuto_final
    if minuto_inicial == minuto_final:
        m = 0

if hora_inicial == hora_final:
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
        h = 0
    if minuto_inicial > minuto_final:
        m = (60 - minuto_inicial) + minuto_final
        h = 23
    if minuto_inicial == minuto_final:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))

# 1052
mes = int(input())

if mes == 1:
    print("January")
elif mes == 2:
    print("February")
elif mes == 3:
    print("March")
elif mes == 4:
    print("April")
elif mes == 5:
    print("May")
elif mes == 6:
    print("June")
elif mes == 7:
    print("July")
elif mes == 8:
    print("August")
elif mes == 9:
    print("September")
elif mes == 10:
    print("October")
elif mes == 11:
    print("November")
elif mes == 12:
    print("December")

# 1066
par=0
imp=0
pos=0
neg = 0
for contador in range(0,5,1):
    num = int(input())    
    if num%2==0:
        par+= 1
    else:
        imp+= 1
    if num>0:
        pos+= 1
    if num<0:
        neg+= 1

print(par,"valor(es) par(es)")
print(imp,"valor(es) impar(es)")
print(pos,"valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")

# média 3 1040
num1,num2,num3,num4 = list(map(float, input().split(" ")))
media = ((num1*2)+(num2*3)+(num3*4)+(num4*1))/(2+3+4+1)
if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media <5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >=5 and media <=6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame:",exame)
    nota_recup = (exame+media)/2
    if nota_recup >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {nota_recup:.1f}")
    else:
        print("Aluno reprovado.",nota_recup)

# 1067
num = int(input())
x=0
for x in range(num):
    
    if x%2==1:
      print(x)
if num%2==1:
  print(num)
  
  
# 1048
sal = float(input())

if sal >=0 and sal <=400:
    reajuste = sal*0.15 
    sal = (sal*0.15)+sal
    print(f"Novo salario: {sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 15 %")
elif sal >= 400.01 and sal <= 800:
    reajuste = sal*0.12
    sal = (sal*0.12)+sal
    print(f"Novo salario: {sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 12 %")
elif sal >= 800.01 and sal <= 1200:
    reajuste = sal*0.10
    sal = (sal*0.10)+sal
    print(f"Novo salario: {sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 10 %")
elif sal >= 1200.01 and sal <= 2000:
    reajuste = sal*0.07
    sal = (sal*0.07)+sal
    print(f"Novo salario: {sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 7 %")
elif sal > 2000:
    reajuste = sal*0.04
    sal = (sal*0.04)+sal
    print(f"Novo salario: {sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 4 %")
    
# ERRO ERRO 2686 FIX
while True: 
    try: 
        minut9o = float(input())
        if minuto == 360 or minuto >=0 and minuto<= 105:
            print("Bom Dia!!")
            if minuto == 0 or minuto == 360:
                  print("06:00:00")
            if minuto >0 and minuto <=15:
                
                resp = minuto-0
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("06:0"+str(minuto)+":00")
                else:
                  print("06:"+str(minuto)+":00")
            elif minuto >15 and minuto <=30:
                resp = minuto-15
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("07:0"+str(minuto)+":00")
                else:
                  print("07:"+str(minuto)+":00")
            elif minuto >30 and minuto <=45:
                resp = minuto-30
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("08:0"+str(minuto)+":00")
                else:
                  print("08:"+str(minuto)+":00")
            elif minuto >45 and minuto <=60:
                resp = minuto-45
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("09:0"+str(minuto)+":00")
                else:
                  print("09:"+str(minuto)+":00")
            elif minuto >60 and minuto <=75:
                resp = minuto-60
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("10:0"+str(minuto)+":00")
                else:
                  print("10:"+str(minuto)+":00")
            elif minuto >75 and minuto <90:
                resp = minuto-75
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("11:0"+str(minuto)+":00")
                else:
                  print("11:"+str(minuto)+":00")
            elif minuto >90 and minuto <=105:
                resp = minuto-90
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("12:0"+str(minuto)+":00")
                else:
                  print("12:"+str(minuto)+":00")
        elif minuto >105 and minuto<=195:
            print("Boa Tarde!!")
            if minuto >105 and minuto <=120:
                resp = minuto-105
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("13:0"+str(minuto)+":00")
                else:
                  print("13:"+str(minuto)+":00")
            elif minuto >120 and minuto <=135:
                resp = minuto-120
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("14:0"+str(minuto)+":00")
                else:
                  print("14:"+str(minuto)+":00")
            elif minuto >135 and minuto <=150:
                resp = minuto-135
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("15:0"+str(minuto)+":00")
                else:
                  print("15:"+str(minuto)+":00")
            elif minuto >150 and minuto <=165:
                resp = minuto-150
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("16:0"+str(minuto)+":00")
                else:
                  print("16:"+str(minuto)+":00")
            elif minuto >165 and minuto <=180:
                resp = minuto-165
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("17:0"+str(minuto)+":00")
                else:
                  print("17:"+str(minuto)+":00")
            elif minuto >180 and minuto <=195:
                resp = minuto-180
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("18:0"+str(minuto)+":00")
                else:
                  print("18:"+str(minuto)+":00")
        elif minuto >195 and minuto<=285:
            print("Boa Noite!!")
            if minuto >195 and minuto <=210:
                resp = minuto-195
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("19:0"+str(minuto)+":00")
                else:
                  print("19:"+str(minuto)+":00")
            elif minuto >210 and minuto <=225:
                resp = minuto-210
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("20:0"+str(minuto)+":00")
                else:
                  print("20:"+str(minuto)+":00")
            elif minuto >225 and minuto <=240:
                resp = minuto-225
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("21:0"+str(minuto)+":00")
                else:
                  print("21:"+str(minuto)+":00")
            elif minuto >240 and minuto <=255:
                resp = minuto-240
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("22:0"+str(minuto)+":00")
                else:
                  print("22:"+str(minuto)+":00")
            elif minuto >255 and minuto <=270:
                resp = minuto-255
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("23:0"+str(minuto)+":00")
                else:
                  print("23:"+str(minuto)+":00")
            elif minuto >270 and minuto <=285:
                resp = minuto-270
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("00:0"+str(minuto)+":00")
                else:
                  print("00:"+str(minuto)+":00")
        elif minuto >285 and minuto<=360:
            print("De Madrugada!!")
            if minuto >285 and minuto <=299:
                resp = minuto-285
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("01:0"+str(minuto)+":00")
                else:
                  print("01:"+str(minuto)+":00")
            elif minuto >=300 and minuto <=315:
                resp = minuto-300
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("02:0"+str(minuto)+":00")
                else:
                  print("02:"+str(minuto)+":00")
            elif minuto >315 and minuto <=330:
                resp = minuto-315
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("03:0"+str(minuto)+":00")
                else:
                  print("03:"+str(minuto)+":00")
            elif minuto >330 and minuto <=345:
                resp = minuto-330
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("04:0"+str(minuto)+":00")
                else:
                  print("04:"+str(minuto)+":00")
            elif minuto >345 and minuto <=359:
                resp = minuto-345
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("05:0"+str(minuto)+":00")
                else:
                  print("05:"+str(minuto)+":00")
    except EOFError:
                break
