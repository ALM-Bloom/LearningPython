# Definición de clases en Python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
        
# Declaración de un objeto
myobjectx = MyClass()
myobjecty = MyClass()

# Acceso a las variables
myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# Acceso a los métodos

myobjectx.function()

# La función _init_, se llama cuando se inicializa el objeto
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

# Ejercicio
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.color = "red"
car1.name = "convertible"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Fer"
car2.color = "blue"
car2.value = 10000.00
# test codec
print(car1.description())
print(car2.description())