# List 인덱싱, 슬라이딩

# index -> 0 1 2
# element -> 123 'abc' True

animals = ['코알라', '하이에나', '바다소', '땅다람쥐']
animals.append('바다코끼리')
animals.append('스컹크')
animals.append('아나콘다')

print(animals[3])
print(animals[4])

del animals[4]
print(animals)

animals.append('바다코끼리')
print(animals)

# Slicing
# [0:2]

print(animals[0:2])