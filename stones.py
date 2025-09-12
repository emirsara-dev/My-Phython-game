import random

def pick_for_computer(stones):
    """Returns the coumputer's pick of stones."""
    #If possible leave a losing state of 4.
    if stones <= 2 or stones == 5:
        return 1
    elif stones == 3 or stones == 6:
        return 2
    
    return random.randint(1, 2)

def pick_for_user():
    """Returns the user's pick of stones with limit."""
    removed = 0
    while removed != 1 and removed != 2:
        removed = int(input("How many do you pick up? (1-2): "))
    return removed

def show(num_stones):
    """Returns a visual of the stone pile."""
    picture = "o " * num_stones
    label = "(" + str(num_stones) + " stones)\n"
    return picture + label

def initialize():
    """Returns the starting size of the stone pile."""
    initial_num_stones = random.randint(10, 16)
    return initial_num_stones