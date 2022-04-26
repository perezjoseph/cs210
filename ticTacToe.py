import re
grid = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
def game_logic(ans,entity):
    gr = grid.replace(str(ans),entity)
    return gr
def validation(ans,entity):
    global grid
    gri = re.sub("\n\-\+\-\+\-\n","|",grid)
    gri = gri.split("|")
    while ans not in range(1,9):
        print("You Must select a different number")
        ans = int(input(f"{entity}'s turn to choose a square (1-9): "))
    while gri[ans-1] =="x" or gri[ans-1] == "O":
        print("You Must select a different number")
        ans = int(input(f"{entity}'s turn to choose a square (1-9): "))
    result = game_logic(ans,entity)
    return result
def main():
    bo = True
    global grid
    print(grid)
    while bo != False:
        x = int(input("x's turn to choose a square (1-9): "))
        grid  = validation(x,"x")
        print(grid)
        O = int(input("O's turn to choose a square (1-9): "))
        grid = validation(O,"O")
        print(grid)
main()

