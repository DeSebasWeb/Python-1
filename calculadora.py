operacion = input('que operacion vamos a hacer hoy? ')

a = input("pon el primer numero ")
b = input('pon el segundo ')

operaciones = ['suma', 'resta', 'multiplicacion', 'division']

if  operacion[0]:
    print(int(a)+int(b))

if  operacion[1]:
    print(int(a)-int(b))

if  operacion[2]:
    print(int(a)*int(b))
        
if  operacion[3]:
    print(int(a)/int(b))


