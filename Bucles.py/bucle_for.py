#usamos el ciclo for para recorrer elementos de un grupo de datos
juegos = {"dota 2", "MK", "street fighter", "counter strike", "7daystodie"}
numeros = {10,20,30,40,50}

for juego in juegos:
    print(juego)
print ()
for numero in numeros:
    resultado = numero * numero
    print (f"el resultado de multiplicar {numero} * {numero} = {resultado}")

for num in range(5):
    print (num)
    
for num in range(5,15): 
    print (num)    

for num in range(5,15,3):
    print (num)

for elemento in enumerate(numeros):
    indice = elemento[0]
    valor = elemento[1]
    print(f"el indice es: {indice} y el valor es: {valor}")