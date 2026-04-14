#EJERCICIO 1
print(f'\nEJERCICIOS 1:\n')

from os import strerror

try:
    i=0
    stream=open('p1.txt','rt')

    c=stream.read(1)

    while c != '':
        print(c)
        i+=1
        c=stream.read(1)
    
    stream.close()
    print(f'CONTADOR: {i}')


except IOErros as e:
    print(strerror(e.errno))

print('-----<>-----')


#EJERCICIO 2
print(f'\nEJERCICIOS 2:\n')

try:
    i=0
    with open('p1.txt','rt') as s:
        a=s.read()

        while a != '':
            print(a)
            
            for c in a:
                i+=1
                
            a=s.read()
        print(f'CONTADOR: {i}')

except IOErros as e:
    print(strerror(e.errno))

print('-----<>-----')


#EJERCICIO 4
print(f'\nEJERCICIOS 4:\n')

try:
    with open('p1.txt','rt')as s:
        i=0
        ls=s.readlines()

        for l in ls:
            for c in l:
                i+=1
    
        print(ls)
        print(f'\nNº LINEAS: {len(ls)}')
        print(f'CONTADOR: {i}')
    
except IOErros as e:
    print(strerror(e.errno))

print('-----<>-----')


#EJERCICIO 5
print(f'\nEJERCICIOS 5:\n')

try:
    with open('manolita.txt','w+t')as s:
        cadena='pepe'
        
        for i in range(10):
            
            #linea a linea sin el for interno
            #s.write(f'{i+1} pepe \n')
            
            s.write(f'{i+1} ')
            for c in cadena:
                s.write(c)

            s.write('\n')
       
             
    with open('manolita.txt','rt')as s:
        a=s.read()
        print(a)
    

except IOError as e:
    print(strerror(e.errno))
    

print('-----<>-----')


#EJERCICIO 6
print(f'\nEJERCICIOS 6:\n')

fs6='s6.txt'
try:
    with open(fs6,'rt') as s6:
        i=0
        a=s6.read()
        print(a)

        '''
        al=a.lower()
        print(al)
        '''
        
        dic={}
        for c in a.lower():
            if c.isalpha():
                i+=1
                
                if not c in dic:
                    dic[c]=1
                else:
                    dic[c]+=1
        
        print(f'\n{i}')

        print(dic)

        '''
        ordenL= sorted(dic)
        
        print(ordenL)

        for l in ordenL:
            if l in dic:
                print(f'{l} -> {dic[l]}')
        '''
        
        #ORDENAR ALFABETICAMENTE POR KEY
        print(f'\n#ORDENAR ALFABETICAMENTE POR KEY\n')
        for key,value in sorted(dic.items()):
            print(f'{key} -> {value}')
            
          
        #ORDENAR POR VALOR
        print(f'\nORDENAR POR VALOR\n')
        for key in sorted(dic,key=dic.get,reverse=True):
            print(f'{key} -> {dic[key]}')
            
        

except IOError as e:
    print(strerror(e.errno))
        

print('-----<>-----')


#EJERCICIO 7
print(f'\nEJERCICIOS 7:\n')

try:
    fs7='alonso.txt'
    with open(fs7,'rt') as s7:

        lista=s7.readlines()

        print(lista)

        '''
        for l in lista:
            suma=0.0
            aux=l.split(' ')
            print(aux)

            for i in range(2,len(aux)-1):
                print(aux[i])
                suma+=float(aux[i])

            print(f'{aux[0]} {aux[1]} --> {suma}')  
        
        '''
        
        dic7={}

        for l in lista:
            aux=l.split(' ')
            print(aux)

            nombre=aux[0]+' '+aux[1]
            print(nombre)

            if nombre not in dic7:
                dic7[nombre]= float(aux[2])
            else:
                dic7[nombre]+= float(aux[2])
                
        print(dic7)
            

except IOError as e:
    print(strerror(e.errno))
