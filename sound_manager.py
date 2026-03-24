import pygame


class GerenciadorSom:

    def __init__(self):
        pygame.mixer.init()
        self._trilha_tocando = False

        self._som_raquete = self._carregar_efeito("sounds/hit_paddle.mp3")
    #   self._som_parede  = self._carregar_efeito("sounds/hit_wall.mp3")
        self._som_ponto   = self._carregar_efeito("sounds/score.mp3")
        self._trilha      = self._carregar_musica("sounds/music.mp3")

    def _carregar_efeito(self, caminho: str):
        try:
            som = pygame.mixer.Sound(caminho)
            som.set_volume(0.5)
            return som
        except FileNotFoundError:
            print(f"[Som] Arquivo não encontrado: {caminho}")
            return None

    def _carregar_musica(self, caminho: str):
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.set_volume(0.05)
            return caminho
        except (FileNotFoundError, pygame.error):
            print(f"[Som] Trilha não encontrada: {caminho}")
            return None

    def tocar_raquete(self):
        if self._som_raquete:
            self._som_raquete.play()

    #def tocar_parede(self):
     #   if self._som_parede:
      #      self._som_parede.play()

    def tocar_ponto(self):
        if self._som_ponto:
            self._som_ponto.play()

    def iniciar_trilha(self):
        if self._trilha and not self._trilha_tocando:   
            pygame.mixer.music.play(loops=-1)
            self._trilha_tocando = True

    def parar_trilha(self):
        if self._trilha_tocando:
            pygame.mixer.music.stop()
            self._trilha_tocando = False