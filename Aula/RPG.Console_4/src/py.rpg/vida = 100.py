vida = 100.0
dinheiro = 450.0
vida_boss = 110.0

nome_heroi = input("Digite o nome do seu heroi: ")

print("\n O nome do seu heroi é :   " + nome_heroi)
print(" Vida do heroi:  100 HP ")
print(" Dineheiro do heroi:  450  ")

troco = 0.0

print("\n Você tem duas opções de caminho")
print("(1) --> Vila  (2) --> caverna ")

opcao_heroi = int(input("escolha uma opção"))

if (opcao_heroi == 1):
    print("\n Depois de ir para vila você encontrou um mercador")
    resp = input("Deseja comprar algo? (s) ou (n)")

    while (resp == 's'):
        print(" (1) espada R$: 300")
        print(" (2) poção de cura R$: 50")
        print(" (3) sair")

        opcao_item = int(input("\n Escolha um item: \n"))
        if (opcao_item == 1):
            print("Você escolheu a espada")
            if(dinheiro < 300):
                print("Está compra não é possivel")
                break
            dinheiro -= 300
            print(f"Dinheiro atual:  {dinheiro} ") 
        elif (opcao_item == 2):
            print("Você escolheu a poção de cura")
            if(dinheiro < 50):
                print("Está compra não é possivel")
                break
            dinheiro -= 50
            print(f"Dinheiro atual:  {dinheiro} ")  
        else:
            print("Adeus!") 
            break

    print("Depois de conversar com o mercador, voce ouve um rugido distante. ")
    print("Ao se aproximar, voce se depara com um dragão!")   
    

elif (opcao_heroi == 2):
    print("\n Depois de ir para a caverna você encontrou um bau!")
    print("\n Dentro do bau tem uma espada e um arco. Você só pode selecionar 1 item. ")

    opcao_bau = int(input("espada (1) arco (2)  "))
    if (opcao_bau == 1):
        print("Voce pegou a espada!")
    elif (opcao_bau == 2):
        print("Voce pegou o arco!")
    
    print("\n Após voce explorar a caverna e não encontrar nada, voce volta e decide ir para a vila. ")
    print("Chegendo na vila, voce se depara com um dragão! ")

print(f"Vida do boss: {vida_boss}")
print (f"Vida do heroi: {vida}")


print("____________________¶¶__¶_5¶¶")  
print("____________5¶__¶__¶¶_5¶__¶¶¶5")
print("__________5¶¶¶__¶¶5¶¶¶¶¶5¶¶__5¶¶¶5")
print("_________¶¶¶¶__¶5¶¶¶¶¶¶¶¶¶¶¶__5¶¶¶¶5")
print("_______5¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶_5¶¶__5¶¶¶¶¶5")
print("______¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶5¶¶¶__¶¶¶¶5¶5")
print("_____¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶5")
print("____¶¶¶¶¶¶¶_¶¶¶5¶¶¶¶_¶¶¶¶¶5_5¶_¶¶¶¶¶¶¶¶5")
print("___¶¶¶¶¶¶¶¶__5¶¶¶¶¶¶___5¶¶¶¶__5¶¶¶¶¶¶¶¶¶5")
print("__¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶__¶¶5_5¶¶¶¶¶¶¶¶¶¶¶")
print("_5¶¶¶¶¶¶¶¶¶¶¶¶_5¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶5")
print("_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_5¶¶¶¶")
print("5¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶__¶¶¶¶_¶¶¶_¶¶¶¶")
print("¶¶¶¶¶¶¶¶_¶¶5_5¶__¶¶¶¶¶¶¶¶¶5_5¶¶¶_5¶¶¶_5¶¶¶5")
print("¶5¶¶¶¶¶_¶¶_5¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶5_5¶¶_5¶¶¶_¶¶¶5")
print("¶¶¶¶_¶¶__¶__¶¶¶¶¶¶5_5¶¶¶¶¶¶¶¶¶¶_¶¶_5¶¶_5¶¶¶")
print("¶¶¶5_5¶______5¶¶5¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶_5¶_¶5¶")
print("5¶¶____5¶¶¶¶_____¶¶¶¶¶¶¶_¶¶¶¶¶_¶__¶¶_5¶¶")
print("_¶¶__5¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶_¶¶¶¶¶_____¶_¶¶")
print("_¶¶___5¶¶¶¶¶¶¶¶¶__________5¶_¶¶¶¶¶____¶¶_¶¶")
print("_¶¶_______5¶¶¶¶¶¶____________¶¶¶¶¶_____¶_¶¶")
print("_5¶________¶¶_¶¶¶¶________¶¶¶¶¶_______¶¶")
print("__¶¶__________¶___¶¶¶¶¶___¶¶¶¶¶¶_______¶5")
print("__¶¶____________5¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶")
print("___¶________________5¶¶¶¶¶¶¶¶_¶¶")
print("___¶__________5¶¶¶¶¶¶¶¶5¶¶¶__¶5")
print("    _____________________5¶¶¶___¶5 ")

while (vida_boss > 0):
    print("\n Escolha o que usar")
    opcao_boss = int(input("(1) Espada  (2) Arco  (3) Poção de Cura"))

    if (opcao_boss == 1):
        print("\n Voce atacou o dragão e deu 20 de dano!")
        print("\n O dragão te atacou e te deu 10 de dano!")
        vida_boss -= 20
        print(f"\n Vida atual do boss {vida_boss}")
        vida -= 10
        print(f"\n Vida atual do heroi {vida}")
    elif (opcao_boss == 2):
        print("\n Voce atacou o dragão e deu 15 de dano!")
        print("\n O dragão te atacou e te deu 10 de dano!")
        vida_boss -= 15
        print(f"\n Vida atual do boss {vida_boss}")
        vida -= 10
        print(f"\n Vida atual do heroi {vida}")
    elif (opcao_boss == 3):
        print("\n Voce curou 15 de vida!")
        vida += 15
        print(f"\nVida atual do heroi {vida}")

print("\n Parabens!!!! Voce derrotou o Dragão!!!!")
print("\n FIM")
                