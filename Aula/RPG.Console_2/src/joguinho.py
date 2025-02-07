import random
dano = 1
defesa = 0
resp = "sim"
vida_guerreiro = 100
dinheiro = 50
itens = ["adaga","Escudo","armadura","espada","heal", "lanca" , "arco longo", "glaive"]
print("Vida: ", vida_guerreiro, "Defesa: ", defesa, "Dano: ", dano)
caminho = int(input("Escolha o caminho: \n 1 - Caverna \n 2 - Floresta"))
item_recebido =  ""
opcao_escolhida = 8


if caminho == 1:
 print("Voce encontrou um mercador")


 escolha_mercador = int(input("Boa noite guerreiro! Tem interesse em comprar algo? \n (1)Sim (2) Não"))

 if escolha_mercador == 1:
    while opcao_escolhida != 0:
        print("1 - Espada (+25 dano) R$25.0")
        print("2 - Escudo (+10 defesa) R$12.0")
        print("3 - Arco e flecha (+8 dano) R$50.0")
        print("4 - Armadura (+12 defesa) R$40.0")
        print("5 - Adaga (+3 dano)")
        

        print(f"valor disponivel {dinheiro}")

        opcao_escolhida = int(input("Escolha sua opcao \n 0 - PARA SAIR "))

        if (opcao_escolhida == 1):
            print("Voce escolheu a Espada")
            dano = dano + 25
            dinheiro = dinheiro - 25
            print(f"Saldo atual: {dinheiro}")

        elif (opcao_escolhida == 2):
            defesa = defesa + 10
            print("Voce escolheu o Escudo")
            dinheiro = dinheiro - 12
            print(f"Saldo atual: {dinheiro}")

        elif (opcao_escolhida == 3):
            print("Voce escolheu o Arco  Flecha")
            dano = dano + 8
            dinheiro = dinheiro - 50
            print(f"Saldo atual: {dinheiro}")

        elif (opcao_escolhida == 4):
            defesa = defesa + 12
            print("Voce escolheu a armadura")
            dinheiro = dinheiro - 40
            print(f"Saldo insuficiente")

        elif (opcao_escolhida == 5):
            dano = dano + 3
            print("Voce escolheu a adaga")
            dinheiro = dinheiro - 16
        elif(opcao_escolhida == 0):
            break


        print(f"Saldo insuficiente") 
        break
    else:
        print("Boa Sorte na sua jornada")


if caminho == 2:
      print("Voce encontrou um Bau Misterioso")
      abrir = int(input("Deseja abri-lo? \n 1 - sim \n 2 - não"))

      if abrir == 1:
            loot = random.randint(1,2)
            if loot == 1:
                  print("Parabens, voce recebeu uma quantidade aleatoria de dinheiro")
                  dinheiro = dinheiro + random.randint(10,300)
                  print("Dinheiro atual: ", dinheiro)
            elif loot == 2:
                print("Parabens, voce recebeu um item aleatorio")
                item_recebido = random.choice(itens)
                print(item_recebido)
                print("Voce não tem espaço na mochila, o item foi convertido para o PP equivalente")
                dinheiro = dinheiro+ random.randint(1,100)
        

print("Voce chegou a area do boss")

vida_chefe = 100
print(f' CHECKPOINT - Você encontrou o CHEFE DA INSTÂNCIA. O combate é inevitável.')

while (vida_guerreiro > 0 and vida_chefe > 0):
     
    chance_esquiva = random.randint(0,100)
    ação = int(input('Você deve agir rápido ! \n (1) - Atacar \n (2) - Esquivar \n (3) - Fugir \n'))

    if ação == 1:
        vida_chefe = vida_chefe - dano
        print("O Chefe sofreu dano  \n Vida atual do chefe: ",vida_chefe)
        vida_guerreiro = vida_guerreiro - (10 - (defesa / 10))
        print("Voce tambem foi ferido \n sua vida: ", vida_guerreiro)

    elif ação == 2:
        if chance_esquiva > 50:
                print("esquiva bem sucedida")
        elif chance_esquiva <50:
                print("Esquiva falhou")
                vida_guerreiro = vida_guerreiro - 10
                print("Vida atual: ", vida_guerreiro)

    elif ação == 3:
        print("Chefe: COVARDE!! \n O Chefe, em um ataque de furia, te matou")
        vida_guerreiro = 0
    else:
        print('Comando não reconhecido')


print("final")