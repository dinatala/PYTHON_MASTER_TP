class Animal():
    def faire_du_bruit(self):
        print(f"cette animal possede le son:")
#different implementation du meme fonction du class parent
class Chat(Animal):
   def faire_du_bruit(self):
    return f"{super().faire_du_bruit()} ,maaow"
   
   
class Chien(Animal):
    def faire_du_bruit(self):
     return f"{super().faire_du_bruit()} ,woof"                      
cat=Chat()
dog=Chien()
print(cat.faire_du_bruit())
print(dog.faire_du_bruit())

