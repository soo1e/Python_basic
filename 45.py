# 여러개 돌려주기
# return 값에 대해

def add_mul(num1, num2):
    return num1 + num2, num1 * num2

print(add_mul(1,2))

my_add, my_mul = add_mul(1,2)
print(my_add)
print(my_mul)