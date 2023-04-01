#Control de flujo, if
password = True
if password == True:
    print("Ingresado correctamente!")
else:
    print("Ingrese contraseña válida...") 

numero = 6
if numero > 0:
    print("Es positivo.")
elif numero < 0:
    print("Es negativo.")
elif numero == 0:
    print("Es cero")

#Veremos un bucle.
edad = 6
while edad < 18:
    edad = edad + 1
    print("Tienes "+ str(edad))  

#Ponemos un if dentro de la función como filtro de un sitio web.
def ingresarAlSitio (edad):
    if edad >= 18:
        print("Puede ingresar la sitio web.")
    else:
        print("No puede ingresar al sitio web.")   

ingresarAlSitio(edad)         


#Bucle for...in lo usaremos para recorrer una lista.
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)

#Ahora ponemos el bucle dentro de una funcion.
def iterador(lista):
    for elemento in lista:
        print(elemento)  

iterador(secuencia)          