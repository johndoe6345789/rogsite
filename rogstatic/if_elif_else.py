import random

# we generate a number between 1 and 6  ----
random_number = random.randrange(7)

#Now take a guess, is it 6 or 4?

if random_number == 6:
    print("First guess correct!")
elif random_number == 4:
    print("second and last guess correct!")
else:
    print("Failed!")