import random

choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def board(state1,state2):
    zero = "X" if state1[0] else ("O" if state2[0] else 0)
    one = "X" if state1[1] else ("O" if state2[1] else 1)
    two = "X" if state1[2] else ("O" if state2[2] else 2)
    three = "X" if state1[3] else ("O" if state2[3] else 3)
    four = "X" if state1[4] else ("O" if state2[4] else 4)
    five = "X" if state1[5] else ("O" if state2[5] else 5)
    six = "X" if state1[6] else ("O" if state2[6] else 6)
    seven = "X" if state1[7] else ("O" if state2[7] else 7)
    eight = "X" if state1[8] else ("O" if state2[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def SinglePlayer():
    state1=[0,0,0,0,0,0,0,0,0]
    state2=[0,0,0,0,0,0,0,0,0]
    chance=1
    while True:
        board(state1,state2)
        if chance==1:
            print("X's chance")
            answer=int(input("Play your chance: "))
            choices.remove(answer)
            print("Choices >>",choices)
            if(state1[answer]==1 or state2[answer]==1):
                print("Already filled")
            else:
                state1[answer]=1
                if Checkwin(state1):
                    board(state1,state2)
                    print("X has won")
                    break
        else:
            print("O's chance")
            changed = False
            for win in wins:
                if state2[win[0]] + state2[win[1]] + state2[win[2]] == 1 or state2[win[0]] + state2[win[1]] + state2[win[2]] == 2:
                    if (state1[win[0]] == 0 and state2[win[0]] == 0)and (state1[win[1]]==0 and state2[win[1]]==1) and (state1[win[2]]==0 or state2[win[2]]==1):
                        answer = win[0]
                        changed = True
                    elif (state1[win[1]] == 0 and state2[win[1]] == 0) and (state1[win[0]]==0 or state2[win[0]]==1) and (state1[win[2]]==0 or state2[win[2]]==1):
                        answer = win[1]
                        changed = True
                    elif (state1[win[2]] == 0 and state2[win[2]] == 0) and (state1[win[1]]==0 or state2[win[1]]==1) and (state1[win[0]]==0 or state2[win[0]]==1):
                        answer = win[2]
                        changed = True
            if changed:
                print(f"Computer choose {answer} from algorithm")
            else:
                answer = random.choice(choices)
                choices.remove(answer)
                print(f"Computer choose {answer} from random")
            if(state1[answer]==1 or state2[answer]==1):
                print("Already filled")
            else:    
                state2[answer]=1
                if Checkwin(state2):
                    board(state1,state2)
                    print("O has won")
                    break
        chance =  1 - chance

def Multiplayer():
    state1=[0,0,0,0,0,0,0,0,0]
    state2=[0,0,0,0,0,0,0,0,0]
    chance=1
    while True:
        board(state1,state2)
        if chance==1:
            print("X's chance")
            answer=int(input("Play your chance: "))
            if(state1[answer]==1 or state2[answer]==1):
                print("Already filled")
                continue
            state1[answer]=1
            if Checkwin(state1):
                print("X has won")
                break
        else:
            print("O's chance")
            answer=int(input("Play your chance: "))
            if(state1[answer]==1 or state2[answer]==1):
                print("Already filled")
                continue
            state2[answer]=1
            if Checkwin(state2):
                print("0 has won")
                break
        chance =  1 - chance

def Checkwin(state):
    for win in wins:
        if state[win[0]] + state[win[1]] + state[win[2]] == 3:
            return True
    return False

def main():
    print("Welcome to the Game")
    print("1. For single player")
    print("2. For two player")
    choice=int(input("Enter your choice: "))
    if choice==1:
        SinglePlayer()
    elif choice ==2:
        Multiplayer()
    else:
        print("Invalid input")
        
main()