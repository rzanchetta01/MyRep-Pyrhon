# O famoso 21
import random as rnd

# Fold
endedPlayer = False
endedBot = False

# Cartas base
baralho = {
    "red": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    "blue": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
}

# Baralho na mesa
board_baralho = {
    "red": [],
    "blue": []
}

# Sua mão
baralho_jogador = []
playerCount = 0

# Mão do bot
baralho_bot = []
botCount = 0

# Da as cartas


def draw_card():
    baralho_color = rnd.randrange(0, 2)
    if baralho_color == 0:
        baralho_color = "red"
    else:
        baralho_color = "blue"

    select_card = rnd.randrange(0, 12)
    resultKey = baralho.get(baralho_color)
    resultValue = resultKey[select_card]

    if board_baralho[baralho_color].__contains__(resultValue):
        return draw_card()
    else:
        board_baralho[baralho_color].append(resultValue)
        return resultValue

# Executa os movimentos


def fold_or_draw(choice: str, turn: bool, count : int):
    if turn:
        if(choice.upper() == "SIM" or choice.upper() == "DRAW"):
            print("Coragem hein\n")

            play = draw_card()
            baralho_jogador.append(play)

            if play == "A" or play == "J" or play == "Q" or play == "K":
                count += 10
                print(f" +10 Player count {count} \n")
            else:
                count += int(play)
                print(f" +{int(play)} Player count {count} \n")

            print(f"você virou : {play}")
            return count

        elif(choice.upper() == "NAO" or choice.upper() == "FOLD"):
            endedPlayer = True
            print(f"Você arregou com o baralho: {baralho_jogador} e com o total de: {count}")
            return count
        else:
            print("Num entendi")
            return fold_or_draw(input("SIM OU NAO? "), turn, count)
    else:
        if count < 18:
            botPlay = draw_card()
            baralho_bot.append(botPlay)
            if botPlay == "A" or botPlay == "J" or botPlay == "Q" or botPlay == "K":
                count += 10
            else:
                count += int(botPlay)

            print(f"O RoboCopinson virou: {botPlay}")
            return count

        else:
            endedBot = True
            print(f"O bot arregou com as seguintes cartas: {baralho_bot} totalizando {count}")
            return count


print("O famoso 21, você vai jogar contra o RoboCopinson nossa maquina invencivel")
opt = input("Preparado? ")


# Loop jogo
playerTurn = False
playerCount += fold_or_draw(opt, True, playerCount)

while not endedPlayer and not endedBot:
    if endedBot:
            if playerTurn:
                opt = input("Continua ou não? ")
                playerCount += fold_or_draw(opt, playerTurn, playerCount)
    
    if endedPlayer:
            botCount += fold_or_draw(opt, playerTurn, botCount)
        
    else:
        if playerTurn:
            opt = input("Continua ou não? ")
            playerCount += fold_or_draw(opt, playerTurn, playerCount)
            playerTurn = False
        else:
            botCount += fold_or_draw(opt, playerTurn, botCount)
            playerTurn = True
