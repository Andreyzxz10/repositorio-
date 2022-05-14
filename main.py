import os
while True:
    print("bienvenidos al menu principal")
    print ("1.operadores \n")
    choice=int(input("ingresar el numero"))
    os.system("clear")
    if choice == 1 :
      choice = 1
      while choice != 99:
        print("1.vamos a hallar el area de un triangulo \n""2.vamos a sumar dos numers\n""3.elevar un numero al cuadrado \n""4.vamos a convertir euros a dolares\n""5.vamos a hallar el area y perimetro de un cuadrado\n""6.vamos a hallar el area y volumen de un cilindro\n""7.circunferencia y longitud de un circulo\n""8. hallar el promedio de tres numeros\n""99.volver al menu principal")
        choice=int(input("ingresar el numero"))
        if choice == 1:   
          print("el area de un trigangulo")
          base = int(input ("ingrese la base \n"))
          altura = int(input("ingrese la altura \n"))
          area = base * altura 
          print("el area es: " + str(area))
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 2 :
          print ("vamos a sumar dos numeros")
          num1 = int(input("ingrese el numero 1\n"))
          num2 = int(input("ingrese el numero 2\n"))
          s = num1 + num2
          print ("la sumatoria es: ", s)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 3 :
          print("vamos a elevar un numero al cuadrado\n")
          numero=float(input("ingresar el numero: "))
          n = numero**2
          print ("el numero elevado al cuadrado es: ", n)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 4 :
          print("vamos a convertir los euros a dolares")
          euro = int(input("ingresar la cantida de euros: \n"))
          dolar = 4000
          conver = euro*dolar 
          print ("el valor en dolares es: " ,conver,)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 5 :
          print ("escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del area y del perimetro \n")
          lado = int(input("ingrese el lado del cuadrado \n"))
          area = lado**2  
          print ("el area es: ",area,)
          perimetro = lado + lado + lado + lado
          print ("el perimetro es = ",perimetro)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 6 :
           print("escribir un algoritmo que pida el lado de un cilindro y muestre el valor del volumen y area de un cilindro \n")
          radio = int(input("ingresar el radio del circulo: \n"
                           )
          altura = int(input("ingresar la altura del cilindro: \n"))
          volumen = 3.14 * radio **2 * altura
          print("el volumen del cilindro es: ",volumen)
          area = 2 * 3.14 * radio**2 + 2 * 3.14 * radio * altura
          print ("el area del cilindro es: ",area)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 7:
          print("circunferencia y longitud")
          perimetro = int(input("ingresar el valor del perimetro de la circunferencia: \n"))
          radio = perimetro / 2*3.14
          print ("el radio de una circunferencia es: ",radio)
          area = 3.14 * radio**2
          print ("el area del circulo es: ",area)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 8:
          print ("calcula el promedio de 3 numeros")
          numero1 = int(input("ingrese el valor del primer numero : "))
          numero2 = int(input("ingrese el valor del segundo numero : ")) 
          numero3 = int(input("ingrese el valor del tercer numero : ")) 
          promedio = (numero1 + numero2 + numero3) / 4
          print ("el valor del proedio es de: ",promedio)


#a = int(input("ingrese el primer numero: \n"))
#b = 0
#if a < b:
  #print ("negativo")

#elif a > b:
  #print ("positivo")

#print ("algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor")
#x = int(input("ingrese el primer numero \n"))
#y = int(input("ingrese el segundo numero \n"))
#if x>y:
  #print (x,"es mayor que ",y)
#else: 
  #print (y, "es mayor que ",x)

#print ("Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos")
#n1= int(input("ingrese el primer numero \n"))
#n2= int(input("ingrese el segundo numero \n"))
#n3= int(input("ingrese el tercer numero \n"))
#if  n2 < n1 > n3: 
  #print ("el numero mayor es:",n1)
#elif n1 < n2 > n3:
  #print ("el numero mayor es:",n2)
#elif n2 < n3 > n1:
  #print ("el numero mayor es:",n3)
#if n2 > n1 < n3: 
  #print ("el numero menor es:",n1)
#elif n1 > n2 < n3:
  #print ("el numero menor es:",n2)
#elif n2 > n3 < n1:
  #print ("el numero menor es:",n3)

#print ("Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.")

#a = int(input("ingrese el primer numero: \n"))
#b = int(input("ingrese el segundo numero: \n"))

#if a < b: 
  #x = a + b
  #print("la suma es igual a:" ,x)
#else:
 # z = a - b
  #print("la resta es igual a:" ,z)

#print ("Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por 0 no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.")

#a = int(input("ingrese el primer numero: \n")) 
#b = int(input("ingrese el segundo numero: \n"))

#if b == 0: 
  #print ("no se puede realizar la division")
#else: 
  #cociente = a / b
  #print ("el cociente es igual a: ",int(cociente))

#print ("Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos")

#a = int(input("ingrese el primer numero: \n"))
#b = int(input("ingrese el segundo numero: \n"))

#if a <= 0 or b <= 0:
 # suma = a + b
  #print ("la suma es igual a: ",int(suma))
#else:
  #producto = a * b 
  #print("la multiplicacion es igual: ", producto)

#print ("Escribir un algoritmo que determine si un año es bisiesto o no.")

#a = int(input("ingrese el año por favor: \n"))

#if (a % 4 == 100 != 0) or (a % 400 == 0):
  #print ("el año",a,"es bisiesto")
#else:
 # print("el año",a,"no es bisisesto")




#print ("Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")

#for i in range(1,101):
 # if i % 3 == 0:
  #  print("los multiplos de 3 de 1 a 100 son:",i) 

#print("Imprimir los números impares entre 0 y 100.")

#for i in range(0,101):
 # if i % 2 != 0:
  #  print("los numero impares son:",i)

#print("Imprimir los números pares del 1 al 100")
#for i in range(1,101):
 #if i % 2 == 0:
  #  print("los numeros pares son:",i)

#for i in range(1,31):
 # i = i**2 
  #print("los numeros son",i)
  
#print("Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla")
#suma = 0
#for i in range(1,101):
#  suma = suma + i**2
#  print("la suma es igual a:",suma)

#print ("Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente.")

#a = int(input("ingrese el numero menor \n"))
#b = int(input("ingrese el numero mayor \n"))   

#for i in range(a,b):
#    print("el rango es",i)

#print("Sumar todos los números que se digitan por teclado mientras no sea cero")

#a = int(input("ingrese el primer numero: \n"))

#b = int(input("ingrese el segundo numero:  \n"))

#suma = a + b 
#if a > 0 < b:
 # print("la suma es igual a",suma)
#else:
 # print("no se puede sumar")
