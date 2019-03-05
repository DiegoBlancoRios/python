#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CONVERTIR UNA CANTIDAD DE TIEMPO EXPRESADA EN SEGUNDOS AL FORMATO HORAS-MINUTOS-SEGUNDOS")
    numero_1 = float(input("Escriba un número: "))
    numero_2 = float(input("Escriba otro número: "))
    numero_3 = float(input("Escriba otro número: "))
    media = (numero_1 + numero_2) / 2
    print("La media aritmética de " + str(numero_1)*3600 +" y "+str(numero_2)*60 +" es "+ str(media))
    #otra forma
  
 
if __name__ == "__main__":
    main()


