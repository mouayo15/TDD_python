from RPG_CI.Personnage import Personnage

def test_hp_initiaux():
    personnage = Personnage()
    assert personnage.get_point_de_vie() == 100

def test_initialement_vivant():
    personnage = Personnage()
    assert not personnage.is_est_mort()

def test_mort():
    personnage = Personnage()
    personnage.tuer()
    assert personnage.get_point_de_vie() == 0
    assert personnage.is_est_mort()

def test_attaquer_autre_personnage():
    attaquant = Personnage()
    adversaire = Personnage()
    point_de_vie_avant_attaque = adversaire.get_point_de_vie()
    degat = 10  
    attaquant.attaquer(adversaire, degat)
    assert adversaire.get_point_de_vie() == point_de_vie_avant_attaque - degat
