import time

def medir_tiempo(funcion):
    
    def wrapper():
        inicio = time.time()
        
        funcion()
        
        fin = time.time()
        
        print("Tiempo: ", fin - inicio)
    
    return wrapper

@medir_tiempo
def saludar():
    print("Hola estudiante")
    
def ejecutar(funcion):
    funcion()
    
ejecutar(saludar)

@medir_tiempo
def proceso_lento():
    print("inicio")
    for i in range(500000000):
        pass
    print('Termino')
    
proceso_lento()