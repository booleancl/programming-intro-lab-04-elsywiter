# Similar a los arreglos, los diccionarios no permiten
# estructurar información con la diferencia de que los
# elementos están ordenados por llave y no por índice. Ejemplo

my_car = {
        "brand": "Mazda",
        "model": "5",
        "year": "2022",
        "options": ["5 puertas", "Aire acondicionado", "Frenos ABS"],
        "available": True
}

print(my_car["brand"])
print(my_car["year"])
print(my_car["options"])

# Si queremos todos las llaves, tenemos el metodo .keys(
    print(my_car.keys())
# Si queremos todos los valores, tenemos el metodo .values
    print(my_car.values())

# Podemos tambien actualizar valores de una determinada llave
my_car["model"] = "9"
print(my_car["molde"])

# También podemos agregar llaves y valores
my_car["color"] = "silver"
print(my_car)
)