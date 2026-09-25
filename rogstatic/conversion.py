'''
Converting ints, strings, floats lists etc 
'''


#--int to string----------------
num = 4
num_string = str(num)

#--string to int----------------
num_string = '4'
num = int(num_string)

#--int to float -----------------
num = 7
float_num = float(num)

print(num,"",float_num)

#--string to list -----------------
string1 = '123abc'
list1 =list(string1)

print(string1,"", list1)

#-- list to dictionary ------------
a = ['1', '2', '3', 'a', 'b', 'c']

b = {}
for i in range(0, len(a), 2):
        b[a[i]] = a[i+1]
        
print(a, "", b)
