#classe chien:
class Chien:
  def __init__(self,nom,age,race):
    self.nom=nom
    self.age=age 
    self.race=race
  def aboyer(self):
    print("wouf")
     
  

chien1=Chien("alex",8,"husky")
print(chien1.nom,chien1.age,chien1.race)
chien1.aboyer()  

   
   