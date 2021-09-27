# Idade em dias cod 1020
dia = int(input())
ano = int(dia/365)
dia -= ano*365
meses = int(dia/30)
dia -= meses*30
print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dia} dia(s)')