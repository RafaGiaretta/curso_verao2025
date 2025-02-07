import random
import os
vida_boss= 120
vida_guerreiro=110
usos_cura = 4
moedas = 500
ataque = 0.0
ataque_a_distancia = 0.0
ataque_do_boss = 23.0
usos_magia = 5
nome = ""













print("Seus olhos se abrem, revelando um ambiente escuro e assustador, voce presume que possa ser uma caverna")
print("\n Voce consegue enxergar duas opcoes de escolha, uma luz do que parece ser uma saida, ou adentrar os confins da caverna")
print("\n1 - Sair da Caverna ")
print("2 - Adentrar a Caverna")

opcao_escolhida = int(input("\n O que voce escolhe? "))

if (opcao_escolhida == 1):
    print("Voce escolheu sair da caverna")
    print("\nTentando buscar a saída, voce e surpreendido por pedras que desmoronam fechando sua passagem")
    print("Com isso apenas restou adentrar a caverna")
    input("Pressione enter para continuar")
    
else:
    print("Voce se enche da coragem que imagina ter, e segue em frente na escura caverna")

print("\nApos andar sem rumo algum, guiado por seus instintos primitivos, voce se depara com o que parece ser um homem bem ferido, que pergunta")
nome1 = input("Ei rapaz, Qual o seu nome? ")
print("Tome muito cuidado com a casa na floresta " + nome1 )
print("Logo em seguida o homem ferido acaba falecendo e deixando os seguintes itens ")
print("1- Armadura leve (2 CA)[armor class]")
print("1- tocha")
print("1- espada curta")
print("1- escudo pesado(3 CA)[armor class]")
input("\n Pressione enter para continuar")

print("Seguindo adiante voce se encontrar com uma saida da caverna escura, voce se depara com uma floresta densa e iluminada, ao fundo voce se depara com 2 opçoes")
print("1- Uma casa abandonada")
print("2- Uma fumaça ao longe")

local_ir = int(input("Para onde ira: "))

if(local_ir == 1):
    print("Voce se depara com uma criatura mistica: ")
        
    print("""
                                ,-.
        ___,---.__          /'|`\          __,---,___
        ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
    ,'        |           ~'\     /`~           |        `.
    /      ___//              `. ,'          ,  , \___      \
    |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
    |   /          /\_  `   .    |    ,      _/\          \   |
    \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
    \  \           | `._   `\\  |  //'   _,' |           /  /
    `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
        ``       /     \    ,='/ \`=.    /     \       ''
                |__   /|\_,--.,-.--,--._/|\   __|
                /  `./  \\`\ |  |  | /,//' \,'  \
    eViL        /   /     ||--+--|--+-/-|     \   \
            |   |     /'\_\_\ | /_/_/`\     |   |
                \   \__, \_     `~'     _/ .__/   /
                `-._,-'   `-._______,-'   `-._,-'

    """)

    input("Pressione enter para batalhar")

    while vida_boss > 0 and vida_guerreiro > 0:
        # Turno do jogador
        os.system("cls")
        print(f"Vida do Boss: {vida_boss}")
        print(f"Sua Vida: {vida_guerreiro}")
        print("\nOpções:")
        print("[1] Atacar")
        if usos_cura > 0: print("[2] Curar")
        if usos_magia > 0: print("[3] Magia")
        
        acao = input("Escolha: ")
        
        # Ação do jogador
        if acao == '1':
            ataque = 3 + ataque
            vida_boss -= ataque
            print(f"Você causou {ataque} de dano!")
        elif acao == '2' and usos_cura > 0:
            vida_guerreiro +=  40
            usos_cura -= 1
            print("Você se curou!")
        elif acao == '3' and usos_magia > 0:
            vida_boss -= 30
            usos_magia -= 1
            print("Magia poderosa!")
        else:
            print("Ação inválida!")
        
        input("Pressione Enter...")
        
        # Turno do Boss
        if vida_boss > 0:
            dano_boss = ataque_do_boss
            vida_guerreiro -= dano_boss
            print(f"O Boss te atacou causando {dano_boss} de dano!")
            input("Pressione Enter...")

        # Resultado final
        os.system("cls")
        if vida_guerreiro <= 0:
            print(" voce foi derrotado")

elif(local_ir == 2):
    print("Voce encontra uma pequena caravana com um velho")
    print(" O veho te ve e se apresenta")
    print("Ola jovem aventureiro, meu nome é Hepistenio e o seu ?")
    print("Meu nome e "( + nome1 ) )