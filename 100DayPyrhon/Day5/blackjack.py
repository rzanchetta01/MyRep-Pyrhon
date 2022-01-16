# O famoso 21
from pickle import FALSE
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

# Mão do bot
baralho_bot = []

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
def fold_or_draw(choice: str, obj : rfd):
    
    #Player turn
    if obj.playerTurn:
        if(choice.upper() == "SIM" or choice.upper() == "DRAW"):
            print("Coragem hein\n")

            play = draw_card()
            baralho_jogador.append(play)

            if play == "A" or play == "J" or play == "Q" or play == "K":
                obj.playerCount += 10
            else:
                obj.playerCount += int(play)

            print(f"você virou : {play}")
           
            return obj

        elif(choice.upper() == "NAO" or choice.upper() == "FOLD"):
            obj.endedPlayer = True
            print(f"Você arregou com o baralho: {baralho_jogador} e com o total de: {obj.playerCount}")
            return obj
        else:
            print("Num entendi")
            return fold_or_draw(input("SIM OU NAO? "),obj)
        
    #Bot Turn
    else:
        if obj.botCount < 18:
            botPlay = draw_card()
            baralho_bot.append(botPlay)
            if botPlay == "A" or botPlay == "J" or botPlay == "Q" or botPlay == "K":
                obj.botCount += 10
            else:
                obj.botCount += int(botPlay)

            print(f"O RoboCopinson virou: {botPlay}")
            return obj

        else:
            obj.endedBot = True
            print(f"O bot arregou com as seguintes cartas: {baralho_bot} totalizando {obj.botCount}")
            return obj

#Valida vitória
def endGame():
    if (obj.playerCount == 21 and obj.botCount == 21):
        print("EMPATOU, EU NÃO ACREDITO")
    
    elif obj.playerCount == obj.botCount:
         print("EMPATOU, EU NÃO ACREDITO")
        
    elif obj.playerCount == 21:
        print("O player ganhou, inacreditavel")
        
    elif obj.botCount == 21:
        print("Deu a lógica RoboCopinson jogou o que sabe")
        
    elif obj.playerCount > obj.botCount and obj.playerCount <=21:
        print("O player ganhou, inacreditavel")
        
    elif obj.botCount > obj.playerCount and obj.botCount <=21:
        print("Deu a lógica RoboCopinson jogou o que sabe")

    elif obj.playerCount < obj.botCount and obj.playerCount <=21:
        print("O player ganhou, inacreditavel")
        
    elif obj.botCount < obj.playerCount and obj.botCount <=21:
        print("Deu a lógica RoboCopinson jogou o que sabe")
        
#
def checkStatusGame(endedBot : bool, endedPlayer : bool):
    if endedBot == True and endedPlayer == True:
        return False
    else:
        return True
    
        
print("O famoso 21, você vai jogar contra o RoboCopinson nossa maquina invencivel")
opt = input("Preparado? ")


# Loop jogo
obj = rfd
obj.botCount = 0
obj.endedBot = False
obj.endedPlayer = False
obj.playerCount = 0
obj.playerTurn = True

while checkStatusGame(obj.endedBot, obj.endedPlayer):

    if obj.playerTurn:
        opt = input("Vai ou arrega? ")
        obj = fold_or_draw(opt, obj)
        obj.playerTurn = False

    else:
        obj = fold_or_draw(opt, obj)
        obj.playerTurn = True
        if opt.upper() != "SIM":
            obj.playerTurn = False

endGame()