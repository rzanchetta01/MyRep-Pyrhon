#Valida senha

senha = str(input("digite qual vai ser a sua senha "))


tentativa = str(input("digite a senha "))
while(tentativa!=senha):
    print("senha incorreta")
    tentativa = str(input("digite a senha novamente "))
print("senha correta ")