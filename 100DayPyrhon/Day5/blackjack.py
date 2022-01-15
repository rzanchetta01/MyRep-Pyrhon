# O famoso 21
import random as rnd
import returnFoldDraw as rfd

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
            rfd.count = count
            return rfd

        elif(choice.upper() == "NAO" or choice.upper() == "FOLD"):
            rfd.count = count
            rfd.endedPlayer = True
            print(f"Você arregou com o baralho: {baralho_jogador} e com o total de: {count}")
            return rfd
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
            rfd.count = count
            return rfd

        else:
            rfd.count = count
            rfd.endedBot = True
            print(f"O bot arregou com as seguintes cartas: {baralho_bot} totalizando {count}")
            return rfd

#Valida vitória
def endGame():
    if (playerCount == 21 and botCount == 21):
        print("EMPATOU, EU NÃO ACREDITO")
    
    elif playerCount == botCount:
         print("EMPATOU, EU NÃO ACREDITO")
        
    elif playerCount == 21:
        print("O player ganhou, inacreditavel")
        
    elif botCount == 21:
        print("Deu a lógica RoboCopinson jogou o que sabe")
        
    elif playerCount > botCount and playerCount <=21:
        print("O player ganhou, inacreditavel")
        
    elif botCount > playerCount and botCount <=21:
        print("Deu a lógica RoboCopinson jogou o que sabe")
        
def checkStatusGame(endedBot : bool, endedPlayer : bool):
    if endedBot == True and endedPlayer == True:
        return False
    else:
        return True
    
        
print("O famoso 21, você vai jogar contra o RoboCopinson nossa maquina invencivel")
opt = input("Preparado? ")


# Loop jogo
playerTurn = True
botObj = rfd
botObj.endedBot = False
botObj.count = 0
playerObj = rfd
playerObj.endedPlayer = False
playerObj.count = 0

while checkStatusGame(botObj.endedBot, playerObj.endedPlayer):
    if endedBot:
            if playerTurn:
                opt = input("Continua ou não? ")
                             
    if endedPlayer:
            botObj = fold_or_draw(opt, playerTurn, botObj.count)
        
    else:
        if playerTurn:
            opt = input("Vai ou arrega? ")
            playerObj = fold_or_draw(opt, playerTurn, playerObj.count)
            playerTurn = False

        else:
            botObj = fold_or_draw(opt, playerTurn, botObj.count)
            playerTurn = True
            if opt.upper() != "SIM":
                playerTurn = False

endGame()