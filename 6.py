#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CONVERTIR UNA CANTIDAD DE TIEMPO EXPRESADA EN SEGUNDOS AL FORMATO HORAS-MINUTOS-SEGUNDOS")
    n = int(input("Escriba un número: "))
    horas= (n/3600)
    minutos= (n%3600)/60
    segundos= (n%60)
    print("horas:"+ str(horas))
    print("minutos:"+ str(minutos))
    print("segundos:"+ str(segundos))
  
 
if __name__ == "__main__":
    main()


