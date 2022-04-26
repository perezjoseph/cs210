import re
#Joseph Perez CS 210 TictacToe Game
grid = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"

def check_winner(gri):
    #Using grid variable string check if we have a winner
    global grid
    gri = re.sub("\n\-\+\-\+\-\n","|",grid)
    gri = gri.split("|")
    if gri[0] == gri[1] == gri[2] or gri[3] == gri[4] == gri[5] or gri[6] == gri[7] == gri[8] or gri[0] == gri[3] == gri[6] or gri[1] == gri[4] == gri[7] or gri[2] == gri[5] == gri[8] or gri[0] == gri[4] == gri[8] or gri[2] == gri[4] == gri[6]:
        print("Good game. Thanks for playing!")
        return False

    else:
        b = re.sub("\D","", grid)
        if re.sub("\D", "", grid)  == '':
            print("Game Over")
            return False
        return True


def game_modifier(ans,entity):
    #Modify the string
    gr = grid.replace(str(ans),entity)
    return gr
def validation(ans,entity):
    #Check if the input is valid
    global grid
    gri = re.sub("\n\-\+\-\+\-\n","|",grid)
    gri = gri.split("|")
    while gri[ans-1] =="x" or gri[ans-1] == "O":
        try:
            print("You Must select a different number")
            ans = int(input(f"{entity}'s turn to choose a square (1-9): "))
        except:
            print("You Must select a different number")
            ans = int(input(f"{entity}'s turn to choose a square (1-9): "))
    #After checking input proceed to execute the modification
    result = game_modifier(ans,entity)
    return result
def main():
    bo = True
    global grid
    print(grid)
    while bo != False:
        x = int(input(f"\033[1;31;40mx's turn to choose a square (1-9): "))
        grid  = validation(x,"x")
        print(grid)
        bo = check_winner(grid)
        if bo == False:
            break
        O = int(input("\033[1;34;40mO's turn to choose a square (1-9): "))
        grid = validation(O,"O")
        print(grid)
        bo = check_winner(grid)
        if bo == False:
            break
main()

