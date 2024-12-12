class Voiture:
    def afficher_info(self,marque,modele,annee):
        self.marque=marque
        self.annee=annee
        self.modele=modele
        return'{}{}{}'.format(self.marque ,self.modele ,self.annee)

voiture1=Voiture()
print(voiture1.afficher_info("porche","LUX",2024))

