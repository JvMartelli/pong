import pygame
from settings import (
    LARGURA, ALTURA, BOLA_RAIO, BOLA_VELOCIDADE_INICIAL, BRANCO
)


class Bola:
    """Representa a bola do jogo. Gerencia sua posição, movimento e colisões."""

    def __init__(self):
        self.raio = BOLA_RAIO
        self.resetar(direcao=1)

    def resetar(self, direcao: int = 1):
        """
        Reposiciona a bola no centro da tela.

        Args:
            direcao: 1 para mover para a direita, -1 para a esquerda.
        """
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.vel_x = BOLA_VELOCIDADE_INICIAL * direcao
        self.vel_y = BOLA_VELOCIDADE_INICIAL

    @property
    def rect(self) -> pygame.Rect:
        """Retorna o rect de colisão centralizado na posição da bola."""
        return pygame.Rect(
            self.x - self.raio,
            self.y - self.raio,
            self.raio * 2,
            self.raio * 2,
        )

    def atualizar(self):
        """Move a bola e rebate nas bordas superior e inferior."""
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y - self.raio <= 0 or self.y + self.raio >= ALTURA:
            self.vel_y = -self.vel_y

    def rebater_raquete(self, raquete_rect: pygame.Rect):
        """
        Inverte a velocidade horizontal ao colidir com uma raquete.
        Só inverte se a bola estiver indo na direção da raquete,
        evitando que fique presa dentro dela.

        Args:
            raquete_rect: Rect da raquete com a qual a bola colidiu.
        """
        if self.rect.colliderect(raquete_rect):
            if raquete_rect.centerx < LARGURA // 2 and self.vel_x < 0:
                self.vel_x = -self.vel_x
            elif raquete_rect.centerx > LARGURA // 2 and self.vel_x > 0:
                self.vel_x = -self.vel_x

    def saiu_pela_esquerda(self) -> bool:
        """Verifica se a bola saiu pelo lado esquerdo da tela."""
        return self.x + self.raio < 0

    def saiu_pela_direita(self) -> bool:
        """Verifica se a bola saiu pelo lado direito da tela."""
        return self.x - self.raio > LARGURA

    def desenhar(self, tela: pygame.Surface):
        """Desenha a bola na tela."""
        pygame.draw.circle(tela, BRANCO, (self.x, self.y), self.raio)
