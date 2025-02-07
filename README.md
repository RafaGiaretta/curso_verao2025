# 🏹 Projeto RPG Console - Teste Técnico - Bootcamp Introdução a Engenharia de software

## 🎯 Descrição do Projeto
Este projeto tem como objetivo desafiar os alunos a desenvolverem um jogo de RPG baseado em texto, utilizando **Python** ou **C**, aplicando conceitos fundamentais da programação e lógica.

Os alunos formarão **grupos de 4 pessoas** e deverão primeiro criar um **fluxograma** representando a lógica do jogo e uma breve documentacao, antes de iniciar a implementação.

---

## 📜 Regras de Negócio
1. O jogo deve ter um **herói** com atributos:
   - **Vida** (exemplo: 100 HP)
   - **Dinheiro** (exemplo: 50 moedas)
2. Durante o jogo, o herói poderá encontrar:
   - **Um mercador**, onde poderá comprar equipamentos
   - **Um baú**, que pode conter ouro ou equipamentos
3. O jogador poderá **comprar equipamentos** para melhorar suas chances contra o chefe final.
4. O jogo deve terminar com uma **batalha contra o chefe**, que também possui **vida** e deve ser derrotado para vencer.

---

## 🏗️ Estrutura do Projeto
O projeto deve seguir a seguinte estrutura básica:

```
📁 rpg_console
 ├── 📜 Alunos.txt
 ├── 📜 fluxograma.png (imagem do fluxograma do grupo)
 ├── 📂 src
 │   ├── rpg.py  (se em Python)
 │   ├── rpg.c   (se em C)
 ├── 📂 docs
 │   ├── regras_negocio.txt (explicação das regras)
```

---

## 🎮 Fluxo Básico do Jogo
1. O jogo inicia e exibe a **vida e dinheiro do herói**.
2. O jogador se move e encontra **eventos aleatórios** (mercador ou baú).
3. No mercador, o jogador pode gastar dinheiro para comprar equipamentos.
4. No baú, o jogador pode ganhar dinheiro ou itens.
5. O jogo finaliza com uma **batalha contra o chefe**, onde as decisões do jogador influenciam o resultado.

---

## 🛠️ Tecnologias
- Linguagens: **Python ou C**
- Entrada e saída via **console** (sem interface gráfica)

---

## 📌 Requisitos
- O código deve ser modularizado (evite tudo em um único bloco de código).
- Utilize **estruturas condicionais** (`if, else`) e **laços de repetição** (`for, while`).
- O jogo deve **exibir mensagens claras** para o jogador durante o fluxo.
- O código deve ser **bem comentado**, para facilitar a compreensão.

---

## 🚀 Como Começar
1. Forme seu grupo e crie o **fluxograma do jogo** antes de começar a programar.
2. Crie sua documentacao.
3. Escolha a linguagem: **Python ou C**.
4. Crie o arquivo principal (`rpg.py` ou `rpg.c`).
5. Desenvolva o jogo seguindo as **regras de negócio**.
6. Teste e ajuste o código conforme necessário.
7. Salve os arquivos como descrito na Estrutura do Projeto.

💡 **Dica:** Divida as tarefas entre os membros do grupo para facilitar o desenvolvimento!

---

## 📢 Entrega
- O grupo deve **adicionar o fluxograma e a documentacao** ao repositorio.
- O jogo deve rodar corretamente no console.
- O código deve estar organizado e comentado.

---

Boa sorte e divirtam-se programando! 🚀
