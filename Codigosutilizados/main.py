# Ejemplo Introducción
print(10 / 2)

-----

# Ejemplos de tipos de excepciones

# Esto genera ZeroDivisionError
resultado = 100 / 0

# Esto genera ValueError
numero = int("veinticinco")  # No se puede convertir

# Esto genera NameError
print(edad)  # Nunca definimos 'edad' antes

# Esto genera TypeError
resultado = "2" + 2  # Texto + número

# Esto genera IndexError
colores = ["rojo", "verde", "azul"]
print(colores[10])  # Solo hay hasta el índice 2

-----

# Ejemplo de uso de else

try:
    # Forzamos una excepción al dividir entre 0
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en except, ha ocurrido una excepción

try:
    # La división puede realizarse sin problema
    x = 2/2
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en else, no ha ocurrido ninguna excepción

-----

# Ejemplo uso de raise

edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
