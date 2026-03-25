import pygame
from settings import LARGURA, ALTURA, PRETO, BRANCO, CINZA
from paddle import Raquete
from scoreboard import Placar


class Renderer:

    def __init__(self, tela: pygame.Surface):
        self.tela = tela
        self.fonte_placar = pygame.font.SysFont(None, 48)
        self.fonte_titulo = pygame.font.SysFont(None, 80)
        self.fonte_media = pygame.font.SysFont(None, 36)
        self.fonte_pequena = pygame.font.SysFont(None, 28)

    def limpar(self):
        self.tela.fill(PRETO)

    def desenhar_linha_central(self):
        segmento = 20
        espaco = 10
        for y in range(0, ALTURA, segmento + espaco):
            pygame.draw.rect(self.tela, CINZA, (LARGURA // 2 - 2, y, 4, segmento))

    def desenhar_placar(self, placar: Placar):
        texto = self.fonte_placar.render(
            f"{placar.pontos_j1}   {placar.pontos_j2}", True, BRANCO
        )
        self.tela.blit(texto, texto.get_rect(center=(LARGURA // 2, 30)))

    def desenhar_jogo(self, bolas: list, raquete1: Raquete, raquete2: Raquete, placar: Placar):
        self.limpar()
        self.desenhar_linha_central()
        raquete1.desenhar(self.tela)
        raquete2.desenhar(self.tela)
        for bola in bolas:
            bola.desenhar(self.tela)
        self.desenhar_placar(placar)

    def desenhar_menu(self):
        self.limpar()

        titulo = self.fonte_titulo.render("PONG", True, BRANCO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))

        controles = self.fonte_pequena.render(
            "Jogador 1: Setas  |  Jogador 2: IA", True, CINZA
        )
        self.tela.blit(controles, controles.get_rect(center=(LARGURA // 2, ALTURA // 2)))

        if pygame.time.get_ticks() % 2000 < 1000:
            instrucao = self.fonte_pequena.render(
                "Pressione ESPAÇO para jogar", True, BRANCO
            )
            self.tela.blit(instrucao, instrucao.get_rect(center=(LARGURA // 2, ALTURA // 2 + 70)))

    def desenhar_vitoria(self, vencedor: str):
        self.limpar()

        titulo = self.fonte_titulo.render(f"{vencedor} venceu!", True, BRANCO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))

        reiniciar = self.fonte_media.render("ESPAÇO — Jogar novamente", True, CINZA)
        sair = self.fonte_media.render("ESC — Menu principal", True, CINZA)
        self.tela.blit(reiniciar, reiniciar.get_rect(center=(LARGURA // 2, ALTURA // 2 + 30)))
        self.tela.blit(sair, sair.get_rect(center=(LARGURA // 2, ALTURA // 2 + 70)))