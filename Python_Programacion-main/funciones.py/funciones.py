
#definir funcion saludar
#def saludar(nombre):
#    print(f"buen dia estimado(a) {nombre}")
#saludar("cristian taibo")
#
#nombre = input("ingrese su nombre: ")
#saludar(nombre)
#
#definir funcion sumar
#def suma(a,b):
#    resultado = a + b
#    print(f"el resultado de sumar {a} + {b} = {resultado}")
#
#numero_1 = int (input("ingrese su primer numero: "))
#numero_2 = int (input("ingrese su segundo numero: "))
#
#suma(numero_1,numero_2)


numero_1 = float (input("ingrese su primer numero: "))
operar =   (input("ingrese su operacion: "))
numero_2 = float (input("ingrese su segundo numero: "))

#  
#  #definir calculadora
#  def calculadora(a,b,op):
#      resultado = 0
#      if op == "+":
#          resultado = a + b
#      elif op == "*":
#          resultado = a * b
#      elif op == "-":
#          resultado = a - b
#      else:
#          if numero_2 == 0:
#              print("numero no valido")
#              #return se usa para salir del ciclo
#              return
#          else:
#              resultado = a/b
#  
#      print(f"el resultado de {a}{op}{b} = {resultado}")
#  
#  
#  calculadora(numero_1,numero_2,operar)

#definir variables
numero_1 = float(input("ingrese su primer numero: "))
#crear funcion
def area(a):
    resultado = a * a
    print(f"el area es {a} * {a} = {resultado}")

#llamar funcion
area(numero_1)