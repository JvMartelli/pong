from paddle import Raquete
from ball import Bola


class ControladorIA:

    def atualizar(self, raquete: Raquete, bola: Bola):
        centro_raquete = raquete.y + raquete.altura // 2

        if centro_raquete < bola.y:
            raquete.mover_baixo()
        elif centro_raquete > bola.y:
            raquete.mover_cima()
