# Create an empty tuple
empty_tuple = ()
print(empty_tuple)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother = ("Andres", "Lolo")
sisters = ("Laura", "Lala")
# Join brothers and sisters tuples and assign it to siblings
sons = brother + sisters
print(sons) # ('Andres', 'Lolo', 'Laura', 'lala')
# How many siblings do you have?
print(len(sons)) # 4
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
fathers = ("Toto", "Lala")
family_members = sons + fathers
print(family_members)
# Unpack siblings and parents from family_members
fathers_ = family_members[4:6]
print(fathers_) # ('Toto', 'Lala')
# Create fruits, vegetables and animal products tuples.  
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Papas","Tomates","Peras")
vegetables = ("Batatas", "Nueces")
animal_products = ("Carne", "Higados", "Tripas")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp) # ('Papas', 'Tomates', 'Peras', 'Batatas', 'Nueces', 'Carne', 'Higados')
# Change the about food_stuff_tp tuple to a  list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) # ['Papas', 'Tomates', 'Peras', 'Batatas', 'Nueces', 'Carne', 'Higados']
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Obtener la longitud de la tupla
length = len(food_stuff_tp)

# Verificar si la longitud es par o impar
if length % 2 == 0:
    # Si es par, extraer los dos elementos del medio usando slicing
    middle_item = food_stuff_tp[length // 2 - 1 : length // 2 + 1]
else:
    # Si es impar, extraer solo el elemento del medio
    # Se pone una coma para que el resultado sea una tupla de un solo elemento
    middle_item = (food_stuff_tp[length // 2],)

# Imprimir el/los elemento(s) del medio
print(middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three) # ['Papas', 'Tomates', 'Peras']
print(last_three) # ['Carne', 'Higados', 'Tripas']
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp)
#
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries) # False
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries) # True