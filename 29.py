# Comprehension -> 간결하게

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

print(odd_numbers)

print([number for number in numbers if number % 2 == 1])