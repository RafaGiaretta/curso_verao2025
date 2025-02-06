#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Variáveis globais
int vida_boss = 100;
int vida_guerreiro = 100;
int usos_magia = 3;
int usos_cura = 3;
float moedas = 500.0;
int ataque = 0;
int ataque_distancia = 0;
int defesa = 0;
char nome[50];

void limparTela() {
    system("cls");
}

int main() {
    limparTela();
    
    printf("Insira o nome do aventureiro: ");
    fgets(nome, 50, stdin);
    nome[strcspn(nome, "\n")] = 0;
    system("cls");

    printf("O aventureiro %s comecou sua aventura e se deparou com uma bifurcacao.\n", nome);
    printf("O caminho da esquerda leva para um castelo assombrado.\n");
    printf("O caminho da direita leva para um pantano sombrio.\n");

    int escolha;
    printf("\nPor qual caminho %s ira seguir: \n[1] Esquerda\n[2] Direita\nResposta: ", nome);
    scanf("%d", &escolha);
    system("cls");

    if(escolha == 1) {
        printf("Adentrando o Castelo, voce encontra um velho afiando uma espada.\n");
        printf("-- O que voce faz neste castelo?\n");
        printf("[1] Estou em busca do meu caminho\n[2] Nao e da sua conta\nResposta: ");
        scanf("%d", &escolha);
        system("cls");

        if(escolha == 1) {
            while(1) {
                printf("\n------------------------- LOJA -------------------------\n");
                printf("[1] Espada Grande (10 de Ataque) $400\n");
                printf("[2] Espada Pequena (5 de Ataque) $300\n");
                printf("[3] Arco (5 de Ataque a Distancia) $100\n");
                printf("[4] Escudo Grande (10 de Defesa) $200\n");
                printf("[5] Escudo Pequeno (5 de Defesa) $100\n");
                printf("\nMoedas: $%.2f\n", moedas);
                printf("Escolha um item ou [6] Sair: ");

                int compra;
                scanf("%d", &compra);

                if(compra == 1 && moedas >= 400) {
                    moedas -= 400;
                    ataque += 10;
                    printf("Voce comprou a Espada Grande!\n");
                }
                else if(compra == 2 && moedas >= 300) {
                    moedas -= 300;
                    ataque += 5;
                    printf("Voce comprou a Espada Pequena!\n");
                }
                else if(compra == 3 && moedas >= 100) {
                    moedas -= 100;
                    ataque_distancia += 5;
                    printf("Voce comprou o Arco!\n");
                }
                else if(compra == 4 && moedas >= 200) {
                    moedas -= 200;
                    defesa += 10;
                    printf("Voce comprou o Escudo Grande!\n");
                }
                else if(compra == 5 && moedas >= 100) {
                    moedas -= 100;
                    defesa += 5;
                    printf("Voce comprou o Escudo Pequeno!\n");
                }
                else if(compra == 6) {
                    break;
                }
                else {
                    printf("Opcao invalida ou moedas insuficientes!\n");
                }
                getchar();
            }
        }
        else {
            printf("O velho te expulsa do castelo!\n");
            getchar();
        }
    }
    else {
        printf("No pantano, voce encontra um bau misterioso!\n");
        printf("[1] Abrir\n[2] Ignorar\nResposta: ");
        scanf("%d", &escolha);
        
        if(escolha == 1) {
            printf("Voce encontrou equipamentos!\n");
            ataque += 5;
            defesa += 5;
        }
        getchar();
        system("cls");
    }
    
	getchar();
	limparTela();
		
	printf("Voce caminha por um caminho escuro e ouve um barulho estrondeante, parece uma mistura de trovao com rugido!\n");
    
    printf("\nUm monstro gigante aparece!\n");
    
    printf("                         ^                       ^  			 	  \n");
    printf("                         |\\   \\        /        /|   			      \n");
    printf("                        /  \\  |\\__  __/|       /  \\  		      \n");
    printf("                       / /\\ \\ \\ _ \\/ _ /      /    \\ 		  	  \n");
    printf("                      /  / \\ \\ {*}\\/{*}      /  / \\ \\  		  \n");
    printf("                      | | | \\ \\( (00) )     /  // |\\ \\   		  \n");
    printf("                      | | | |\\ \\(V\"\"V)\\    /  / | || \\|         \n");
    printf("                      | | | | \\ |^--^| \\  /  / || || ||  			  \n");
    printf("                     / / /  | |( WWWW__ \\/  /| || || ||  			  \n");
    printf("                    | | | | | |  \\______\\  / / || || || 			  \n");
    printf("                    | | | / | | )|______\\ ) | / | || ||  		      \n");
    printf("                    / / /  / /  /______/   /| \\ \\ || ||             \n");
    printf("                   / / /  / /  /\\_____/  |/ /__\\ \\ \\ \\ \\        \n");
    printf("                   | | | / /  /\\______/    \\   \\__| \\ \\ \\       \n");
    printf("                   | | | | | |\\______ __    \\_    \\__|_| \\        \n");
    printf("                   | | ,___ /\\______ _  _     \\_       \\  |        \n");
    printf("                   | |/    /\\_____  /    \\      \\__     \\ |    /\\\n");
    printf("                   |/ |   |\\______ |      |        \\___  \\ |__/  \\\n");
    printf("                   v  |   |\\______ |      |            \\___/     |  \n");
    printf("                      |   |\\______ |      |                    __/   \n");
    printf("                       \\   \\________\\_    _\\               ____/  \n");
    printf("                     __/   /\\_____ __/   /   )\\_,      _____/       \n");
    printf("                    /  ___/  \\ uuuu /  ___/___)    \\______/         \n");
    printf("                    VVV  V        VVV  V    						  \n");
    
    printf("\nVoce esta pronto para enfrentar o Boss! %s esta com %d de vida e %d adicional de ataque.\n", nome, vida_guerreiro, ataque);
    
    getchar();
    system("cls");

    while(vida_boss > 0 && vida_guerreiro > 0) {
        printf("Vida do Boss: %d\n", vida_boss);
        printf("Sua Vida: %d\n", vida_guerreiro);
        printf("\nOpcoes:\n");
        printf("[1] Atacar\n");
        if(usos_cura > 0) printf("[2] Curar\n");
        if(usos_magia > 0) printf("[3] Magia\n");

        int acao;
        printf("Escolha: ");
        scanf("%d", &acao);

        // Ação do jogador
        if(acao == 1) {
            int dano = 15 + ataque;
            vida_boss -= dano;
            printf("Voce causou %d de dano!\n", dano);
        }
        else if(acao == 2 && usos_cura > 0) {
            vida_guerreiro = (vida_guerreiro + 30 > 100) ? 100 : vida_guerreiro + 30;
            usos_cura--;
            printf("Voce se curou!\n");
        }
        else if(acao == 3 && usos_magia > 0) {
            int dano_magia = 30;
            vida_boss -= dano_magia;
            usos_magia--;
            printf("Magia poderosa! Causou %d de dano!\n", dano_magia);
        }
        else {
            printf("Acao invalida!\n");
        }

        getchar();
        getchar();
      	system("cls");

        // Turno do Boss
        if(vida_boss > 0) {
            int dano_boss = 23;
            vida_guerreiro -= dano_boss;
            printf("O Boss te atacou causando %d de dano!\n", dano_boss);
            getchar();
            system("cls");
        }
    }

    limparTela();
    if(vida_guerreiro <= 0) {
        printf("  ____    _    __  __ _____    _____     _______ ____        \n");
        printf(" / ___|  / \\  |  \\/  | ____|  / _ \\ \\   / / ____|  _ \\  \n");
        printf("| |  _  / _ \\ | |\\/| |  _|   | | | \\ \\ V /|  _| | |_) |  \n");
        printf("| |_| |/ ___ \\| |  | | |___  | |_| | | | | |___|  _ <       \n");
        printf(" \\____/_/   \\_\\_|  |_|_____|  \\___/  |_| |_____|_| \\_\\ \n");
    }
    else {
        printf("    ___________   		 \n");
        printf("   '._==_==_=_.'   		 \n");
        printf("   .-\\\\:      /-.   	 \n");
        printf("  | (|:.     |) |  		 \n");
        printf("   '-|:.     |-'   		 \n");
        printf("     \\\\::.    /    	 \n");
        printf("      '::. .'      		 \n");
        printf("        ) (       		 \n");
        printf("      _.' '._     		 \n");
        printf("     `\"\"\"\"\"\"\"`    \n");
        printf("VOCE DERROTOU O MONSTRO! \n");
    }

    printf("Obrigado por jogar!\n");
    return 0;
}
