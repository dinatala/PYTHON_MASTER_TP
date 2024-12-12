class Livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre=titre
        self.auteur=auteur
        self.annee_publication=annee_publication
    def __str__(self):
       return f"titre:{self.titre} de {self.auteur} publié en:{self.annee_publication}"

class Bibliotheque:
 def __init__(self):
    self.list_livres=list() 

 def ajouter_livres(self,livre) :
    self.list_livres.append(livre)

 def afficher_livres(self):
     for i in self.list_livres:
         print(i)   

livre1=Livre('petit prince','ALbert',2013)    
biblio=Bibliotheque()
biblio.ajouter_livres(livre1)
biblio.afficher_livres()
