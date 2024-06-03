# Tuple의 특징 : Packing, UnPacking

my_tuple = 1,2,3
num1, num2, num3 = my_tuple
print(num1)
print(num2)
print(num3)

num1 = 1
num2 = 2

num1, num2 = num2, num1
print(num1)
print(num2)
print(num3)