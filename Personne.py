class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom= nom
        self.__prenom = prenom
        self.__age = age
        
        
    @property
    def nom(self):
        return self.__nom

    def setNom(self,n):
        self.__nom=n
   
    def getAge(self):
        return self.__age
    def setAge(self,a):
        self.__age=a
    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def Prenom(self,p):
        self.__prenom=p
    

p=Personne("sara","azil",21)
print(f"le nom:{p.nom},le prenom:{p.prenom},age:{p.getAge()}")
