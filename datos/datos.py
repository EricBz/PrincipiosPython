#Esto es un comentario...
#PRACTICA INICIAL PRINCIPIOS DE PYTHON.
cadena = "hola es una cadena."
print(cadena)
mostrarTipo = type(cadena)
print(mostrarTipo)
numero = 29
booleano = True
print(type(numero))
print(type(booleano))

#lista
lista = [1,2,3,4,5]
print(type(lista))
print(lista)
#Para ver el numero deberemos pasarlo a string, esto lo haremos con la fn str().
print("Este es un elemento en la lista, el numero: "+str(lista[2]))

#tupla
tupla = (1,2,3,4,5)
print(type(tupla))
print(tupla)

#Diccionarios, son como un json.
diccionario = {"name": "Apu"}
print(type(diccionario))
print(diccionario)


#Es una función, pero lo veremos en profundidad un poco después.
entrada = "Primer entrada..."
def mostrar(entrada):
    print(entrada)

mostrar(entrada)    