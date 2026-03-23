# Pong Game - Refatorado com Boas Práticas

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## Sobre o Projeto

Este projeto consiste na implementação do clássico jogo Pong, desenvolvido em Python utilizando a biblioteca Pygame.

O foco principal não é apenas o jogo em si, mas sim a aplicação de conceitos fundamentais de Engenharia de Software, como:

* Refatoramento de código
* Separação de responsabilidades
* Aplicação de princípios SOLID
* Organização e versionamento com Git

---

## Objetivo do Trabalho

O objetivo deste trabalho é refatorar um código existente, melhorando sua estrutura e qualidade com base nos seguintes critérios:

* Abstração
* Separação de responsabilidades
* Aplicação de princípios SOLID
* Legibilidade
* Documentação

Além disso, o projeto deve seguir boas práticas de desenvolvimento com Git, incluindo uso de branches e Pull Requests.

---

## Estrutura do Projeto

```
pong/
├── main.py            # Ponto de entrada da aplicação
├── settings.py        # Constantes e configurações globais
├── game.py            # Orquestrador do loop e fluxo de cenas
├── ball.py            # Entidade: bola (posição, movimento, colisão)
├── paddle.py          # Entidade: raquete (posição, limites)
├── scoreboard.py      # Estado e regras do placar
├── ai_controller.py   # Lógica de controle da IA
├── renderer.py        # Toda a lógica de desenho
└── .gitignore         # Arquivos ignorados pelo Git
```

---

## Funcionalidades

* Menu inicial com interação por teclado
* Sistema de pontuação
* Controle do jogador (teclas ↑ ↓)
* Movimento automático do oponente (IA simples)
* Detecção de colisão da bola com raquetes e paredes
* Tela de vitória com opção de reiniciar ou voltar ao menu
* Condição de vitória

---

## Controles

| Ação             | Tecla  |
|------------------|--------|
| Mover para cima  | ↑      |
| Mover para baixo | ↓      |
| Iniciar jogo     | Espaço |
| Jogar novamente  | Espaço |
| Voltar ao menu   | ESC    |

---

## Conceitos Aplicados

### Abstração

O código foi organizado em classes que representam conceitos reais do jogo:

* `Bola` — encapsula posição, velocidade e comportamento de colisão
* `Raquete` — encapsula posição e limites de movimento
* `Placar` — encapsula pontuação e condição de vitória
* `ControladorIA` — encapsula a lógica de decisão da IA
* `Renderer` — encapsula toda a lógica de desenho

### Separação de Responsabilidades

Cada arquivo possui uma única responsabilidade clara:

* `renderer.py` — único arquivo que chama `pygame.draw`
* `scoreboard.py` — único que conhece a pontuação necessária para vencer
* `ai_controller.py` — único que decide como a IA se move
* `game.py` — coordena as entidades, sem saber como desenhá-las

### SOLID

**S — Single Responsibility:** cada classe tem exatamente uma razão para mudar. `Bola` muda se a física mudar; `Renderer` muda se o visual mudar — nunca os dois juntos.

**O — Open/Closed:** para adicionar uma IA com dificuldade diferente, basta criar uma nova classe em `ai_controller.py` sem modificar o código existente.

**L — Liskov Substitution:** `ControladorIA` pode ser substituída por qualquer outro controlador sem impacto em `game.py`.

**I — Interface Segregation:** as classes recebem apenas o que precisam. A IA recebe `Raquete` e `Bola`, não o objeto `Jogo` inteiro.

**D — Dependency Inversion:** `Jogo` depende das entidades (`Bola`, `Raquete`), não de lógica concreta de desenho ou IA.

---

## Tecnologias Utilizadas

* Python 3
* Pygame
* Git e GitHub

