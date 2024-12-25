class Produit:
    def __init__(self, n, p):
        self.__nom = n
        self.__prix = p

    @property
    def prix(self):
        return self.__prix

    @property
    def nom(self):
        return self.__nom
    
    def remise_prix(self, remise):
        if self.__prix < remise:
            print("operation impossible")
        else:
            self.__prix -= remise
            print("operation realise")

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} = {self.calculer_total():.2f}"

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = 0
        for commande in self.commandes:
            total += commande.calculer_total()  # appel de la fonction calculer_total de la classe Commande
        return total

    def afficher_total(self):
        print(f"Total du panier : {self.calculer_total():.2f}")


# Création de produits
produit1 = Produit("Pomme", 0.5)
produit2 = Produit("Banane", 0.3)

# Création de commandes
commande1 = Commande(produit1, 4)  
commande2 = Commande(produit2, 10)  

# Création du panier
panier = Panier()

panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

# Calcul du total
panier.afficher_total()

#calcule du prix en exercise 4:
op=Produit("jake",5000)
print(op.prix)
op.remise_prix(7000)
