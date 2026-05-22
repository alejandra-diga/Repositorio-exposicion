MANEJO DE EXCEPCIONES EN PYTHON

# --- Sintaxis básica & Tipos de excepciones comunes ---
print("--- Sintaxis Básica y Excepciones Comunes ---")

try:
    # Intento de operación inválida (Genera un ZeroDivisionError)
    resultado = 10 / 0
except ZeroDivisionError:
    print("Excepción capturada: No se permite la división por cero.")

try:
    # Intento de conversión inválida (Genera un ValueError)
    numero = int("Texto no numérico")
except ValueError:
    print("Excepción capturada: Tipo de dato no válido para la conversión.")


# --- Manejo específico de errores & Uso de try y except ---
print("\n--- Manejo Específico y Uso de try/except ---")

def dividir_valores(a, b):
    try:
        # El bloque 'try' contiene el código que podría fallar
        operacion = a / b
        print(f"Resultado: {operacion}")
    except ZeroDivisionError:
        # Bloque específico para manejar divisiones entre cero
        print("Error específico: El divisor no puede ser cero.")
    except TypeError:
        # Bloque específico por si se envían tipos de datos incorrectos (ej. texto)
        print("Error específico: Ambos argumentos deben ser numéricos.")
    except Exception as error_general:
        # Captura cualquier otra excepción no prevista
        print(f"Error inesperado: {error_general}")

# Pruebas de la función
dividir_valores(10, 2)     # Caso exitoso
dividir_valores(10, 0)     # Detona ZeroDivisionError
dividir_valores(10, "dos") # Detona TypeError


# --- Uso de else & Uso de finally ---
print("\n--- Uso de else y finally ---")

try:
    print("Intentando realizar una operación segura...")
    calculo_valido = 50 / 5
except ZeroDivisionError:
    print("Ocurrió un error en el cálculo.")
else:
    # Se ejecuta UNICAMENTE si el bloque 'try' finalizó con éxito total
    print(f"¡Bloque 'else' ejecutado! El resultado fue exitoso: {calculo_valido}")
finally:
    # Se ejecuta SIEMPRE, sin importar si hubo errores o si se ejecutó el 'else'
    print("Bloque 'finally' ejecutado: Limpiando y cerrando conexiones.")


# --- Uso de raise ---
print("\n--- Uso de raise ---")

def registrar_usuario(edad):
    if edad < 18:
        # 'raise' nos permite forzar el lanzamiento de una excepción propia
        raise ValueError("Acceso denegado: El usuario debe ser mayor de edad.")
    return "Usuario registrado con éxito."

try:
    # Forzamos la ejecución con un dato inválido para ver el comportamiento
    print(registrar_usuario(15))
except ValueError as mensaje_error:
    print(f"Controlado con raise -> {mensaje_error}")
