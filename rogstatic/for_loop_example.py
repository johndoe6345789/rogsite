'''
Let's add up every tenth number up to one hundred,
'''
total = 0

#--range(start, end, step)------
for number in range(10, 101, 10):
    total = total + number
    # Now we loop---

# finished when loop steps to 101----   
print(total)
    