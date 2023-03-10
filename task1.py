# Задача 1. Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def raise_degree(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * raise_degree(a, b - 1)
print(raise_degree(a, b))