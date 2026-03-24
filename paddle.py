import pygame
from settings import (
    ALTURA, RAQUETE_LARGURA, RAQUETE_ALTURA, RAQUETE_VELOCIDADE, BRANCO
)


class Raquete:
    """
    Representa uma raquete do jogo.
    Pode ser controlada pelo jogador (via teclado) ou pela IA.
    """

    def __init__(self, x: int):
        """
        Inicializa a raquete em uma posição horizontal fixa.

        Args:
            x: Posição horizontal da raquete na tela.
        """
        self.x = x
        self.y = ALTURA // 2 - RAQUETE_ALTURA // 2
        self.largura = RAQUETE_LARGURA
        self.altura = RAQUETE_ALTURA
        self.velocidade = RAQUETE_VELOCIDADE

    @property
    def rect(self) -> pygame.Rect:
        """Retorna o rect de colisão da raquete."""
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover_cima(self):
        """Move a raquete para cima, respeitando o limite da tela."""
        self.y = max(0, self.y - self.velocidade)

    def mover_baixo(self):
        """Move a raquete para baixo, respeitando o limite da tela."""
        self.y = min(ALTURA - self.altura, self.y + self.velocidade)

    def desenhar(self, tela: pygame.Surface):
        """Desenha a raquete na tela."""
        pygame.draw.rect(tela, BRANCO, self.rect)
