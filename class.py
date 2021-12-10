class animal:
    thing = 'animal'
    species = None
    weight = None
    diet = None

    def __init__(self, species, weight, diet):
        self.species = species
        self.weight = weight
        self.diet = diet

    # Get name variable
    def get_species(self):
        return self.species

    # Set name variable
    def set_species(self, species):
        self.species = species

    # Get weight variable
    def get_weight(self):
        return self.weight

    # Set weight variable
    def set_weight(self, weight):
        self.weight = weight

    # Get diet variable
    def get_diet(self):
        return self.diet

    # Set diet variable
    def set_diet(self, diet):
        self.diet = diet

    #check to see if animal is large
    def isscary(self):
        if self.weight >= 300:
            print("Wow!", self.species, "is huge and powerful!")
        else:
            print( self.species, "is a pretty average animal")

    #See which animal will win a fight
    def fight(self, other):
        if self.weight > other.weight:
            print("the", self.thing, self.species, "managed to beat", other.species)
        elif self.weight == other.weight:
            if self.diet == "meat" and other.diet == "grass":
                print("the", self.thing, self.species, "managed to beat", other.species)
            elif self.diet == "grass" and other.diet == "meat":
                print("the", other.thing, other.species, "managed to beat", self.species)
            else:
                print("The fight is very even. No victors")
        else:
            print("the", other.thing, other.species, "managed to beat", self.species)

        





if __name__ == "__main__":

    # Create three objects 
    animal1 = animal('tiger', 400, "meat")
    animal2 = animal('elephant', 2000, "grass")
    animal3 = animal('rat', 1, "grass")

    # Check if animals are big
    animal1.isscary()
    animal2.isscary()
    animal3.isscary()

    # Make animals fight each other
    animal1.fight(animal2)
    animal1.fight(animal3)
    animal3.fight(animal2)

    #Change animal 3 weight
    animal3.set_weight(5000)

    animal3.fight(animal1)
    animal3.fight(animal2)
    

