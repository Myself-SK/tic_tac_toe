import sys
tic = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display():
    print("[%c,%c,%c]" % (tic[1], tic[2], tic[3]))
    print("[%c,%c,%c]" % (tic[4], tic[5], tic[6]))
    print("[%c,%c,%c]" % (tic[7], tic[8], tic[9]))


def CheckPosition(x):
    if(tic[x] == ' '):
        return True
    else:
        return False


def CheckWin(p):
    if(tic[1] == tic[2] and tic[2] == tic[3] and tic[1] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[4] == tic[5] and tic[5] == tic[6] and tic[4] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[7] == tic[8] and tic[8] == tic[9] and tic[7] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[1] == tic[4] and tic[4] == tic[7] and tic[1] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[2] == tic[5] and tic[5] == tic[8] and tic[2] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[3] == tic[6] and tic[6] == tic[9] and tic[3] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[1] == tic[5] and tic[5] == tic[9] and tic[5] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[3] == tic[5] and tic[5] == tic[7] and tic[5] != ' '):
        print("{0} Won the Game".format(p))
        sys.exit(0)
    elif(tic[1] != ' ' and tic[2] != ' ' and tic[3] != ' ' and tic[4] != ' ' and tic[5] != ' ' and tic[6] != ' ' and tic[7] != ' ' and tic[8] != ' ' and tic[9] != ' '):
        print("This Game is Draw")
        sys.exit(0)
    else:
        return -1


while CheckWin:
    display()
    print("Two Options:\n1.X\n2.O")
    p1 = str.upper(input("Select your Choice:"))
    if p1 == '1' or p1 == 'X':
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    print("Player 1 =", p1)
    print("Player 2 =", p2)
    for i in range(1, 10):
        if i % 2 != 0:
            i += 1
            choice = int(
                input("Enter the position between [1-9] where you want to mark : "))
            if(CheckPosition(choice)):
                tic[choice] = p1
                display()
                CheckWin(p1)
        else:
            choice = int(
                input("Enter the position between [1-9] where you want to mark : "))
            if(CheckPosition(choice)):
                tic[choice] = p2
                display()
                CheckWin(p2)
