# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Pluma", "color":"Blanca" , "breed": "Caniche", "legs":"4" , "age":2 }
# Create a student dictionary and 
# add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Andres",
    "last_name": "Rodriguez", 
    "gender":"Male", 
    "age": 44,
    "marital_status": "Married",
    "skills": [
        "Html",
        "CSS",
        "Javascript"
    ],
    "Country": "Uruguay",
    "City":"Rivera",
    "adress": "Blanes 2491"
    }
# Get the length of the student dictionary
print(len(student)) # 9

# Get the value of skills and check the data type, it should be a list
student_skills = student.get("skills")
print(student_skills) # ('Html', 'CSS', 'Javascript')

# Modify the skills values by adding one or two skills
student["skills"].append("Python")
student["skills"].append("IBM")
student_skills = student.get("skills")
print(student_skills) 

# Get the dictionary keys as a list
keys = student.keys()
print(f"Las keys en students son {keys}")
# print(type(student_skills))
# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
student_tuple = tuple(student.items()) 
print(student_tuple)
# print(type(student_tuple))
for clave, valor in student_tuple:
    print(f"Clave: {clave}, Valor: {valor}" )

""" 
Clave: first_name, Valor: Andres
Clave: last_name, Valor: Rodriguez
Clave: gender, Valor: Male
Clave: age, Valor: 44
Clave: marital_status, Valor: Married
Clave: skills, Valor: ['Html', 'CSS', 'Javascript', 'Python', 'IBM']
Clave: Country, Valor: Uruguay
Clave: City, Valor: Rivera
Clave: adress, Valor: Blanes 2491

"""
# Delete one of the items in the dictionary
student.pop("age")
print(student)
# Delete one of the dictionaries
del student