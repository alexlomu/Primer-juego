import random
numero = random.randint(0,100)
numero_jugador = int(input("Introduce un número del 0 al 99: "))
jugadas = 0
if numero_jugador < 0 or numero_jugador > 99:
    print("Por favor, introude un número válido.")
    numero_jugador = int(input("\nIntroduce un número del 0 al 99: \n"))
while numero_jugador != numero:
    if numero_jugador < numero:
        jugadas += 1
        print("Demasiado pequeño")
        numero_jugador = int(input("\nIntroduce un número del 0 al 99: \n"))
    if numero_jugador > numero:
        jugadas += 1
        print("Demasiado grande")
        numero_jugador = int(input("\nIntroduce un número del 0 al 99: \n"))
if numero_jugador == numero:
    jugadas += 1
    print("Felicidades has ganado, el número era", str(numero))
    print("En total has hecho:", str(jugadas), "intentos.")


