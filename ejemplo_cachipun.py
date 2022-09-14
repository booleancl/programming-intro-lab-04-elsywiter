print("bienvenido al juego del cachipun")
print("selecciona tu opción")
print("1 para piedra")
print("2 para papel")
print("3 para tijera")
user_input = int(input("jugador1\n"))
options = ["piedra", "papel", "tijera",]
user_options = options[user_input -1]

computer_options = random.choice(options)

print("mi mano: ", user_options)
print("mano del compuatdor:", computer_options)


if (user_options == computer_options):
    prin("empatan jugadores")
elif(user_options == "piedra" and computer_options == "tijera") or (user_options == "papel" and computer_options == "piedra"):
    print("felicitaciones! ganaste la partida")
else:
    print ("lo siento el computador ha ganado")
