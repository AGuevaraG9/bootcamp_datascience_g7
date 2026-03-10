def operaciones(a,b):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    def multiplicacion(a,b):
        return a * b
    def division(a,b):
        return a/b
    
    print(f"suma: {suma(a,b)}")
    print(f"resta: {resta(a,b)}")
    print(f"multiplicacion: {multiplicacion(a,b)}")
    print(f"division: {division(a,b)}")
    
operaciones(10,5)

#funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    else: return n * factorial(n-1)
    
print(f"Factorial de 5: {factorial(5)}")

#funciones como parametro de otra funcion
def aplicar_funcion(func, valor):
    return func(valor)

doblar = lambda x: x * 2
resultado = aplicar_funcion(doblar,5)
print(f'Resultado de aplicar funcion {resultado}')
