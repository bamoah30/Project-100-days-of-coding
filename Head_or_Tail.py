import random
your_number = input('Please make your choice: Head or tail ').lower()
if your_number == 'head':
    head = 1
else:
    tail = 0

chosen_side = random.randint(0,1)
if chosen_side == your_number:
    print(f"You chose {your_number} and it is equal to what the computer chose therefore you've won the game")
else:
    print(f"Your choice is {your_number} and is different from the computer's. You've lost the game")
