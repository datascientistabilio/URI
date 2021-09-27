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