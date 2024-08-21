import random

playing = True

values = {"A1": " ", "B1": " ", "C1": " ",
          "A2": " ", "B2": " ", "C2": " ",
          "A3": " ", "B3": " ", "C3": " ",
          }

player1 = "X"
player2 = "O"
players = [player1, player2]


def victory_verifier():
    global playing
    if values["A1"] == "X" and values["A2"] == "X" and values["A3"] == "X":
        print("'X' Ganhou!")
        playing = False
        print(playing)
        return playing
    elif values["B1"] == "X" and values["B2"] == "X" and values["B3"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["C1"] == "X" and values["C2"] == "X" and values["C3"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["A1"] == "X" and values["B1"] == "X" and values["C1"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["A2"] == "X" and values["B2"] == "X" and values["C2"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["A3"] == "X" and values["B3"] == "X" and values["C3"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["A1"] == "X" and values["B2"] == "X" and values["C3"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing
    elif values["A3"] == "X" and values["B2"] == "X" and values["C1"] == "X":
        print("'X' Ganhou!")
        playing = False
        return playing



    elif values["A1"] == "O" and values["A2"] == "O" and values["A3"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["B1"] == "O" and values["B2"] == "O" and values["B3"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["C1"] == "O" and values["C2"] == "O" and values["C3"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["A1"] == "O" and values["B1"] == "O" and values["C1"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["A2"] == "O" and values["B2"] == "O" and values["C2"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["A3"] == "O" and values["B3"] == "O" and values["C3"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["A1"] == "O" and values["B2"] == "O" and values["C3"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing
    elif values["A3"] == "O" and values["B2"] == "O" and values["C1"] == "O":
        print("'O' Ganhou!")
        playing = False
        return playing


def printboard():
    print(f"""
      A     B     C          
1     {values["A1"]}  |  {values["B1"]}  |  {values["C1"]} 
    _____|_____|_____
2     {values["A2"]}  |  {values["B2"]}  |  {values["C2"]}  
    _____|_____|_____
3     {values["A3"]}  |  {values["B3"]}  |  {values["C3"]}  
         |     |

""")


printboard()


def x_playing():
    x_play = True
    while x_play:
        try:
            print("Vez de 'X'")
            print("Digite uma posição, informando primeiro a coluna e a seguir a linha, exemplo: 'A1' ou 'B3'")
            choose = input("Escolha: ").upper()
            if values[choose] == "O" or values[choose] == "X":
                print("Esta posição ja foi escolhida!")
                continue
            else:
                values[choose] = "X"
                printboard()
                victory_verifier()
                if playing == False:
                    startgame()
                elif playing == True:
                    o_playing()
        except ValueError:
            print(ValueError)
            break


def o_playing():
    global x_play
    o_play = True
    while o_play:
        try:
            print("Vez de 'O'")
            print("Digite uma posição, informando primeiro a coluna e a seguir a linha, exemplo: 'A1' ou 'B3'")
            choose = input("Escolha: ").upper()
            if values[choose] == "X" or values[choose] == "O":
                print("Esta posição ja foi escolhida!")
                continue
            else:
                values[choose] = "O"
                printboard()
                victory_verifier()
                if playing == False:
                    startgame()
                elif playing == True:
                    x_playing()
        except ValueError:
            print(ValueError)
            break


def startgame():
    while playing:
        try:
            first_playing = random.choice(players)
            if first_playing == "X":
                print("'X' Joga primeiro!")
                x_playing()
            elif first_playing == "O":
                print("'O' Joga primeiro!")
                o_playing()

        except ValueError:
            print("Algo deu errado!")
            break
        print("Jogo encerrado!")


startgame()