hora = input("Que Horas são (0-23): ")
bomDia = 11
boatarde = 17
boanoite = 23

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= bomDia:
        print("Bom dia")
    if hora >= bomDia and hora <= boatarde:
        print("Boa tarde")
    if hora >= boatarde and hora <= boanoite:
        print("Boa noite")
    if hora >23 :
        print("A hora deve ser entre 0-23 !!")
else:
    print("Isso não é uma hora!!")