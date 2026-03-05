numero1 = int(input("Número 1 : "))
numero2 = int(input("Número 2 : "))
operacion = input("Ingrese operación(+ - x /): ")

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "x":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operación no válida...")
    exit()
    
print(f"{numero1} {operacion} {numero2} = {resultado}")