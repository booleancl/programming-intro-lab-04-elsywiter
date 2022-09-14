# Tenemos expresiones que se pueden evaluar en terminos booleanos
# ó dicotomicos
# Ejemplo:

print (10 > 9)

# Esto nos permite hacer ejecuciones condicionales,  por ejemplo

def is_adult(age):
    if age>= 18:
        return True
    else:
        return False 

gaby_age = 4
paola_age = 30

# Estas siguientes intrucciones la podemos leer como:
# si(if) el resultado de is_adult ejecutada con la variable gaby_age
# Es verdadero, entonces el programa imprime '¿ Quieres una Cerverza'
# DE OTRO MODO (else), imprime 'Cantemos chuchuwa?'"

if is_adult(paola_age):
    print ("Quieres una cerverza")
else:
    print("cantemos chuchuwa?")

# El if es una abreviacion "else if" nos permite seguir evaluando
# expresiones, podemos tener tanto como lo necesitamos


if ("paola_age > gaby_age") :
    print ("paola es mayor que gaby")
else:
    print ("tinen la misma edad gay y paola")
    