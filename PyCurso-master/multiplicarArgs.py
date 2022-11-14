


def mul(*args):
    print(args)
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = mul(1,2,3,4,5)
print(1*2*3*4*5)
print(resultado)
