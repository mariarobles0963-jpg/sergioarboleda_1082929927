edad = 17
if edad >= 18:
    print("Eres mayor de edad.")
else:   print("Eres menor de edad.")

#BUCLE FOR 
for i in range(5):
    print("hola mundo")

    #WHILE
contador = 1
while contador <= 5:
    print("numero: " + str(contador))
    contador = contador + 1

    for i in range(0, 12, 3):
     print ("numero: " + str(i))

encontrado = False
numerobuscado = 6
numeros = [1, 3, 5, 7, 9]
for numero in numeros:
    if numero == numerobuscado:
        encontrado = True
        break
    print("Numero" ,numerobuscado, "encontrado:", encontrado)

    for i in range(1, 4):
        for j in range(1, 4):
            print("i:" + str(i) + " j:" + str(j))