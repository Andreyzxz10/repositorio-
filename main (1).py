import os
while True:
    print("bienvenidos al menu principal")
    print ("1.operadores \n""2.condicionales \n""3.ciclos \n")
    choice=int(input("ingresar el numero\n"))
    os.system("clear")
    if choice == 1 :
      choice = 1
      while choice != 99:
        print("1.vamos a hallar el area de un triangulo \n""2.vamos a sumar dos numeros\n""3.elevar un numero al cuadrado \n""4.vamos a convertir euros a dolares\n""5.vamos a hallar el area y perimetro de un cuadrado\n""6.vamos a hallar el area y volumen de un cilindro\n""7.circunferencia y longitud de un circulo\n""8. hallar el promedio de tres numeros\n""99.volver al menu principal")
        choice=int(input("ingresar el numero\n"))
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
          dolar = 1.05
          conver = euro*dolar 
          print ("el valor en dolares es: " ,conver)
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
          print("area y volumen de un cilindro")
          radio = int(input("ingresar el radio del circulo: \n"))
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
          n4 = input("Enter para continuar")
          os.system("clear")
    if choice == 2 :
      choice = 2
      while choice != 99:
        print("1.??el numero es positivo o negativo? \n""2.??cual es el numero mayor y menor?\n""3.programa que lea tres n??meros enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos\n""4.sumarlos si A es menor que B o sino restarlos\n""5.encontrar el cociente entre dos numero \n""6.sumar los numeros si al menos uno de ellos es negativo, en caso contrario multiplicarlos\n""7.??el a??o es biciesto?\n""99.volver al menu principal\n" )
        choice=int(input("ingresar el numero\n"))
        if choice == 1:
          print("??el numero es positivo o negativo?")
          a = int(input("ingrese el primer numero: \n"))
          b = 0
          if a < b:
            print ("negativo")
          elif a > b:
            print ("positivo")
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 2 :
          print("cual es el numero mayor y menor")
          x = int(input("ingrese el primer numero \n"))
          y = int(input("ingrese el segundo numero \n"))
          if x>y:
            print (x,"es mayor que ",y)
          else: 
              print (y, "es mayor que ",x)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 3 :
          print ("Escriba un programa que lea tres n??meros enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos")
          n1= int(input("ingrese el primer numero \n"))
          n2= int(input("ingrese el segundo numero \n"))
          n3= int(input("ingrese el tercer numero \n"))
          if  n2 < n1 > n3: 
            print ("el numero mayor es:",n1)
          elif n1 < n2 > n3:
            print ("el numero mayor es:",n2)
          elif n2 < n3 > n1:
            print ("el numero mayor es:",n3)
          if n2 > n1 < n3: 
            print ("el numero menor es:",n1)
          elif n1 > n2 < n3:
            print ("el numero menor es:",n2)
          elif n2 > n3 < n1:
            print ("el numero menor es:",n3)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 4 :
            print ("Dados dos n??meros A y B, sumarlos si A es menor que B o sino restarlos.")
            a = int(input("ingrese el primer numero: \n"))
            b = int(input("ingrese el segundo numero: \n"))
            if a < b : 
              x = a + b
              print("la suma es igual a:" ,x)
            else:
              z = a - b
              print("la resta es igual a:" ,z)
            n4 = input("Enter para continuar")
            os.system("clear")
        if choice == 5 :
          print ("Dados dos n??meros A y B encontrar el cociente entre A y B. Recordar que la divisi??n por 0 no est?? definida, en ese caso debe aparecer una leyenda anunciando que la divisi??n no es posible.")
          a = int(input("ingrese el primer numero: \n"))
          b = int(input("ingrese el segundo numero: \n"))
          if b == 0: 
            print ("no se puede realizar la division")
          else: 
            cociente = a / b
            print ("el cociente es igual a: ",int(cociente))
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 6 : 
            print ("Dados dos n??meros A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos")
            a = int(input("ingrese el primer numero: \n"))
            b = int(input("ingrese el segundo numero: \n"))
            if a <= 0 or b <= 0:
              suma = a + b
              print ("la suma es igual a: ",int(suma))
            else:
              producto = a * b 
              print("la multiplicacion es igual: ", producto)
            n4 = input("Enter para continuar")
            os.system("clear")
        if choice == 7 :
          print ("Escribir un algoritmo que determine si un a??o es bisiesto o no.")
          a = int(input("ingrese el a??o por favor: \n"))
          if (a % 4 == 100 != 0) or (a % 400 == 0):
            print ("el a??o",a,"es bisiesto")
          else:
            print("el a??o",a,"no es bisisesto")
          n4 = input("Enter para continuar")
          os.system("clear")
    if choice == 3 :
      choice = 3
      while choice != 99:
        print("1.multiplos de 3 que hay en 1 y 100\n""2.n??meros impares entre 0 y 100\n""3.n??meros pares del 1 al 100 \n""4.numeros al cuadrado de 1 a 30\n""5.suma de los cuadrados de los cien primeros n??meros naturales\n""6.mostrar todos los n??meros comprendidos entre ellos en secuencia\n""7.Sumar todos los n??meros que se digitan por teclado mientras no sea cero\n")
        choice=int(input("ingresar el numero\n"))
        if choice == 1 :
          print ("Imprimir todos los m??ltiplos de 3 que hay entre 1 y 100.")
          for i in range(1,101):
            if i % 3 == 0:
              print("los multiplos de 3 de 1 a 100 son:",i) 
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 2 :
          print("Imprimir los n??meros impares entre 0 y 100.")
          for i in range(0,101):
             if i % 2 != 0:
              print("los numero impares son:",i)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 3 :
          print("Imprimir los n??meros pares del 1 al 100")
          for i in range(1,101):
             if i % 2 == 0:
              print("los numeros pares son:",i)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 4 : 
          print("numeros al cuadrado de 1 a 30")
          for i in range(1,31):
              i = i**2 
              print("los numeros son",i)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 5 :
          print("suma de los cuadrados de los cien primeros n??meros naturales")
          suma = 0
          for i in range(1,101):
            suma = suma + i**2
            print("la suma es igual a:",suma)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 6 : 
          print ("Dados dos n??meros naturales, el primero menor que el segundo, generar y mostrar todos los n??meros comprendidos entre ellos en secuencia ascendente.")

          a = int(input("ingrese el numero menor \n"))
          b = int(input("ingrese el numero mayor \n"))   

          for i in range(a,b):
            print("el rango es",i)
          n4 = input("Enter para continuar")
          os.system("clear")
        if choice == 7 :
          print("Sumar todos los n??meros que se digitan por teclado mientras no sea cero")
          suma = 0
          while True:
            n = int(input("ingrese los numero por favor\n"))
            if n != 0 :
              suma = n + suma 
            else:  
              print ("la suma es igual a",suma)
              break
          n4 = input("Enter para continuar")
          os.system("clear")
            
            
