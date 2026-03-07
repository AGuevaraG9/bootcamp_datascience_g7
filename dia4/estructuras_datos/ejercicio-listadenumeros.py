numeros = []

for i in range(5):
    numero = input(f'Ingrese el número {i+1}: ')
    numeros.append(numero)
    
print(f'Los números ingresados son {numeros}')

mayor = numero[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
        
print(f'El mayor es {mayor}')

menor = numero[0]
for numero in numeros:
    if numero < menor:
        menor = numero
        
print(f'El menor es {menor}')

numerosOrdenados = numeros

for i in range(len(numerosOrdenados)):
    for j in range(len(numerosOrdenados) - 1):
        if numerosOrdenados[j] < numerosOrdenados[j+1]:
            numerosOrdenados[j], numerosOrdenados[j+1] = numerosOrdenados[j+1], numerosOrdenados[j]
            
print(f'Lista ordenada : {numerosOrdenados}')