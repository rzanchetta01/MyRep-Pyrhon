import os

col1 = [" ", " ", " "]
col2 = [" ", " ", " "]
col3 = [" ", " ", " "]
isEnded = False
playerTurn = True
turnCount = 0


def check_win():
    # Horizontals
    if col1[0] == "X" and col1[1] == "X" and col1[2] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[0] == "O" and col1[1] == "O" and col1[2] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    if col2[0] == "X" and col2[1] == "X" and col2[2] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col2[0] == "O" and col2[1] == "O" and col2[2] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    if col3[0] == "X" and col3[1] == "X" and col3[2] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col3[0] == "O" and col3[1] == "O" and col3[2] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    # Verticals
    if col1[0] == "X" and col2[0] == "X" and col3[0] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[0] == "O" and col2[0] == "O" and col3[0] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    if col1[1] == "X" and col2[1] == "X" and col3[1] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[1] == "O" and col2[1] == "O" and col3[1] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    if col1[2] == "X" and col2[2] == "X" and col3[2] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[2] == "O" and col2[2] == "O" and col3[2] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    # Diagonals
    if col1[0] == "X" and col2[1] == "X" and col3[2] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[0] == "O" and col2[1] == "O" and col3[2] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    if col1[2] == "X" and col2[1] == "X" and col3[0] == "X":
        print("Player X, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()

    elif col1[2] == "O" and col2[1] == "O" and col3[0] == "O":
        print("PLayer O, you win")
        print("   1     2     3")
        print(f"C {col1}\nB {col2}\nA {col3}")
        exit()


while not isEnded:
    print("   1     2     3")
    print(f"C {col1}\nB {col2}\nA {col3}")
    play = input("\nSelect the next movement: ").upper()
    print("\n\n\n\n\n\n\n\n")
    if play == "A1" and col3[0] == " ":
        if playerTurn:
            col3[0] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col3[0] = "O"
            playerTurn = True
            turnCount += 1

    if play == "A2" and col3[1] == " ":
        if playerTurn:
            col3[1] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col3[1] = "O"
            playerTurn = True
            turnCount += 1

    if play == "A3" and col3[2] == " ":
        if playerTurn:
            col3[2] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col3[2] = "O"
            playerTurn = True
            turnCount += 1

    if play == "B1" and col2[0] == " ":
        if playerTurn:
            col2[0] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col2[0] = "O"
            playerTurn = True
            turnCount += 1

    if play == "B2" and col2[1] == " ":
        if playerTurn:
            col2[1] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col2[1] = "O"
            playerTurn = True
            turnCount += 1

    if play == "B3" and col2[2] == " ":
        if playerTurn:
            col2[2] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col2[2] = "O"
            playerTurn = True
            turnCount += 1

    if play == "C1" and col1[0] == " ":
        if playerTurn:
            col1[0] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col1[0] = "O"
            playerTurn = True
            turnCount += 1

    if play == "C2" and col1[1] == " ":
        if playerTurn:
            col1[1] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col1[1] = "O"
            playerTurn = True
            turnCount += 1

    if play == "C3" and col1[2] == " ":
        if playerTurn:
            col1[2] = "X"
            playerTurn = False
            turnCount += 1

        else:
            col1[2] = "O"
            playerTurn = True
            turnCount += 1

    if turnCount == 9:
        os.system('pause')
        col1 = [" ", " ", " "]
        col2 = [" ", " ", " "]
        col3 = [" ", " ", " "]
        turnCount = 0

    check_win()
    if play.upper() == "STOP":
        isEnded = True
