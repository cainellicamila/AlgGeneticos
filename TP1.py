# dos a la treinta menos 1 (2^30)-1
#Poblacion inicial 10 cromosomas
# 30 genes en el
# Crossover: 0.75
# Mutacion: 0.05
# Funcion
from random import *
import numpy as np
import tabulate

tabla = np.zeros((10,4))



def aleatorioC(a,b,c):
    cromosoma=[]
    for i in range(0,c):
        r=randint(a,b)
        cromosoma.append(r)
    return cromosoma

def PoblacionInicial():
    poblacion=[]
    for i in range (0,10) :
        a=aleatorioC(0,1,30)
        poblacion.append(a)
    return poblacion

Poblacion=PoblacionInicial()
def binadec ():
    j=0
    for cromosoma in Poblacion:
        print(cromosoma)
        strOfNumbers=''.join(str(n) for n in cromosoma)
        crom=(int(strOfNumbers))
        tabla[j][0]=crom
        dec=(int(strOfNumbers,2))
        tabla[j][1]=dec
        j+=1

    

def cuentas ():
    sum=0
    for j in range(10):
        num=int(tabla[j][1])
        fobj=((num/((2**30)-1))**2)
        tabla[j][2] = fobj
    for x in range (9):
        sum=(sum+(tabla[x][2]+tabla[x+1][2]))
    for i in range (10):
        fit= (tabla[i][2]/sum)
        tabla[i][3]=fit

    print(tabulate.tabulate(tabla, headers= ["Cromosoma","Decimal","FObj","Fit"]))

binadec()
cuentas()

