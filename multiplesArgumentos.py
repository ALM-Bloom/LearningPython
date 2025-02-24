# Definir argumentos que podrán ser de tamaño variable para las funciones

# 'theres' podrá tomar un valor variable, es decir, dinámicamente.
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5)
# First: 1
# Second: 2
# Third: 3
# And all the rest... [4, 5]

# Se pueden enviar argumentos por palabras clave, de manera que el orden no importe

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
