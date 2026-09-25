'''
A simple demonstration of a while loop, it
slices a list and prints out the maximum 
value character  in the four-piece slice.
'''
keyboard ='qwertyuiopasdfghjklzxcvbnm'

#--now convert to List, saves much typing---
keyboard = list(keyboard)
#--print the list for a check----
print(keyboard)
#-- set initial list indexes-----
index1 = 0
index2 = 4

while  not index2 > len(keyboard):    # <-- this avoids an 
                                      # out of index error
    slice = keyboard[index1:index2]
    max_char = max(slice)

    print(max_char)
    index1 = index1 + 1
    index2 = index2 + 1
    #-- loop to end of the list
