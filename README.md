# Primer-juego

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/alexlomu/Primer-juego)
https://github.com/alexlomu/Primer-juego
Hemos resuelto un juego de adivinar con valores enteros entre 0 y 99.
El diagrama de flujo que tenemos en nuestro código es el siguiente:

![figma_adivina_numero](https://user-images.githubusercontent.com/91721507/140508358-2491f13c-8cf0-4e90-9afa-6d64cc06acf8.jpg)

El código del juego es el siguiente:

```import random
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
