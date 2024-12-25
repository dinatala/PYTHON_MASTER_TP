from abc import ABC, abstractmethod
import math

# Classe abstraite Forme
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

    def afficher_surface(self):
        print(f"La surface de la forme est: {self.calculer_surface():.2f}")


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * (self.rayon ** 2)


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_surface(self):
        return self.longueur * self.largeur



cercle = Cercle(5)
rectangle = Rectangle(4, 6)

 #calcule et affichage des surfaces:  
print("les surfaces des formes:")
cercle.afficher_surface()
rectangle.afficher_surface()


