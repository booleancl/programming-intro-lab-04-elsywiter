import time

# Es perfectamente posible llamar una funcion de otra 
# Lo hicimos cuando calculamos el volumen de un cilindro

# Pero tambien es perfectamen posible cuando una funcion se llame asi misma
# Esto es una tecnica muy poderosa para ciertos problemas

# Funcion conteo regresivo
def countdown(number):
    if number <= 0:
        print("KABUMM")
    else:
        print(number)
        time.sleep(0.5)
        countdown(number - 1)

countdown(5)

