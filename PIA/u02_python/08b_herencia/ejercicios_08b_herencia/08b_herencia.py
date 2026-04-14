#EJERCICIO1
print('\nEJERCICIO 1: FIGURA GEOMETRICA\n')

import math

class FiguraGeometrica:
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

    '''
    def imp_detalles(self):
        print(f'\nAREA: {self.calcular_area()}')
        print(f'\nPERIMETRO: {self.calcular_perimetro()}\n')
    '''
    def __str__(self):
        return 'AREA: '+str(self.calcular_area())+'\nPERIMETRO: '+str(self.calcular_perimetro())
       


class Circle(FiguraGeometrica):
    def __init__(self,radio):
        self.radio=radio

    def calcular_area(self):
        super().calcular_area()
        self.area= math.pi * (self.radio)**2

        return self.area

    #2*pi*r
    def calcular_perimetro(self):
        super().calcular_perimetro()
        self.perimetro = (2* math.pi)* self.radio

        return self.perimetro


class Rectangle(FiguraGeometrica):
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto

    #ancho * alto
    def calcular_area(self):
        super().calcular_area()
        self.area= self.ancho * self.alto

        return self.area

    def calcular_perimetro(self):
        super().calcular_perimetro()
        self.perimetro=(self.ancho*2) + (self.alto*2)

        return self.perimetro


class Triangle(FiguraGeometrica):
    def __init__(self,base,altura,ladoA,ladoB,ladoC):
        self.base=base
        self.altura=altura
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC
        
    #(base *altura) /2
    def calcular_area(self):
        super().calcular_area()
        self.area= (self.base * self.altura) /2

        return self.area
        
    
    #suma de los 3 lados
    def calcular_perimetro(self):
        super().calcular_perimetro()
        self.perimetro=self.ladoA + self.ladoB + self.ladoC

        return self.perimetro

circ1=Circle(5)

rect1=Rectangle(8,4)

trian1=Triangle(3,4,3,4,5)


print(f'\nRADIO CICULO: {circ1.radio}')
print(f'\nAREA CIRCULO: {circ1.calcular_area()}')
print(f'\nPERIMETRO CIRCULO: {circ1.calcular_perimetro()}')

print(f'\nAREA RECATNGULO: {rect1.calcular_area()}')
print(f'\nPERIMETRO RECTANGULO: {rect1.calcular_perimetro()}')     

print(f'\nAREA TRIANGULO: {trian1.calcular_area()}')
print(f'\nPERIMETRO TRIANGULO: {trian1.calcular_perimetro()}')        

#circ1.imp_detalles()

print(circ1)


print('-----<>-----')

#EJERCICIO 2
print('\nEJERCICIO 2: EMPLEADOS\n')

class Empleado():
    def obtener_informacion(self):
        pass

    def calcular_sueldo(self):
        pass


class EmpleadoContratado(Empleado):
    def __init__(self,nombre,puesto,salario):
        self.nombre=nombre
        self.puesto=puesto
        self.salario=salario

    def obtener_informacion(self):
        super().obtener_informacion()
        self.detalles=[]
        
        self.detalles.append(self.nombre)
        self.detalles.append(self.puesto)
        self.detalles.append(self.salario)
            
        return self.detalles


    def calcular_sueldo(self):
        super().calcular_sueldo()
        self.sueldo= self.salario * 1.10

        return self.sueldo



class EmpleadoExterno(Empleado):
    def __init__(self,nombre,puesto,horas,sueldoHora):
        self.nombre=nombre
        self.puesto=puesto
        self.horas=horas
        self.sueldoHora=sueldoHora

    def obtener_informacion(self):
        super().obtener_informacion()
        self.detalles=[]

        self.dic={}
        self.dic['nombre']=self.nombre
        self.dic['puesto']=self.puesto
        self.dic['horas']=self.horas
        self.dic['sueldoHora']=self.sueldoHora

        if self.sueldo:
            self.dic['sueldo']=self.sueldo

        return self.dic
        
        '''
        self.detalles.append(self.nombre)
        self.detalles.append(self.puesto)
        self.detalles.append(self.horas)
        self.detalles.append(self.sueldoHora)

        if self.sueldo:    
            self.detalles.append(self.sueldo)
            
        return self.detalles
        '''
        

    def calcular_sueldo(self):
        super().calcular_sueldo()
        self.sueldo= self.sueldoHora * self.horas

        return self.sueldo

empl1=EmpleadoContratado('pepe','it',1500)

empl2=EmpleadoExterno('lola','consultora',15,200)

print(empl2.calcular_sueldo())

print(empl1.obtener_informacion())

print(empl2.obtener_informacion())
