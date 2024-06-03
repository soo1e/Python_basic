# 홀짝 구분하기
numbers = [1,2,3,4,5,6,7]
for num in numbers:
    print(num)

print("*****************")

for num in numbers:
    if num % 2 == 1:
        print(num, "는 홀수!")
    else:
        print(num, "는 짝수!")

print("*****************")

