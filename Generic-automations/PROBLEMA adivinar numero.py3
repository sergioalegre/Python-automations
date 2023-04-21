import random

cuantos_juegos = int(input("Cuantos juegos quieres "))
i=0

for i in range(cuantos_juegos):
    print("Comineza el juego número",i+1)
    numero = random.randint(1,25)
    respuesta = 0
    intento = 0
    while(respuesta != numero):
            respuesta = int(input("dime un numero "))
            intento+=1
            if(respuesta > numero):
                print("muy alto")
            elif(respuesta < numero):
                print("muy bajo")
            elif (respuesta == numero):
                print("Has encontrado el numero en el intento: %s" % intento)
            continue
    i+=1
