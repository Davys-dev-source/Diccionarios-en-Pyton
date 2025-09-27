# Diccionario en Python - Datos ingresados por el usuario

# Crear un diccionario vacío
informacion_personal = {}

# Ingresar datos desde el teclado
informacion_personal["nombre"] = input("Ingrese su nombre: ")
informacion_personal["edad"] = int(input("Ingrese su edad: "))
informacion_personal["ciudad"] = input("Ingrese su ciudad: ")
informacion_personal["profesion"] = input("Ingrese su profesión: ")

# Acceder y modificar el valor de la clave "ciudad"
nueva_ciudad = input("Ingrese una nueva ciudad para actualizar: ")
informacion_personal["ciudad"] = nueva_ciudad

# Agregar una nueva clave-valor (profesión actualizada)
nueva_profesion = input("Ingrese una nueva profesión: ")
informacion_personal["profesion"] = nueva_profesion

# Verificar si existe la clave "telefono". Si no existe, agregarla
if "telefono" not in informacion_personal:
    telefono = input("Ingrese su número de teléfono: ")
    informacion_personal["telefono"] = telefono

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
