import person

titular = person.Person( "Andres", 55)
titular.saludar()
titular.mostrar_edad()

import string

# 1. Entrada del usuario
frase = input("Escribí una frase: ").lower()

# 2. Eliminar signos de puntuación
for caracter in string.punctuation:
    frase = frase.replace(caracter, "")

# 3. Lista de palabras ignoradas (stopwords)
stopwords = ["el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una", "que", "con", "por", "para", "es"]

# 4. Separar palabras
palabras = frase.split()

# 5. Contar palabras, ignorando stopwords
conteo = {}
for palabra in palabras:
    if palabra not in stopwords:
        conteo[palabra] = conteo.get(palabra, 0) + 1

# 6. Mostrar resultados
print("\n📊 Frecuencia de palabras (sin stopwords ni signos):")
for palabra in sorted(conteo):
    print(f"{palabra}: {conteo[palabra]}")

# 7. Mostrar totales
total_distintas = len(conteo)
total_palabras = sum(conteo.values())
print(f"\n🔢 Total palabras distintas: {total_distintas}")
print(f"🔁 Total palabras (repetidas incluidas): {total_palabras}")
print(type(total_distintas))

def funcion():
    pass

print(funcion())