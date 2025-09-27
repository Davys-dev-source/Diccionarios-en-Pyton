def crear_diccionario():
    """Crea un diccionario con datos ingresados por el usuario"""
    return {
        "nombre": input("Ingrese su nombre: "),
        "edad": int(input("Ingrese su edad: ")),
        "ciudad": input("Ingrese su ciudad: "),
        "profesion": input("Ingrese su profesión: ")
    }

def actualizar_ciudad(dic):
    nueva_ciudad = input("Ingrese una nueva ciudad para actualizar: ")
    dic["ciudad"] = nueva_ciudad

def actualizar_profesion(dic):
    nueva_profesion = input("Ingrese una nueva profesión: ")
    dic["profesion"] = nueva_profesion

def verificar_telefono(dic):
    if "telefono" not in dic:
        dic["telefono"] = input("Ingrese un número de teléfono: ")

def eliminar_edad(dic):
    if "edad" in dic:
        del dic["edad"]

def main():
    # Crear diccionario inicial
    informacion_personal = crear_diccionario()
    
    print("\nDiccionario inicial:")
    print(informacion_personal)
    
    # Operaciones
    actualizar_ciudad(informacion_personal)
    actualizar_profesion(informacion_personal)
    verificar_telefono(informacion_personal)
    eliminar_edad(informacion_personal)
    
    print("\nDiccionario final:")
    print(informacion_personal)

# Ejecutar el programa
if __name__ == "__main__":
    main()

