import os
from random import randint
from time import sleep
#variaveis
vida = 100.0
moedas = 350.0
opcao = 0
escolha_loja = 5
dano = 5.0
dano_magia = 0
vida_boss = 100.0
ataque_boss = 0
defesa = 10.0
uso_magia = 2
uso_cura = 0
acao = 0


#inicio
nome = str(input("Digite o Nome do heroi: "))
print(f"Saldo:{moedas}")

print("O Heroi se depara com uma bifurcação")
print("""-----Qual caminho o heroi escolhe -----
    [1] Direita
    [2] Esquerda """)
escolha = int(input("Digite o caminho: "))
os.system("cls")
print(f"Vida:{vida}")
print(f"Saldo:{moedas}")


if escolha == 1:
    print("O heroi se depara com um bau!")
    opcao = int(input("""Você deseja abrir o bau? 
[1] Sim
[2] Não
    """))

    if opcao == 1:
        print("-="*20)
        print("Você encontrou uma Poção de cura ")
        print("-="*20)
        sleep(2)
        uso_cura += 1
        os.system("cls")
        print(f"Vida:{vida}")
        print(f"Saldo:{moedas}")
        print("O Heroi segue para a proxima sala")

    elif opcao == 2:
        print("O Heroi decide não abrir o bau")

elif escolha == 2:
    print("O Heroi segue o caminho e se depara com um mercador ")

#Mercador
print("Mercador: Você deseja comprar algo? ")    
opcao = int(input("""[1] Sim 
[2] Não
"""))

if opcao == 1:
    while opcao != 0:
        print("-="*10)
        print("1 - Espada R$150.0 (15 de dano)")
        print("2 - Poção de cura 75.0")
        print ("3- Escudo 175.0 (10 de defesa)")
        print ("0 - Para desistir da compra")

        escolha_loja = int(input("Digite sua escolha: "))
        if opcao == 1:
            print("Você comprou a Espada ")
            moedas -= 150.0
            os.system("cls")
            dano +=  5.0
            print(f"Vida:{vida}")
            print(f"Saldo:{moedas}")
        elif opcao == 2:
            print("Você comprou a Poção de cura")
            moedas -= 75.0
            os.system("cls")
            uso_cura += 1
            print(f"Vida:{vida}")
            print(f"Saldo:{moedas}")
        elif opcao == 3:
            print("Você comprou a Escudo ")
            moedas -= 175.0
            os.system("cls")
            defesa += 10
            print(f"Vida:{vida}")
            print(f"Saldo:{moedas}")
        if moedas <= 0.0:
            print("Saldo insuficiente")
            break

elif opcao == 2:
    print("Ao seguir o caminho o heroi ")

#Encontro com o boss
while vida_boss > 0 and vida > 0:
    os.system("cls")
    print("O Heroi Chega a uma planice e encontra o boss ")
    print("-="*20)
    print(f"Vida {nome}:{vida}")
    print("-="*20)
    print(f"Boss:{vida_boss}")
    print("-="*20)
    print("\n Opções ")
    print("[1] Atacar ")
    if uso_magia > 0: print("[2] Magia ")
    if uso_cura > 0: print("[3] Curar ")
    acao = int(input("Digite a ação: "))

    #Ações do heroi
    if acao == 1:
        vida_boss -= dano
        print(f"Você causou {dano} de dano")

    elif acao == 2:
        dano_magia = randint(5, 15)
        vida_boss -= dano_magia
        uso_magia -= 1
        print(f"Você causou {dano_magia} de dano")

    elif acao == 3:
        if vida == 100:
            print("Sua vida ja está completa: ")
        else:
            vida += 20
    else:
        print("Ação invalida")
    
    input("Pressione Enter...")

    #turno do boss
    if vida_boss > 0:
        ataque_boss = randint(5, 20)
        vida -= ataque_boss
        print(f"O Boss te atacou! e causou {ataque_boss} de dano")
        input("Pressione Enter...")

#Resultado final
os.system("cls")
if vida < 0:
    print("-="*20)
    print("Você perdeu!")
    print("-="*20)
else:
    print("Você ganhou")