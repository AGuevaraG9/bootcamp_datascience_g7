from time import sleep
from src.datos import empresas, guardar_empresas
from src.utils import pausa, titulo, limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresa():
    ruc = input("Ingrese RUC : ")
    razon_social = input("Ingrese la Razón Social : ")
    direccion = input("Ingrese la dirección : ")
    
    empresas[ruc] = {
        "razon_social":razon_social,
        "direccion":direccion
    }
    titulo("EMPRESA REGISTRADA EXITOSAMENTE!")
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_empresas():
    for ruc, info in empresas.items():
        print(f'RUC: {ruc}')
        print(f'RAZON SOCIAL : {info['razon_social']}')
        print(f'DIRECCION : {info['direccion']}')
        print("*" * 50)

@pantalla("ACTUALIZAR EMPRESA")
def actualizar_empresa():
    ruc = input("Ingrese el RUC de la empresa : ")
    
    if ruc in empresas:
        print(f'Empresa encontrada : {empresas[ruc]['razon_social']}')
        print(f'Ingrese los nuevos datos de la empresa o deje en blanco para omitir')
        
        nueva_razon_social = input(f'Nueva Razón Social ({empresas[ruc]['razon_social']}) : ')
        nueva_direccion = input(f'Nueva dirección ({empresas[ruc]['direccion']}) : ')
        
        empresas[ruc]['razon_social'] = nueva_razon_social if nueva_razon_social else empresas[ruc]['razon_social']
        empresas[ruc]['direccion'] = nueva_direccion if nueva_direccion else empresas[ruc]['direccion']
        print('DATOS DE EMPRESA ACTUALIZADOS!')
    else:
        print('EMPRESA NO ENCONTRADA!')
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("Ingrese el RUC de la empresa : ")
    
    if ruc in empresas:
        print(f'Empresa encontrada : {empresas[ruc]['razon_social']}')
        opcion = int(input("Esta seguro de eliminar la empresa? ([1] SI, [2] NO) : "))
        if (opcion == 1):
            del empresas[ruc]
            print("EMPRESA ELIMINADA!")
        elif (opcion == 2):
            pass
        else:
            print("Ingrese una opción válida!")
    else:
        print('EMPRESA NO ENCONTRADA!')
        
def menu_principal():
    while True:
        limpiar()
        titulo("SISTEMA DE GESTIÓN DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESA
            [2] MOSTRAR EMPRESAS
            [3] ACTUALIZAR EMPRESA
            [4] ELIMINAR EMPRESA
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE UNA OPCIÓN : "))
        
        if opcion == 1:
            registrar_empresa()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresa()
            pausa()
        elif opcion == 4:
            eliminar_empresa()
            pausa()
        elif opcion == 5:
            guardar_empresas(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA")
            print("Datos guardados en empresas.csv")
            sleep(2)
            break
        else:
            print("Ingrese una opción válida!")