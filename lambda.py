# Funciones Lambda
# Son usadas cuando deseamos crear un comportamiento que será utilizado únicamente.
# De esa manera no tendremos que revisar el código para encontrar una función usada una vez.

# No hace falta que tengan nombre

# Función convencional
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

# Función Lambda

a = 1
b = 2
sum = lambda x,y : x + y # parametros : comportamiento
c = sum(a,b)
print(c)

# Ejercicio

l = [2,4,7,3,14,19]
for i in l:
    is_even = lambda n : (n % 2) == 1
    print(is_even(i))
