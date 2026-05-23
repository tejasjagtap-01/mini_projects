'''
WorkFlow
1. User Input (Rock, Scissor, Paper)
2. Computer Choice (Random choice of Comp)
3. Result print

Conditions
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B- Paper
Paper - Paper = Tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C- Scissor
Scissor - Scissor = Tie
Scissor - Paper = Scissor Win
Scissor - Rock = Rock Win
'''

import random 

choice = ["Rock","Paper","Scissor"]
comp_score = 0
user_score = 0

n = input("Enter the Choice ('Rock','Paper','Scissor') : ")

comp_choice = random.choice(choice)

print(n)
print(f'User Choice is {n}')

print(comp_choice)
print(f'Computer Choice is {comp_choice}')

if(n == comp_choice):
    print("Tie")
    print(f"Computer Choice {comp_score} and User Choice {user_score}")

elif (n == 'Rock'):
    if comp_choice == 'Paper':
        print(f"{comp_choice} Win ", comp_choice+1)
