# Practice if/elif/else statements here.
# my code
print("welcome to rock,scisssors,paper Game".upper())
player_A = input("player_A   please enter rock/scisssor/paper: ")
player_B = input("player_B   please enter rock/scisssor/paper: ")

if player_A == player_B:
   print("The scores are level")

elif player_A == "rock" and player_B == "scissor":
    print("player_A wins!")
    
elif player_A == "scissor" and player_B == "paper":
    print("player_A wins!")
    
elif player_A == "paper" and player_B == "rock":
    print("player_A wins!")

else:
     print("player_B wins!")




















