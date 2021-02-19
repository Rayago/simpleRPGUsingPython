items = ['a suit of armor', 'a peace of meat', 'an edredom']
# Get the player's name with input and store it in the name variable
name = input('What\'s your name? ')
# Greet the player using string concatenation
print('Hello, ' + name +'! The game will start now')
# Print out some steps for player to choose from, for example:
# Next steps: 1) Look around 2) Chop down tree 3) Jump
print('You are in a forest in the middle of the night, alone, what will you do?')
print('Next steps: 1) Look around 2) Chop down tree 3) Jump')
op = int(input())
# Use an if statement to decide the next steps to print. For example, if they picked 1:
if op == 1:
    print('You\'ve spotted a suit of armor! 1) Put it on 2) Ignore it')
    op2 = int(input())
    if op2 == 1:
        print('You ran out of the forest safe and protected against everything could hurt you. Well done! You won the game!')
    elif op2 == 2:
        print('You\'ve been hurt by the hunters of the forest by mistake. This could have been avoided if you were PROTECTED, right? End of the game')

elif op == 2:
    print('The tree fell on you. I\'m sorry. End of the game')
elif op == 3:
    print('Fell and hurt himself, making noise made you chased and captured by the werewolf. End of the game')

# You've spotted a suit of armor! 1) Put it on 2) Ignore it

# Do this inside a loop until the user is done with the game
