class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.age=age
        self.prenom=prenom
        self.listes_amis=list()

    def __str__(self):
        return f"la listes des amis:{self.listes_amis}"
    def se_presenter(self):
        return f"nom:{self.nom} ,prenom:{self.prenom},age:{self.age}"
    def ajouter_ami(self,ami):
        self.listes_amis.append(ami)

    def afficher_amis(self):
     for i in self.listes_amis:
         print(i) 
         
class Etudiant(Personne):
    def _init_(self,nom,prenom,age,matricule):
        super()._init(nom,prenom,age)
        self.matricule=matricule
        
    def etudier():
        pass

person=Etudiant('ali','balal',20)
print(person.se_presenter())
ami=Personne("conan","gambol",18)
ami.ajouter_ami("sara")
print(ami.afficher_amis())