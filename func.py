import random

# This is a comment
def get_random_number():
    return random.randint(1, 100)

#This is another comment
def get_random_number_between(min_value, max_value):
    return random.randint(min_value, max_value)

print(get_random_number_between(1,20))
