def saludar(nombre):
    # return f"Hola {nombre}"
    print(f"Hola {nombre}")

nombre_usuario = input("Hola ¿Como te llamas? ")
# print(saludar(nombre_usuario))
saludar(nombre_usuario)

def sumar(a,b):
    return a + b

resultado = sumar(5,3)
print(f'La suma es {resultado}')