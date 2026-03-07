numeros = []

for i in range(5):
    numero = input(f'Ingrese el número {i+1}: ')
    numeros.append(numero)
    
print(f'Los números ingresados son {numeros}')

mayor = max(numeros)
print(f'El mayor es {mayor}')

menor = min(numeros)        
print(f'El menor es {menor}')

numerosOrdenados = sorted(numeros, reverse=True)            
print(f'Lista ordenada : {numerosOrdenados}')