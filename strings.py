# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
letter_1 = 'Thirty'
letter_2 = 'Days'           
letter_3 = 'Of'
letter_4 = 'Python' 
print(letter_1 + ' ' + letter_2 + ' ' + letter_3 + ' ' + letter_4)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
letter_1 = 'Coding'
letter_2 = "For"
letter_3 = 'All'
print(letter_1 + ' ' + letter_2 + ' ' + letter_3)
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for All"
# Print the variable company using print()
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
to_upper = company.upper()
print(to_upper)
# Change all the characters to lowercase letters using lower() method.
to_lower = company.lower()
print(to_lower)
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalized = company.capitalize() # capitalize the first word Coding for all
title = company.title() # Coding For All
swap_cased = company.swapcase() # cODING FOR aLL
print(capitalized + ' ' + title + ' ' + swap_cased)
# Cut(slice) out the first word of Coding For All string.
sliced = company[0:1] # C
print(sliced)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Find() method
chechked = company.find("Coding")
print(chechked)
#index method
index = company.index('Coding')
print(index)
# Using in operator (best for checking existence):
exist_in = "Coding" in company
print(exist_in) # true
# Replace the word coding in the string 'Coding For All' to Python.
replaced_word = company.replace("Coding", "Python")
print(replaced_word)
# Change Python for Everyone to Python for All using the replace method or other methods
new_logo = replaced_word.replace("Python for All", "Python for Everyone")
print(new_logo) # Python for Everyone
# Split the string 'Coding For All' using space as the separator (split()) .
splitted = company.split()
print(splitted)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

language = 'Pythonn'
a,b,c,d,e,f,g = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
print(e)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = company.split(", ") 
print(companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# What is the character at index 0 in the string Coding For All.
company = "Coding For All"
print(company[0]) # C   
# What is the last index of the string Coding For All.
print(company[-1]) # l
# What character is at index 10 in "Coding For All" string.
print(company[11])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
def new_logo(name="Python For Everyone"):
    words = name.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

acronym = new_logo()
print(acronym)  # Imprime "PFE"

def generar_acronimo():
    while True:
        frase = input("Ingresa una frase para generar un acrónimo: ").strip()
        
        # Validación de cadena vacía o solo espacios
        if frase:
            break
        else:
            print("⚠️ La entrada no puede estar vacía. Intenta nuevamente.\n")

    # División en palabras y generación del acrónimo
    palabras = frase.split()
    acronimo = ''.join(palabra[0].upper() for palabra in palabras if palabra)

    return acronimo

# Ejecutar y mostrar
acronimo = generar_acronimo()
print(f"🔤 Acrónimo generado: {acronimo}")

# Create an acronym or an abbreviation for the name 'Coding For All'
def new_form(name = "Coding For All"):
    words = name.split()
    acronimo = ''.join(word[0].upper() for word in words)
    return acronimo
acronym = new_form()
print(acronym)
# Use index to determine the position of the first occurrence of C in Coding For All.
name = "Coding For All"
print(name.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(name.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(name.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
long_sentence = "You cannot end a sentence with because because because is a conjunction"
print(long_sentence.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(long_sentence.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
start = long_sentence.find('because because because')
end = start + len("because because because")
sliced_phrase = long_sentence[start:end]
print(sliced_phrase)
# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding')) # True
# Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())
# Which one of the following variables return True when we use the method isidentifier():
   # 30DaysOfPython False
   # thirty_days_of_python true

# The following list contains the names of some of python libraries:
#  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list_of = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(list_of))

# Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge. \nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity")
print("Andres\t40\tUruguay\tRivera")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))
# Make the following using string formatting methods:
a = 8
b = 6   
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')       
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')   
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}') 
print(f'{a} ** {b} = {a ** b}')
