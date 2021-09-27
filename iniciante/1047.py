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