# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:12:42 2022

@author: ASUS
"""

print("===== Sisi segitiga =====")

A = int(input("Masukkan nilai sisi A = "))
B = int(input("Masukkan nilai sisi B = "))
C = int(input("Masukkan nilai sisi C = "))

print("\nNilai sisi A = ", A)
print("Nilai sisi B = ", B)
print("Nilai sisi C = ", C)

if (A == B == C) :
    print("\nIni segitiga sama sisi")
    print("Artinya Semua sisi bernilai sama")
    print(" ")
    print("Buktinya : Sisi A = ", A, ";")
    print("           Sisi B = ", B, ";")
    print("           Sisi C = ", C, ";")
elif (A == B or A == C or B == C) :
    print("\nIni segitiga sama kaki")
    print("Artinya hanya dua sisi yang bernilai sama")
    print(" ")
    print("Buktinya : Sisi A = ", A, ";")
    print("           Sisi B = ", B, ";")
    print("           Sisi C = ", C, ";")
else : 
    print("\nIni segitiga sembarang")
    print("Artinya tidak ada sisi yang bernilai sama")
    print(" ")
    print("Buktinya : Sisi A = ", A, ";")
    print("           Sisi B = ", B, ";")
    print("           Sisi C = ", C, ";")