from enemigo import *


class ogro(Enemigo):
    def __init_(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo="ogro", puntos_energia=puntos_energia, ataque=ataque)


        def habla(self):
            print("ogro aplastar todo")