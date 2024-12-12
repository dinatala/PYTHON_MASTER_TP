class Compte_bancaire:
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde

    def deposer(self,montant):
      self.solde+=montant 
      return self.solde
    def retirer(self,montant):
       if montant>self.solde:
          print('solde insufficent')
       else:
         self.solde-=montant 
         return self.solde 
    def afficher_solde(self):
       print(self.solde)

bank=Compte_bancaire('MBARKA',100)
bank.deposer(10)
bank.retirer(100)
bank.afficher_solde()



      