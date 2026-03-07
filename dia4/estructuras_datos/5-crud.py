import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
ANCHO = 50

dic_alumnos = {
    '12345678':{
        'nombre':'Juan Perez',
        'email':'juanperez@gmail.com'
    },
    '10010010':{
        'nombre':'Ana Lopez',
        'email':'analopez@gmail.com'
    }
}

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI : ")
        nombre = input("INGRESE NOMBRE : ")
        email = input("INGRESE EMAIL : ")
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email
        }
        dic_alumnos[codigo] = dic_nuevo_alumno
        print("Alumno registrado exitosamente!")
        print("=" * ANCHO)
        
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        
        for codigo, info in dic_alumnos.items():
            print(f"DNI : {codigo}")
            print(f"NOMBRE : {info['nombre']}")
            print(f"EMAIL : {info['email']}")
            print("=" * ANCHO)
        
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
        
        alumno_buscado = input("Ingrese el codigo del alumno : ")
        if alumno_buscado in dic_alumnos:
            nombre = str(input("Ingrese el nuevo nombre : "))
            email = str(input("Ingrese el nuevo email : "))
            dic_alumno_editado = {
                'nombre':nombre,
                'email':email
            }
            dic_alumnos[alumno_buscado] = dic_alumno_editado
            print("Alumno editado exitosamente!")
            print("=" * ANCHO)
        else:
            print("Alumno no encontrado!")
        
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
        
        alumno_buscado = input("Ingrese el codigo del alumno : ")
        if alumno_buscado in dic_alumnos:
            opcion = input("Esta seguro de eliminar al alumno? (si,no) : ")
            if (opcion == "si"):
                dic_alumnos.pop(alumno_buscado)
                print("Alumno eliminado!")
                print("=" * ANCHO)
            elif (opcion == "no"):
                continue
            else:
                print("Ingrese una opción válida!")
        else:
            print("Alumno no encontrado!")
        
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")