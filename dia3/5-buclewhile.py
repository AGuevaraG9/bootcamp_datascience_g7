contador = 1
while(contador < 10):
    print(contador)
    contador += 1
    
numero_adivinar = 5
print("Adivina el número que estoy pensando!")
while(contador != numero_adivinar):
    contador = int(input())
    if contador == numero_adivinar:
        print("GANASTE!!")
    else:
        print("Intenta otra vez! ")