# Conversão de tempo cod 1019
num = int(input())
hora = num // 60**2
num = num - hora * 60**2
minuto = num // 60
num = num - minuto*60
segundo = num
print('{}:{}:{}'.format(hora, minuto, segundo))