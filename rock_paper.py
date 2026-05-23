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

n = input("Enter the Choice ('Rock','Paper','Scissor') : ")

comp_choice = random.choice(choice)

# print(n)
print(f'User Choice is {n}')

#print(comp_choice)
print(f'Computer Choice is {comp_choice}')

if(n == comp_choice):
    print("Tie")
   
elif (n == 'Rock'):
    if comp_choice == 'Paper':
        print(f"Computer's choice {comp_choice} Win ", )
    else:
        print(f"User choice Rock Wins Over Scissor")

elif (n == 'Paper'):
    if comp_choice == 'Scissor':
        print(f"Computer's choice {comp_choice} Win ", )
    else:
        print(f"User choice Paper Wins Over Rock")

elif (n == 'Scissor'):
    if comp_choice == 'Rock':
        print(f"Computer's choice {comp_choice} Win ", )
    else:
        print(f"User choice Scissor Wins Over Paper")