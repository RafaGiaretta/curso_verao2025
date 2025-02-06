# Jogo de Aventura - Teste Final

## Objetivo

O objetivo deste jogo de aventura é que o jogador tome decisões ao longo de sua jornada, o que influenciará diretamente em seu progresso e enfrentamento de desafios. O sistema de combate inclui um "Boss" final, onde o jogador pode usar ataques, magias e curas para vencer. A escolha de itens durante o jogo impacta diretamente as habilidades do jogador.

## Estrutura do Jogo

O jogo é dividido em algumas seções principais:

### 1. Introdução

- O jogador insere seu nome.
- O personagem se depara com uma bifurcação e deve escolher entre dois caminhos.

### 2. Caminho 1: Castelo Assombrado

- O jogador encontra um velho afiando uma espada.
- O jogador pode optar por comprar itens em uma loja utilizando moedas, o que influencia em sua força de ataque e defesa.

### 3. Caminho 2: Pântano Sombrio

- O jogador encontra um baú misterioso que oferece itens que aumentam ataque e defesa.

### 4. Combate com o Boss

- O jogador deve enfrentar o Boss utilizando ataques, magia e cura, com a saúde do Boss e do guerreiro sendo monitoradas durante o combate.

## Requisitos Funcionais

### 1. Entrada de Dados

- O nome do jogador.
- A escolha de caminhos e ações durante a aventura.

### 2. Inventário

- O jogador pode comprar itens como espadas, arcos, e escudos com moedas.
- Os itens afetam o ataque e defesa do jogador.

### 3. Sistema de Combate

- O jogador pode atacar, usar magia ou se curar.
- O Boss possui uma quantidade de vida que diminui conforme os ataques do jogador.

### 4. Condições de Vitória e Derrota

- O jogo termina quando o Boss ou o guerreiro morre.

## Fluxograma

### Fluxo de Ações

1. **Início do Jogo**

   - Recebe o nome do jogador.
   - Escolha do caminho (Esquerda ou Direita).

2. **Escolha de Itens** (Somente no Castelo)

   - Apresentação de uma loja com opções de compra.
   - Atualização dos atributos do jogador (ataque e defesa).

3. **Encontro com o Boss**

   - Jogador escolhe suas ações (atacar, curar, magia).
   - Boss realiza um ataque após a ação do jogador.

4. **Final do Jogo**
   - Se o guerreiro morre: derrota.
   - Se o Boss morre: vitória.

## Requisitos Não Funcionais

- O jogo deve ser executado de maneira fluida, sem travamentos.
- O sistema de batalha deve ser dinâmico e apresentar desafios.

## Desenvolvimento

### Linguagem: C ou Python\*

- Uso de variáveis globais para monitorar o estado do jogo (vida, moedas, itens).

### Estrutura de Dados

- Variáveis para controle de vida, moedas, e ataques do jogador.
- Sistema de compra de itens que afeta o estado do jogador.

## Como Rodar

1. Baixe ou clone o repositório.
2. Compile o código utilizando um compilador C.
3. Execute o programa no terminal.
