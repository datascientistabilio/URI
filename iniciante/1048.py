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