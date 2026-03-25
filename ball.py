import math
import random
import pygame
from settings import LARGURA, ALTURA, BOLA_RAIO, BOLA_VELOCIDADE_INICIAL, BRANCO


class Bola:

    VELOCIDADE = BOLA_VELOCIDADE_INICIAL
    CHANCE_IMPREVISIVEL = 0.25

    def __init__(self, cor=BRANCO, verdadeira=True):
        self.raio = BOLA_RAIO
        self.cor = cor
        self.verdadeira = verdadeira
        self.resetar(direcao=1)

    def resetar(self, direcao: int = 1):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.vel_x = self.VELOCIDADE * direcao
        self.vel_y = random.uniform(-self.VELOCIDADE, self.VELOCIDADE)
        self._rebateu_parede = False

    def _rebote_aleatorio(self, direcao_x: int):
        angulo = random.uniform(-60, 60)
        rad = math.radians(angulo)
        self.vel_x = direcao_x * self.VELOCIDADE * abs(math.cos(rad))
        self.vel_y = self.VELOCIDADE * math.sin(rad)

    def fragmentar(self) -> list:
        fragmentos = []
        for _ in range(3):
            cor = (
                random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255),
            )
            falsa = Bola(cor=cor, verdadeira=False)
            falsa.x = self.x
            falsa.y = self.y
            falsa.vel_x = self.vel_x * random.uniform(0.8, 1.2)
            falsa.vel_y = random.uniform(-self.VELOCIDADE, self.VELOCIDADE)
            fragmentos.append(falsa)
        return fragmentos

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(
            self.x - self.raio,
            self.y - self.raio,
            self.raio * 2,
            self.raio * 2,
        )

    def atualizar(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self._rebateu_parede = False

        if self.y - self.raio <= 0 or self.y + self.raio >= ALTURA:
            self.vel_y = -self.vel_y
            if random.random() < self.CHANCE_IMPREVISIVEL:
                direcao_x = 1 if self.vel_x > 0 else -1
                self._rebote_aleatorio(direcao_x=direcao_x)
                if self.y - self.raio <= 0:
                    self.vel_y = abs(self.vel_y)
                else:
                    self.vel_y = -abs(self.vel_y)
            self._rebateu_parede = True

    def rebateu_parede(self) -> bool:
        return self._rebateu_parede

    def rebater_raquete(self, raquete_rect: pygame.Rect) -> bool:
        if self.rect.colliderect(raquete_rect):
            if raquete_rect.centerx < LARGURA // 2 and self.vel_x < 0:
                self._rebote_aleatorio(direcao_x=1)
                return True
            elif raquete_rect.centerx > LARGURA // 2 and self.vel_x > 0:
                self._rebote_aleatorio(direcao_x=-1)
                return True
        return False

    def saiu_pela_esquerda(self) -> bool:
        return self.x + self.raio < 0

    def saiu_pela_direita(self) -> bool:
        return self.x - self.raio > LARGURA

    def desenhar(self, tela: pygame.Surface):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)