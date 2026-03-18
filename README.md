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

## Funcionalidades

* Menu inicial com interação por teclado
* Sistema de pontuação
* Controle do jogador (teclas ↑ ↓)
* Movimento automático do oponente (IA simples)
* Detecção de colisão da bola com raquetes e paredes
* Condição de vitória

---

## Conceitos Aplicados

### Abstração

O código foi organizado em funções e estruturas que isolam responsabilidades específicas, como:

* Menu principal
* Lógica do jogo
* Renderização

### Separação de Responsabilidades

Cada parte do sistema possui uma função clara:

* Interface (renderização)
* Lógica do jogo
* Controle de entrada

### SOLID (aplicação inicial)

* S: Funções com responsabilidades únicas
* O: Estrutura preparada para expansão
* L: Componentes reutilizáveis sem quebra de comportamento
* I: Separação de funcionalidades
* D: Baixo acoplamento entre partes do código

---

## Tecnologias Utilizadas

* Python 3
* Pygame
* Git e GitHub

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/JvMartelli/pong.git
```

### 2. Acesse a pasta

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install pygame
```

### 4. Execute o projeto

```bash
python main.py
```

---

## Fluxo de Trabalho (Git)

Este projeto segue as seguintes práticas:

* Cada nova funcionalidade é desenvolvida em uma branch específica
* Uso obrigatório de Pull Requests (PRs)
* Merge realizado apenas após validação
* Histórico organizado para avaliação acadêmica

### Exemplo de fluxo:

```bash
git checkout -b feature/nome-da-feature
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin feature/nome-da-feature
```

---

## Possíveis Melhorias

* Adição de efeitos sonoros
* Menu com interface gráfica mais avançada
* Sistema de níveis/dificuldade
* Multiplayer local
* Melhor IA para o oponente
* Animações e partículas

---

## Avaliação

A avaliação do projeto considera:

* Qualidade do código (refatoração)
* Aplicação de boas práticas
* Organização do repositório
* Uso correto de Git
* Implementação de novas features em tempo real


