#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

#definimos el rango
lower = 1
upper = 500


print("Prime numbers between", lower, "and", upper, "are:")

#esta es la funcion correspondiente.
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
