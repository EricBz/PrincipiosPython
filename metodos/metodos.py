#En listas:
lista = [1,2,3,4,5]

lista.append(6)
print(lista)

lista.insert(0, 9) #Primero ponemos el index, luego el elemento que quisieramos ingresar.
print(lista)

lista.remove(9)
print(lista)

def sumar(n):
    return n+2

resultado = map(sumar, lista)
print(resultado)

#En diccionarios:
datos = {"name": "Homero", "age": 36, "surname": "Simpson"}
verClaves = datos.keys()
verValor = datos.values()
print(verClaves)
print(verValor)