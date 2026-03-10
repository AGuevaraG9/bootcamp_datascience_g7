# escribir un archivo txt
# permiso: w - write
with open('notas.txt','w') as archivo:
    archivo.write('Hola mundo en mi archivo')
    archivo.write('\n')
    archivo.write('Esta es una clase de python')
    
# leer un archivo
# permiso: r - read
with open('notas.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
print("----- linea por linea -----")
# leer linea por linea
with open('notas.txt','r') as archivo:
    for linea in archivo:
        print("linea: ", linea.strip())
        
# añadir contenido a un archivo txt
# permiso a = append
with open('notas.txt','a') as archivo:
    nueva_linea = input('Escribe una nueva linea : ')
    archivo.write("\n")
    archivo.write(nueva_linea)