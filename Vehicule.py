from abc import ABC, abstractmethod

# Classe abstraite Vehicule
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass


class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture est plus vite")


class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette est moins vite")


voiture = Voiture()
voiture.deplacer()  

bicyclette = Bicyclette()
bicyclette.deplacer() 
