# Los arreglos son una estructura de datos fundamentales
# Que permiten agrupar valores

first_array = ['Sacar la basura', 'peinarse', 'dormir', 'secarla la ropa']

# En python el primer elemento tinene posición (indice 0)
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existe elemento con indice 4 y phyton da un error
# print(first_array[4]) 

# Podemos saber el largo de un arreglo o lista con la funcion pre definida len ()

print(len(first_array))

# Ademas, podemos agregar elementos al arreglo
first_array.append('comer')
first_array.append('dormir')

# Podemos indicar la posicion del nuevo elemento
first_array.insert(0,'levatarse')

# Podemos imprimir la lista completa
print(first_array)
