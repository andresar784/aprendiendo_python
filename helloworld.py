import math

print("Hola Mundo")

# Dia uno del challenge

print(2 + 3)
print(3 - 1)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 % 2)
print(3 // 2)

# Tipo de datos
print("Tipo de datos")
print(type(3))
print(type(10.1))
print(type(2j))
print(type('Asabeneh'))  
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))

# 3
print("Andres")
print("Rodriguez")
print("Uruguay")
print("Something weird")
#4 Write an example for different Python
#  data types such as Number(Integer, Float, Complex), 
# String, Boolean, List, Tuple, Set and Dictionary.

# Integer: 1
# Float: 2.3
# Complex: 2j
# String: "Hola"
# Boolean: True
# List: [1,2,3]
# Tuple: (10,20, "Banana" )
# Set: {1,2,2,3,3} 
# Dictionary: {"name": "Andres", "apellido": "Rodriguez", "position": 1}

# Example of different Python data types

# Number Types
integer_num = 1  # Integer
float_num = 2.3  # Float
complex_num = 2j  # Complex Number

# String Type
string_value = "Hola"

# Boolean Type
bool_value = True  # Boolean (Can be True or False)

# List Type (Mutable, Ordered Collection)
list_example = [1, 2, 3]

# Tuple Type (Immutable, Ordered Collection)
tuple_example = (10, 20, "Banana")

# Set Type (Unordered, Unique Elements)
set_example = {1, 2, 2, 3, 3}  # Duplicate values are automatically removed

# Dictionary Type (Key-Value Pairs)
dict_example = {
    "name": "Andres",  # Keys should be in quotes
    "apellido": "Rodriguez",
    "position": 1
}

# Output Examples
print("Integer:", integer_num)
print("Float:", float_num)
print("Complex:", complex_num)
print("String:", string_value)
print("Boolean:", bool_value)
print("List:", list_example)
print("Tuple:", tuple_example)
print("Set:", set_example)
print("Dictionary:", dict_example)

# Find an Euclidian distance between (2, 3) and (10, 8)

x1, y1 = 2,3
x2, y2 = 10,8

distance= math.sqrt((x2 - x1)**2+(y2-y1)**2)
print("Distancia euclidiana", distance)
