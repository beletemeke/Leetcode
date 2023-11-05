from math import ceil
n = int(input())
m = int(input())
original_m = m
number_people = []
for _ in range(n):
    number_people.append(int(input()))

diff = 0
number_people.sort()
max_bench = max(number_people) 
for num in number_people:
    diff += max_bench - num

while m > 0:
    m -= diff
    diff = len(number_people)
    if m > 0:
      max_bench += 1


   
minimum = max_bench
maximum = max(number_people) + original_m
print(minimum, maximum)
    
