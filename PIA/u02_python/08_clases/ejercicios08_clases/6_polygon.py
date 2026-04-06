import math

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.__x=x
        self.__y=y
        
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self,x,y):
        self.x=x
        self.y=y
        
        #print(self.__x)

        self.xF=self.__x - x
        self.yF=self.__y - y

        self.distancia= math.hypot(abs(self.xF),abs(self.yF))

        return self.distancia

    
    def distance_from_point(self,point):
        self.point1X=self.__x
        self.point1Y=self.__y

        self.point2X=point.__x
        self.point2Y=point.__y

        '''
        print(self.__x)
        print(self.point1X)

        print(point.__x)
        print(self.point2X)
        print(self.point2Y)
        '''

        self.xF= self.point1X - self.point2X
        self.yF =self.point1Y - self.point2Y

        self.distancia= math.hypot(abs(self.xF),abs(self.yF))

        return self.distancia

        #OPCION B
        #return self.distance_from_xy(point.getx(),point.gety())


#------<>------
class Polygon:
    def __init__(self,*vertices):
        #self.__points=[pointA,pointB,pointC]

        self.__vertices=list(vertices)

        

    def perimeter(self):
        #print(self.__points)
        perimetro =0

        lados=len(self.__vertices)

        #acabar el ultimo tramo del poligono con % (para que vuelva a 0)
        for i in range(lados):
            perimetro+=self.__vertices[i].distance_from_point(self.__vertices[(i+1)%lados])

        return perimetro
       

 
#------<>------
    
poligono = Polygon(Point(0, 0), Point(1, 0), Point(0, 1)) 
print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(1, 0), Point(1,1), Point(0, 1)) 
print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(2, 0), Point(2,1), Point(0, 1)) 
print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(2, 0), Point(1,1), Point(0, 1)) 
print(poligono.perimeter()) 
    
