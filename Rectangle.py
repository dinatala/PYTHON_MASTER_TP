class Rectangle:
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    
    def calculer_surface(self):
        return self.hauteur * self.largeur
    def calculer_perimetre(self):
        return 2 *(self.hauteur + self.largeur)
    
R1= Rectangle(12,7)
print( f"la surface de rectangle est: {R1.calculer_surface()}")
print( f"le perimetre de rectangle est: {R1.calculer_perimetre()}")