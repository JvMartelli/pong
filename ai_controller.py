from paddle import Raquete
from ball import Bola


class ControladorIA:

    ZONA_MORTA = 6

    def atualizar(self, raquete: Raquete, bola: Bola):
        centro_raquete = raquete.y + raquete.altura // 2

        if centro_raquete < bola.y - self.ZONA_MORTA:
            raquete.mover_baixo()
        elif centro_raquete > bola.y + self.ZONA_MORTA:
            raquete.mover_cima()