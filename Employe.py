class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def __str__(self):
        return f"{self.prenom} {self.nom}, Salaire: {self.salaire}"

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.liste_employes = []

    def ajouter_employe(self, employe):
        self.liste_employes.append(employe)
           

    def afficher_employes(self):
        for emp in self.liste_employes:
            print(f" -{emp}")



employe1 = Employe("JAKE", "JAKIE", 2500)
employe2 = Employe("Marie", "Sophie", 2700)
employe3=Employe("SARA","DORA",3000)

# Création d'un manager
manager = Manager("Dupont", "Marc", 4500)

#ajouter un employé
manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)

# Ajout d'un autre employé
manager.ajouter_employe(employe3)

# Affichage des employés 
manager.afficher_employes()

