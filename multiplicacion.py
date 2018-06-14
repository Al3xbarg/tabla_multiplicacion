#!/usr/bin/python
# -*-  coding: utf-8 -*-
num = int(raw_input("Escriba un Numero del 1 al 10: " ))
rango = range(+1,+11)

if num > 10:
    print "Error: Debes elegir un numero entre el 1 y el 10"
elif num < 1:
    print "Error: Debes elegir un numero entre el 1 y el 10"
else:
    for elemento in rango:
        resultado = num * elemento
        print num, "x", elemento, "=" , resultado
