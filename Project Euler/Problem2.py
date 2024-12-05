"""
Even Fibonacci Numbers
"""


current = 2
prev = 1 
temp = 0 
sum = 0
while current < 4000000:
    if current % 2 == 0:
        sum += current
    

    # update current 
    temp = current
    current = prev + current 
    prev = temp 

print(sum)