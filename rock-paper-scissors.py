import random
l = ['rock', 'paper', 'scissors']
while True:
    i = input("Welcome to a legendary rock paper scissors game! What do you want to play? (rock, paper, scissors, I quit)")
    r = random.randint(0,2)
    if l[r] == i.lower():
        print("I played ", l[r], ', Game drawn!')
    elif i.lower() == 'i quit':
        break
    elif l[((r+1)%3)] == i.lower():
        print("I played ", l[r], ', You won!')
    elif l[((r-1)%3)] == i.lower():
        print("I played ", l[r], ', You lost!')
    else:
        print("Invalid input, please try again")
