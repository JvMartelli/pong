import sys
import pygame
from settings import LARGURA, ALTURA, FPS, TITULO, MARGEM_RAQUETE, RAQUETE_LARGURA
from ball import Bola
from paddle import Raquete
from scoreboard import Placar
from ai_controller import ControladorIA
from renderer import Renderer
from sound_manager import GerenciadorSom

INTERVALO_FRAGMENTACAO = 5000  # milissegundos


class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.tela)
        self.ia = ControladorIA()
        self.som = GerenciadorSom()

    def _criar_entidades(self):
        self.bolas = [Bola()]
        self.raquete1 = Raquete(x=MARGEM_RAQUETE)
        self.raquete2 = Raquete(x=LARGURA - MARGEM_RAQUETE - RAQUETE_LARGURA)
        self.placar = Placar()
        self.ultimo_fragmento = pygame.time.get_ticks()

    def _bola_verdadeira(self) -> Bola | None:
        for bola in self.bolas:
            if bola.verdadeira:
                return bola
        return None

    def _processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _processar_input_jogador1(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.raquete1.mover_cima()
        if teclas[pygame.K_DOWN]:
            self.raquete1.mover_baixo()

    def _processar_fragmentacao(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_fragmento >= INTERVALO_FRAGMENTACAO:
            bola_v = self._bola_verdadeira()
            if bola_v:
                self.bolas += bola_v.fragmentar()
                self.ultimo_fragmento = agora

    def _resetar_bolas(self, direcao: int):
        bola = Bola()
        bola.resetar(direcao=direcao)
        self.bolas = [bola]
        self.ultimo_fragmento = pygame.time.get_ticks()

    def cena_menu(self):
        while True:
            self._processar_eventos()
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                return
            self.renderer.desenhar_menu()
            pygame.display.flip()
            self.clock.tick(FPS)

    def cena_jogo(self) -> str:
        self._criar_entidades()
        self.som.iniciar_trilha()

        while True:
            self._processar_eventos()
            self._processar_input_jogador1()

            bola_v = self._bola_verdadeira()
            if bola_v:
                self.ia.atualizar(self.raquete2, bola_v)

            self._processar_fragmentacao()

            for bola in self.bolas:
                bola.atualizar()

                if bola.rebater_raquete(self.raquete1.rect):
                    self.som.tocar_raquete()
                if bola.rebater_raquete(self.raquete2.rect):
                    self.som.tocar_raquete()

            bola_v = self._bola_verdadeira()
            if bola_v:
                if bola_v.saiu_pela_esquerda():
                    self.placar.ponto_jogador2()
                    self.som.tocar_ponto()
                    self._resetar_bolas(direcao=1)

                elif bola_v.saiu_pela_direita():
                    self.placar.ponto_jogador1()
                    self.som.tocar_ponto()
                    self._resetar_bolas(direcao=-1)

            vencedor = self.placar.vencedor()
            if vencedor:
                self.som.parar_trilha()
                return vencedor

            self.renderer.desenhar_jogo(
                self.bolas, self.raquete1, self.raquete2, self.placar
            )
            pygame.display.flip()
            self.clock.tick(FPS)

    def cena_vitoria(self, vencedor: str) -> bool:
        while True:
            self._processar_eventos()
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                return True
            if teclas[pygame.K_ESCAPE]:
                return False
            self.renderer.desenhar_vitoria(vencedor)
            pygame.display.flip()
            self.clock.tick(FPS)

    def executar(self):
        while True:
            self.cena_menu()
            while True:
                vencedor = self.cena_jogo()
                jogar_novamente = self.cena_vitoria(vencedor)
                if not jogar_novamente:
                    break