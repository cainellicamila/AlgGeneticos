# dos a la treinta menos 1 (2^30)-1
#Poblacion inicial 10 cromosomas
# 30 genes en el
# Crossover: 0.75
# Mutacion: 0.05
# Funcion
import random

import numpy as np
from prettytable import PrettyTable

funObj = []
fit = []
coef = (2 ** 30) - 1
cromosoma=[]
decimales=[]
ruleta=[]
elegidos=[]



def aleatorioC(a,b,c):
    cromo=[]

    for i in range(0,c):
        r=random.randint(a,b)
        cromo.append(r)
    return cromo

def PoblacionInicial():
    poblacion=[]

    for i in range (0,10) :
        a=aleatorioC(0,1,30)
        poblacion.append(a)
    return poblacion


def binadec ():
    decimales.clear()
    for i in Poblacion:
        strOfNumbers=''.join(str(n) for n in i)
        crom=strOfNumbers
        cromosoma.append(crom)
        dec=(int(strOfNumbers,2))
        decimales.append(dec)

def cuentas ():
    funObj.clear()
    fit.clear()

    sum = 0
    max = 0
    min = 99999999

    for j in range(10):
        fobj =((decimales[j]/coef)**2)
        funObj.append(fobj)
        if max<fobj:
            max=fobj
        if min>fobj:
            min=fobj
        sum += fobj
    prom = sum/10
    sumf = 0
    ruleta.clear()
    for j in range (10):
        f = funObj[j] / sum
        fit.append(f)
        sumf += f


        for i in range(int(np.round(f*100))):
            ruleta.append(cromosoma[j])

    for i in range(10):
        tabla.add_row([cromosoma[i], decimales[i], funObj[i], fit[i]])
    print(tabla)
    tabla.clear_rows()
    print("Suma Funcion Objetivo: " , sum)
    print("Suma Fit: ", sumf)
    print("Maximo: " , max)
    print("Minimo: " , min)
    print("Promedio: ", prom)

    '''for i in range (99):
        print(ruleta[i])'''

def giraruleta():
    cromosoma.clear()
    #cross1=''
    #cross2=''
    b = aleatorioC(0,99,10)
    print(b)
    print (len(ruleta))
    for al in range(10):
        n=b[al]
        cromosoma.append(ruleta[n])
    print(cromosoma)

    for i in range(0, 10, 2):
        c= random.random()
        c1=cromosoma[i]
        c2=cromosoma[i+1]
        if c <= 0.75:
            corte=random.randrange(0,29)
            cross1=''
            cross2=''
            for j in range (30):
                if j <= corte:
                    cross1=cross1+c1[j]
                    cross2=cross2+c2[j]
                else:
                    cross1=cross1+c2[j]
                    cross2=cross2+c1[j]
            cromosoma[i]=cross1
            cromosoma[i+1]=cross2

    print(cromosoma)

    for i in range (10):
        c=random.random()
        if c <=0.05:
            cambia=random.randrange(0,29)
            cm=cromosoma[i]
            d=int(cambia-1)

            if cm[cambia] == 0:

                cm=(cm[:d]+'1'+cm[cambia:])
            else:

                cm=(cm[:d]+'0'+cm[cambia:])
            cromosoma[i]= cm
    decimales.clear()
    for i in range(10):
        decimales.append(int(cromosoma[i],2))


    print(cromosoma)
    print(decimales)


tabla = PrettyTable()
tabla.field_names=['Cromosoma','Decimal', 'Funcion Objetivo', 'Fit']


Poblacion=PoblacionInicial()
binadec()
for i in range(200):
    print('Corrida', i+1)
    cuentas()
    giraruleta()
