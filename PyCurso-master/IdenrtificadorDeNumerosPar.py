nmr1 = input("Digite um numero inteiro: ")

if nmr1.isdigit():
    nmr1 = int(nmr1)
    if (nmr1 % 2) == 0:
        print(f"{nmr1} é Par")
    else:
        print(f"{nmr1} é Ímpar")

else:
    print("Apenas numeros inteiros")