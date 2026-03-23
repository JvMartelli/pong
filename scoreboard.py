# =============================================================================
# scoreboard.py
# Responsável por armazenar e expor os pontos dos jogadores.
# Princípio SRP: só cuida do estado de pontuação, não de como ela é desenhada.
# =============================================================================

from settings import PONTOS_PARA_VENCER


class Placar:
    """Armazena e gerencia a pontuação dos dois jogadores."""

    def __init__(self):
        self.pontos_j1 = 0
        self.pontos_j2 = 0

    def ponto_jogador1(self):
        """Adiciona um ponto ao jogador 1."""
        self.pontos_j1 += 1

    def ponto_jogador2(self):
        """Adiciona um ponto ao jogador 2."""
        self.pontos_j2 += 1

    def vencedor(self) -> str | None:
        """
        Verifica se algum jogador atingiu a pontuação necessária para vencer.

        Returns:
            Nome do vencedor ('Jogador 1' ou 'Jogador 2') ou None se o
            jogo ainda não terminou.
        """
        if self.pontos_j1 >= PONTOS_PARA_VENCER:
            return "Jogador 1"
        if self.pontos_j2 >= PONTOS_PARA_VENCER:
            return "Jogador 2"
        return None

    def resetar(self):
        """Zera a pontuação dos dois jogadores."""
        self.pontos_j1 = 0
        self.pontos_j2 = 0
