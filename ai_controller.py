# =============================================================================
# ai_controller.py
# Controlador de IA para a raquete do jogador 2.
# Princípio SRP: isola a lógica de decisão da IA das demais partes do jogo.
# Princípio OCP: se quiser criar uma IA diferente (ex: difícil/fácil),
# basta criar outra classe sem modificar esta.
# =============================================================================

from paddle import Raquete
from ball import Bola


class ControladorIA:
    """
    Controla uma raquete automaticamente, seguindo a posição da bola.
    A IA move a raquete em direção ao centro da bola.
    """

    def atualizar(self, raquete: Raquete, bola: Bola):
        """
        Move a raquete da IA com base na posição atual da bola.

        Args:
            raquete: A raquete que a IA controla.
            bola: A bola sendo acompanhada pela IA.
        """
        centro_raquete = raquete.y + raquete.altura // 2

        if centro_raquete < bola.y:
            raquete.mover_baixo()
        elif centro_raquete > bola.y:
            raquete.mover_cima()
