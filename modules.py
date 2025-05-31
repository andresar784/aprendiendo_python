import random
import string
# Write a function which generates a six digit/character random_user_id. 
def random_user_id():
    caracteres = string.ascii_letters + string.digits
    user_id = "".join(random.choices(caracteres, k=10))
    return user_id
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). One of the
# inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    number_of_characterers = int(input("Ingrese el numero de parametros: "))
    ids_to_be_generated = int(input("Numero de ids necesarias?: "))
    caracteres = string.ascii_letters + string.digits
    ids = []
    for i in range(ids_to_be_generated):
        user_id = "".join(random.choices(caracteres, k=number_of_characterers))
        ids.append(user_id)

    for user_id in ids:
      print(user_id)
    
user_id_gen_by_user()

# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255) 
    g = random.randint(0, 255) 
    b = random.randint(0, 255) 
    color = (r,g,b)
    return print(f"RGB {color}")

rgb_color_gen()

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is
# made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n=1):
    colors = []
    hexdigits = "0123456789abcdef"
    for i in range(n):
        color = "#" + "".join(random.choices(hexdigits, k=6))
        colors.append(color)
    print(colors)

list_of_hexa_colors(5)

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array
def list_of_rgb_colors(n):
    colors = []
    for _ in range(2):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = f"rgb({r},{g},{b})"
        colors.append(rgb)
    print(colors)
list_of_rgb_colors(2)

# Write a function generate_colors which can generate
#  any number of hexa or rgb colors.
def generate_colors(color_type , n):
    colors = []
    for _ in range(n):
        if color_type == 'hexa':
            hex_digits = '0123456789abcdef'
            for _ in range(n):
                color = '#' + ''.join(random.choices(hex_digits, k=6))
                colors.append(color)
        elif color_type == 'rgb':
            for _ in range(n):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = f'rgb({r},{g},{b})'
                colors.append(color)
        else:
            raise ValueError("Tipo de color no válido. Usa 'hexa' o 'rgb'.")
    return colors

print(generate_colors("rgb" , 2))
# Call your function shuffle_list,
# it takes a list as a parameter and it returns a shuffled list
lista = [1,2,3,56,3, "Batatas"]
def shuffle_list(list):
    lista_copy = list [:]
    random.shuffle(lista_copy)
    return lista_copy

print(shuffle_list(lista))

# Write a function which returns an array of 
# seven random numbers in a range of 0-9. All the numbers must be unique.
def randon_number():
    return random.sample(range(10), 7)

print(randon_number())