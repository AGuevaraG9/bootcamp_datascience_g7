tasacambio = 3
opcion = 0

print("=============================================")
print("=========== CONVERTIDOR DE MONEDAS ==========")
print("=============================================")
print("[1] CONVERTIR SOLES A DOLARES")
print("[2] CONVERTIR DOLARES A SOLES")
print("[3] SALIR")
print("=============================================")

while(opcion != 3):
    opcion = int(input("Ingrese la opcion que desea: "))
    if (opcion == 1):
        cantidad = int(input("Ingrese la cantidad en soles : "))
        cambio = cantidad / tasacambio
        print(f"Los {cantidad} soles son al cambio {cambio} dólares")
    elif (opcion == 2):
        cantidad = int(input("Ingrese la cantidad en dólares : "))
        cambio = cantidad * tasacambio
        print(f"Los {cantidad} dóalres son al cambio {cambio} soles")
    elif (opcion == 3):
        print("Gracias por usar este convertidor, adiós!")
        break
    else:
        print("Ingrese una opción válida")
        continue
        
