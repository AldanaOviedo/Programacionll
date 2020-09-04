class Fraccion:
    def  __init__ (self,num,den):
        self.numerador= num
        self.denominador = den


    def __init__(fraccion2, numerador, denominador):
        fraccion2.numerador= numerador
        fraccion2.denominador= denominador

    def mostrar (self):
        return str(self.numerador)+ "/" +str(self.denominador)
        


    def sumar (self, fraccion2):
        resultado = Fraccion( 1 , 1 )
        
        resultado.numerador = self.numerador * fraccion2.denominador + self.denominador * fraccion2.numerador
        resultado.denominador = self.denominador * fraccion2.denominador
        
        return resultado

    def restar (self, fraccion2):
        resultado= Fraccion (1,1)

        resultado.numerador = self.numerador * fraccion2.denominador - self.denominador * fraccion2.numerador
        resultado.denominador= self.denominador * fraccion2.denominador

        return resultado

    def multiplicar (self, fraccion2):
        resultado= Fraccion (1,1)

        resultado.numerador= self.numerador * fraccion2.numerador
        resultado.denominador= self.denominador * fraccion2.denominador

        return resultado

    def division (self, fraccion2):
        resultado = Fraccion(1,1)

        resultado.numerador = self.numerador * fraccion2.denominador
        resultado.denominador = self.denominador * fraccion2.numerador

        return resultado



    
