from collections import Counter

with open('input.txt', 'r') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

# PART 2
counter_list2 = Counter(list1)

similarity_score = 0 

for num in list2: 
    if num in counter_list2:
        similarity_score += num * counter_list2[num]

print(f"Similarlity score is: {similarity_score}")

# PART 1

list1 = sorted(list1)
list2 = sorted(list2)

difference = 0 

for index in range(len(list1)):
    difference += abs(list1[index] - list2[index])

print(f"The sum of differences is: {difference}" )

