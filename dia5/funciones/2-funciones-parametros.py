def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))
print(potencia(3,4))

def operaciones(a,b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operaciones(5,3)
print(f'Suma : {resultado_suma}')
print(f'Resta : {resultado_resta}')

def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(sumar_todos(1,2,3))
print(sumar_todos(10,20))

def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'resta':
        return kwargs['a'] - kwargs['b']
    else:
        return 'Operación incorrecta'
    
resultado1 = calculadora(operacion='suma',a=10,b=5)
print(f'Resultado 1 : {resultado1}')
resultado2 = calculadora(operacion='resta',a=10,b=5)
print(f'Resultado 2 : {resultado2}')