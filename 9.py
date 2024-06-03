# 기본재료 2 : 리스트, 튜플, 딕셔너리
import random

# List
# [val1, val2]
my_list = [1,2,3]
print(my_list)

French = ['Mbappe', 'Griezmann', 'Thuram', 'Konate', 'Kante']
print(random.choice(French))

French.append('Theo')

# Tuple -> 값을 바꿀 수 없음
# Dictionary -> 연관 정보를 그룹화
my_dict = {'Mbappe' : 'FW', 'Kante' : 'MF', 'Konate' : 'DF'}
print(my_dict)