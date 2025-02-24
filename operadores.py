# Aritméticos
numero = 1 + 2 * 3 / 4.0
print(numero)

# Módulo
resto = 11 % 3
print(resto)

# Exponencial
al_cuadrado = 7 ** 2
al_cubo = 2 ** 3
print(al_cuadrado)
print(al_cubo)

# Concatenación
helloworld = "hello" + " " + "world"
print(helloworld)

# Multiplicación de Strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Operadores con Listas
numeros_pares = [2,4,6,8]
numeros_impares = [1,3,5,7]
todos_numeros = numeros_pares + numeros_impares # Se concatenan los valores
print(todos_numeros)

print([1,2,3] * 3)

# Ejercicio
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")