from fraccion import Fraccion
denaux= 1
while denaux != 0:
    numaux= int(input("enter the numerator of fraction1"))
    denaux= int(input("enter the denominator of fraction1"))

    while denaux== 0:
        print ("the denominator of the fraction cannot be 0, try again")
        numaux= int(input("enter the numerator of fraction1"))
        denaux= int(input("enter the denominator of fraction1"))
    break
fraccion1= Fraccion (numaux,denaux)

denaux2 = 1
while denaux2 != 0:
    numaux2= int(input("enter the numerator of fraction2"))
    denaux2= int(input("enter the denominator of fraction2"))
    
    while denaux2== 0:
        print ("the denominator of the fraction cannot be 0, try again")
        numaux2= int(input("enter the numerator of fraction2"))
        denaux2= int(input("enter the denominator of fraction2"))
    
    break
fraccion2= Fraccion (numaux2,denaux2)


def menu():
    opcion=0
    while opcion < 5:
        print ("fraction 1:",fraccion1.mostrar())
        print ("fraction 2:",fraccion2.mostrar())
        print ("Menu:")
        print ("Choose an option to perform an operation with the previous fractions")
        print ("1-Add fractions")
        print ("2-Subtract fractions")
        print ("3-Multiply fractions")
        print ("4-Divide fractions")
        print ("5-Exit")
        opcion= int(input("What option do you want to choose?"))
        if opcion == 1:
            resultadosuma = fraccion1.sumar(fraccion2)
            print("the sum is:", resultadosuma.mostrar())
        if opcion == 2:
            resultadoresta= fraccion1.restar(fraccion2)
            print("the subtraction is:", resultadoresta.mostrar())
        if opcion == 3:
            resultadomultiplicar= fraccion1.multiplicar(fraccion2)
            print("the multiplication is:", resultadomultiplicar.mostrar())
        if opcion == 4:
            resultadodivision= fraccion1.division(fraccion2)
            print("the division is:", resultadodivision.mostrar())
        if opcion == 5:
            break
    
menu()




    






