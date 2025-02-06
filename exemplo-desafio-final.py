import random
import os

# Variáveis globais
vida_boss = 100
vida_guerreiro = 100
usos_magia = 3
usos_cura = 3
moedas = 500.0
ataque = 0.0
ataque_distancia = 0.0
defesa = 0.0
nome = ""

os.system("cls")
nome = input("Insira o nome do aventureiro: ")
os.system("cls")

print(f"O aventureiro {nome} começou sua aventura e se deparou com uma bifurcação.")
print("O caminho da esquerda leva para um castelo assombrado.")
print("O caminho da direita leva para um pântano sombrio.")

escolha = input(f"\nPor qual caminho {nome} irá seguir: \n[1] Esquerda\n[2] Direita\nResposta: ")
os.system("cls")

if escolha == '1':
    print("Adentrando o Castelo, você encontra um velho afiando uma espada.")
    print("-- O que você faz neste castelo?")
    escolha = input("[1] Estou em busca do meu caminho\n[2] Não é da sua conta\nResposta: ")
    os.system("cls")
    
    if escolha == '1':
        while True:
            print("\n------------------------- LOJA -------------------------")
            print("[1] Espada Grande (10 de Ataque) $400")
            print("[2] Espada Pequena (5 de Ataque) $300")
            print("[3] Arco (5 de Ataque à Distância) $100")
            print("[4] Escudo Grande (10 de Defesa) $200")
            print("[5] Escudo Pequeno (5 de Defesa) $100")
            print(f"\nMoedas: ${moedas}")
            compra = input("Escolha um item ou [6] Sair: ")
            
            if compra == '1' and moedas >= 400:
                moedas -= 400
                ataque += 10
            elif compra == '2' and moedas >= 300:
                moedas -= 300
                ataque += 5
            elif compra == '3' and moedas >= 100:
                moedas -= 100
                ataque_distancia += 5
            elif compra == '4' and moedas >= 200:
                moedas -= 200
                defesa += 10
            elif compra == '5' and moedas >= 100:
                moedas -= 100
                defesa += 5
            elif compra == '6':
                break
            else:
                print("Opção inválida ou moedas insuficientes!")
            
            os.system("cls")
    else:
        print("O velho te expulsa do castelo!")
        input("Pressione Enter para continuar...")

else:
    print("No pântano, você encontra um baú misterioso!")
    escolha = input("[1] Abrir\n[2] Ignorar\nResposta: ")
    if escolha == '1':
        sorte = random.randint(1,4)
        if sorte == 1:
            print("O baú estava vazio!")
        else:
            print("Você encontrou equipamentos!")
            ataque += 5 * (sorte//2)
            defesa += 5 * (sorte//3)
    input("Pressione Enter para continuar...")
    os.system("cls")

# Combate contra o Boss
print("Um monstro gigante aparece!")
print("                         ^                       ^   ") 
print("                         |\   \        /        /|   ")
print("                        /  \  |\__  __/|       /  \  ")
print("                       / /\ \ \ _ \/ _ /      /    \ ")
print("                      / / /\ \ {*}\/{*}      /  / \ \    ")
print("                      | | | \ \( (00) )     /  // |\ \   ")
print("                      | | | |\ \(V""V)\    /  / | || \|  ")
print("                      | | | | \ |^--^| \  /  / || || ||  ")
print("                     / / /  | |( WWWW__ \/  /| || || ||  ")
print("                    | | | | | |  \______\  / / || || || ")
print("                    | | | / | | )|______\ ) | / | || ||  ")
print("                    / / /  / /  /______/   /| \ \ || ||  ")
print("                   / / /  / /  /\_____/  |/ /__\ \ \ \ \ ")
print("                   | | | / /  /\______/    \   \__| \ \ \ ")
print("                   | | | | | |\______ __    \_    \__|_| \ ")
print("                   | | ,___ /\______ _  _     \_       \  |  ")
print("                   | |/    /\_____  /    \      \__     \ |    /\ ")
print("                   |/ |   |\______ |      |        \___  \ |__/  \ ")
print("                   v  |   |\______ |      |            \___/     | ")
print("                      |   |\______ |      |                    __/ ")
print("                       \   \________\_    _\               ____/  ")
print("                     __/   /\_____ __/   /   )\_,      _____/    ")
print("                    /  ___/  \ uuuu /  ___/___)    \______/    ")
print("                    VVV  V        VVV  V     ")
input("Pressione Enter para continuar...")
os.system("cls")    

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
        dano = random.randint(10 + int(ataque), 20 + int(ataque))
        vida_boss -= dano
        print(f"Você causou {dano} de dano!")
    elif acao == '2' and usos_cura > 0:
        vida_guerreiro = min(100, vida_guerreiro + 30)
        usos_cura -= 1
        print("Você se curou!")
    elif acao == '3' and usos_magia > 0:
        vida_boss -= random.randint(20, 40)
        usos_magia -= 1
        print("Magia poderosa!")
    else:
        print("Ação inválida!")
    
    input("Pressione Enter...")
    
    # Turno do Boss
    if vida_boss > 0:
        dano_boss = random.randint(15, 25)
        vida_guerreiro -= dano_boss
        print(f"O Boss te atacou causando {dano_boss} de dano!")
        input("Pressione Enter...")

# Resultado final
os.system("cls")
if vida_guerreiro <= 0:
    print("""
  ____    _    __  __ _____    _____     _______ ____   
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \  
| |  _  / _ \ | |\/| |  _|   | | | \ \ V /|  _| | |_) | 
| |_| |/ ___ \| |  | | |___  | |_| | | | | |___|  _ <  
 \____/_/   \_\_|  |_|_____|  \___/  |_| |_____|_| \_\  
""")
else:
    print("""
    ___________   
   '._==_==_=_.'   
   .-\\:      /-.   
  | (|:.     |) |  
   '-|:.     |-'    
     \\::.    /     
      '::. .'       
        ) (        
      _.' '._      
     `\"\"\"\"\"\"\"`     
VOCÊ DERROTOU O MONSTRO!""")

print("Obrigado por jogar!")