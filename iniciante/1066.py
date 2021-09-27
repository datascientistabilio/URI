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