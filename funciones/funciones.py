num1 = 2
num2 = 3
operacion = "+"

def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1+num2
    elif operacion == "-":
        return num1-num2
    elif operacion == "*":
        return num1*num2
    elif operacion == "/":
        if num1 > 0 and num2 > 0:
            return num1/num2
        
#Vemos una fn dentro de otra fn.        
def mostrar(num1, num2, operacion, calculadora):
    print(str(calculadora(num1, num2, operacion)))        

mostrar(2, 7, "+", calculadora)

#Funcióm lambda, tiene el return impliscito.
ver = lambda num1, num2, operacion, calculadora : print(str(calculadora(num1, num2, operacion))) 
ver(5,7,"+",calculadora)