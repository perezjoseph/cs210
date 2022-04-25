grid = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
def body(ans,entity):
    grid.replace(str(ans),entity)
    print(grid)
def main():

    bo = True
    print(grid)
    while bo != False:
        x = int(input("x's turn to choose a square (1-9): "))
        grid  = body(x,"x")
        O = int(input("O's turn to choose a square (1-9): "))
        grid = body(O,"O")
main()

