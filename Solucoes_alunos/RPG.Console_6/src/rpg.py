dinheiro = 150.0
life = 100
resp = 's'
vida_slime = 25.0
hit_slime = 10.0
hit_heroi = 10.0
espada = 0
hit_espada = 15.0
nomeheroi = input("Digite o seu nome: ")
volta = 0

def retorno():
      caminho = int(input("Para onde deseja ir: \n[1] Mercador \n[2] Floresta \n[3] Castelo Assombrado\n"))


print(f"A jornada começa com o heroi {nomeheroi} com {life} de saúde e {dinheiro} moedas. \n")
while(volta == 0):
    caminho = int(input("Para onde deseja ir: \n[1] Mercador \n[2] Floresta \n[3] Castelo Assombrado\n"))

    if(caminho == 1):
        print("\nVoce achou o mercador: o que deseja comprar?")
        print("\n[1] - Espada        - 150.0")
        print("[2] - Poção de Cura - 75.0")

        while(resp == 's'):

            opc = int(input("Escolha: [1] Espada, [2] Poção\n"))

            if(opc == 1):
                    if (dinheiro < 150.0):
                        print("Saldo indisponivel")
                    else:
                        dinheiro -= 150.0
                        print(f"Saldo: {dinheiro}")
                        espada = 1
                
            elif(opc == 2):
                    if (dinheiro < 75.0):
                        print("Saldo indisponivel")
                    else:
                        dinheiro -= 75.0
                        print(f"Saldo: {dinheiro}")

            resp = input("\nDeseja realizar outra compra? (s) ou (n)? ")

        print("Prazer fazer negocios!")
        retorno()

 

    elif(caminho == 2):
        print("Você chegou à floresta!")
        print("\nVocê encontrou um Slime!")
    while(vida_slime > 0):
        opcoes_slime = int(input("atacar [1]\ncura [2]"))

        if(opcoes_slime == 1):
            if(espada == 1):
                vida_slime -= hit_heroi + hit_espada
                print(f"você causou {hit_heroi + hit_espada} de dano")
            else:
                vida_slime = hit_heroi
