from unit import Unit

class Item_List:

    def __init__(self, name = "", numHerbs = 2, numVulneraries = 1):
            self.name = ""
            self.numHerbs = 2
            self.numVulneraries = 1

    #TODO: Add different classes for potions, key items, etc.
    #TODO: Make item class
    #TODO: Ensure that healing does not go above max health
    #TODO: Add items

    #Uses the most basic healing item
    def use_herb(self, hero):
        if (self.numHerbs > 0):
            hero.set_hitpoints(hero.get_hitpoints() + 10)
            self.numHerbs -= 1
        else:
            print("No more herbs")

    #Mid tier healing item
    def use_vulnerary(self, hero):
        if (self.numVulneraries > 0):
            hero.set_hitpoints(hero.get_hitpoints() + 20)
            self.numVulneraries -= 1
        else:
            print("No more vulneraries")


        


