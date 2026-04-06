#PADRE
class Stack:
    def __init__(self):
        self.__pila=[]

    def __str__(self):
        self.__str=f"OBJETO: {self.__pila}"

        return self.__str
        

    def push(self,elemento):
        self.elemento= elemento
        self.__pila.append(self.elemento)

        return self.__pila


    def pop(self):
        if not self.__pila:
            raise QueueError("Objeto vacío")
        else:
            self.__primero=self.__pila[0]
            self.__pila.pop()
            
            return self.__primero


#HIJO
class AddStack(Stack):
    
    def __init__(self):
        super().__init__()
        self.contador=0

    def get_sum(self):
        return self.contador

    def push(self,elemento):
        super().push(elemento)

        self.contador+=elemento

    def pop(self,elemento):
        super().pop(elemento)

        self.contador-=elemento


obj=AddStack()
print(obj)

obj.push(7)
print(obj)

obj.push(3)

print(obj.get_sum())
