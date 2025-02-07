import random
import os
import sys


mensagem_de_erro = ""

vida_guerreiro = 100.0
vida_boos = 200.0
multiplicador_ataque = 1.0

classe_guerreiro = ""
nome_guerreiro = ""

caminho_selecionado = ""

tem_chance_de_dar_critico = False
tem_chance_de_completar_a_vida = False

tem_pocao_de_buff = False
numero_pocoes_cura = 1


#Inicio do Jogo
os.system("cls")
nome_guerreiro = input("Digite o nome do guerreiro: ")
os.system("cls")

while(True):
    #Escolhe a classe do guerreiro
    print(mensagem_de_erro)
    classe_guerreiro = input("Escolha a classe do guerreiro: \n1- Guerreiro implacável \n2- Paladino da vingança\n")
    if(classe_guerreiro == '1'):
        classe_guerreiro = "Guerreiro implacável"
        tem_chance_de_dar_critico = True
        mensagem_de_erro = ""
        break
    elif(classe_guerreiro == '2'):
        classe_guerreiro = "Paladino da vingança"    
        tem_chance_de_completar_a_vida = True
        mensagem_de_erro = ""
        break
    else:
        mensagem_de_erro = "Opção inválida! Tente novamente"
        os.system("cls")

os.system("cls")
print(f"O {classe_guerreiro} {nome_guerreiro} começa a seguir o seu caminho em busca de vingança pelo falecimento de sua amada Hannah pelas mãos de Morgoth")
print(f"O {classe_guerreiro} se encontra no Portão Principal de Mordor")
while(True):
    #O Guerreiro precisa decidir para onde ir
    print(mensagem_de_erro)
    caminho_selecionado = input("Ele pode ir para:\n 1- A Torre do Mago Negro\n 2- A Torre principal\n")
    if(caminho_selecionado == '1'):

        os.system("cls")
        print(f"{nome_guerreiro} escolheu ir para a Torre do Mago Negro")
        print(f"Dentro da Torre do Magro negro, {nome_guerreiro} encontra um Velho Vestindo uma túnica")
        deseja_comprar_pocoes = input("O velho pergunta: Deseja comprar poções? Sim (S) - Não(N) ")

        if(deseja_comprar_pocoes == 'S'):
            os.system("cls")
            pocao_escolhida = input("Qual poção: 1-Poção de Buff 2-Poção de Cura Extra")
            if(pocao_escolhida == '1'):
                tem_pocao_de_buff = True
            else:
                numero_pocoes_cura+=1
            os.system("cls")

        
        deseja_lutar_na_torre = input("O velho também pergunta: Deseja lutar na torre principal? Sim (S) - Não(N)")
        if(deseja_lutar_na_torre == 'S'):

            print("Você encontrou o Morgoth, acabe com ele!")
            print('''
............................................................
..........................*...=.............................
.........................:%:-:-:............................
.........................-#*+%*+:...........................
..........................%=+*.+:...........................
.........-:.:...........:.=@@-+.:...........................
.........+*+.*.........-=-=%@%#*..---=......................
.........-#::-.......:##++=%@@+:+*%%=:=.....................
..........=*:........*@@*##*@%%+:@@@+-......................
...........-%#:-=..*+*#@*:-:-.:=.-@@+:......................
.............-@**--#%@@@@@#-.:. *@%+=-......................
...............%@@@@#@@@@*+--   *-@@%=......................
.................-..-*@@@@#:-   -+=@@+-.....................
....................-#@@@@#--   .+-@@@-::...................
....................*@%@@@#+.    ::@@@@%--..................
....................@@#@@%+=.-:.--.+@@+@%**.................
...................:@#@%@#=:=@.=.@+-%%@-*@-:................
..... ..............=%#@@*=.-#*:.%#++%-@%#+:................
......................:-%=.:%#-.:+%:=@@+@*#:................
.......................:+=:=++%:.++#-*@@@%:.:...............
........................=*:@@=#=.++@%*@@@:%=................
........................:=*%***-*-@@@@@@@#*=:  :............
.........................=@+-=@#+##:.=@@@@:+=. .:...........
..........................@+  @@@@@: -@%%@* ==.  :..........
..........................@@*-.=@@@#.=+  ..  +-  ...........
..........................@@- . @@@%.:       :+-  :.........
.........................:@@+.: -@@#-:        .=- ..........
..........................*@#-:  :@#::         =#:-:........
..........................:@%..  .*%-:  .+=-...**++::.......
............................@*-:..-@+::.. ....:+=++:- ......
............................@@--..#@=-..........:+:+-.......
............................@@*:..+@%#:..........::.:.......
............................@#*-..+@@=-.....................
...........................:@%-::..#@*::....................
............................:+=:............................
............................................................
''')
            while(vida_boos > 0):
                print(f"Seu HP: {vida_boos}")
                opcao = input("1- Atacar 2-Se curar 3-Usar poção buff")
                if(opcao == '1'):
                    print("Voce atacou o boss!")
                    vida_boos -= 40 * multiplicador_ataque
                    print(f"Vida do boss: {vida_boos}")
                elif(opcao == '2'):
                    vida_guerreiro += 40
                else:
                    multiplicador_ataque += 0.05 
            print("Você matou o Boss e salvou a alma da sua amada Hannah, a qual estava aprisionada na chama universal!")
            print('''
      .:=+****++++=-.      
-:::: ---::-----::--- .::::
-===-.---====:::::---.----:
-:   =---====:::::=---   ::
=:- : ---====:::::=--   ::-
 -:-   --====::::---   -:- 
  --:  ---===::::---  ::-  
     ---:--==:::--::--     
          -------          
:.:::       ::. .  :: ::-: 
            =-:            
            =-:            
            =-:            
    .:      =-:          ..
    .   ++----:::++     . .
       +++++++++++++       
       ###+++++++###       
       ###-------###       
       #######***###  
''')

        else:
            vida_minion_1 = 50
            vida_minion_2 = 50
            vida_minion_3 = 50

            a = input("Você encontra três gollums a sua frente...")   
            os.system("cls")
            while(vida_minion_1 > 0 or vida_minion_2 > 0 or vida_minion_3 > 0):
                minion_atacado = input(f"Qual gollum atacar?")
                if(minion_atacado == '1'):
                    print("Atacando o gollum falante\n")
                    vida_minion_1 -= 40
                elif(minion_atacado == '2'):
                    print("Atacando gollum cego\n")
                    vida_minion_2 -= 40
                else:
                    print("Atacando gollum mudo\n")
                    vida_minion_3 -= 40

            #Como os 3 minions foram derrotados o guerreiro ganha um boost no ataque
            os.system("cls")
            multiplicador_ataque += 0.1

            print("Você encontrou o Morgoth, acabe com ele!")
            print('''
............................................................
..........................*...=.............................
.........................:%:-:-:............................
.........................-#*+%*+:...........................
..........................%=+*.+:...........................
.........-:.:...........:.=@@-+.:...........................
.........+*+.*.........-=-=%@%#*..---=......................
.........-#::-.......:##++=%@@+:+*%%=:=.....................
..........=*:........*@@*##*@%%+:@@@+-......................
...........-%#:-=..*+*#@*:-:-.:=.-@@+:......................
.............-@**--#%@@@@@#-.:. *@%+=-......................
...............%@@@@#@@@@*+--   *-@@%=......................
.................-..-*@@@@#:-   -+=@@+-.....................
....................-#@@@@#--   .+-@@@-::...................
....................*@%@@@#+.    ::@@@@%--..................
....................@@#@@%+=.-:.--.+@@+@%**.................
...................:@#@%@#=:=@.=.@+-%%@-*@-:................
..... ..............=%#@@*=.-#*:.%#++%-@%#+:................
......................:-%=.:%#-.:+%:=@@+@*#:................
.......................:+=:=++%:.++#-*@@@%:.:...............
........................=*:@@=#=.++@%*@@@:%=................
........................:=*%***-*-@@@@@@@#*=:  :............
.........................=@+-=@#+##:.=@@@@:+=. .:...........
..........................@+  @@@@@: -@%%@* ==.  :..........
..........................@@*-.=@@@#.=+  ..  +-  ...........
..........................@@- . @@@%.:       :+-  :.........
.........................:@@+.: -@@#-:        .=- ..........
..........................*@#-:  :@#::         =#:-:........
..........................:@%..  .*%-:  .+=-...**++::.......
............................@*-:..-@+::.. ....:+=++:- ......
............................@@--..#@=-..........:+:+-.......
............................@@*:..+@%#:..........::.:.......
............................@#*-..+@@=-.....................
...........................:@%-::..#@*::....................
............................:+=:............................
............................................................
''')
            while(vida_boos > 0):
                print(f"Seu HP: {vida_boos}")
                opcao = input("1- Atacar 2-Se curar 3-Usar poção buff")
                if(opcao == '1'):
                    print("Voce atacou o boss!")
                    vida_boos -= 40 * multiplicador_ataque
                    print(f"Vida do boss: {vida_boos}")
                elif(opcao == '2'):
                    vida_guerreiro += 40
                else:
                    multiplicador_ataque += 0.05 
            print("Você matou o Boss e salvou a alma da sua amada Hannah que estava aprisionada na chama universal!")
            print('''
      .:=+****++++=-.      
-:::: ---::-----::--- .::::
-===-.---====:::::---.----:
-:   =---====:::::=---   ::
=:- : ---====:::::=--   ::-
 -:-   --====::::---   -:- 
  --:  ---===::::---  ::-  
     ---:--==:::--::--     
          -------          
:.:::       ::. .  :: ::-: 
            =-:            
            =-:            
            =-:            
    .:      =-:          ..
    .   ++----:::++     . .
       +++++++++++++       
       ###+++++++###       
       ###-------###       
       #######***###  
''')
        break
    elif(caminho_selecionado == '2'):
        os.system("cls")
        print(f"{nome_guerreiro} escolheu ir para a Torre Principal")
        break
    else:
        mensagem_de_erro = "Opção inválida! Tente novamente"
        os.system("cls")
