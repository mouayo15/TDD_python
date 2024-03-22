class Personnage:
    def __init__(self):
        self.point_de_vie = 100
        self.est_mort = False
        self.puissance_attaque = 0

    def get_point_de_vie(self):
        return self.point_de_vie

    def set_point_de_vie(self, point_de_vie):
        self.point_de_vie = point_de_vie

    def is_est_mort(self):
        return self.est_mort

    def set_est_mort(self, est_mort):
        self.est_mort = est_mort

    def tuer(self):
        self.point_de_vie = 0
        self.est_mort = True

    def attaquer(self, cible, degats):
        if not cible.is_est_mort():
            cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.point_de_vie -= degats
        if self.point_de_vie < 0:
            self.point_de_vie = 0

    def get_puissance_attaque(self):
        return self.puissance_attaque
