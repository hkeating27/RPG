from unit import Unit

class Spell_List:

    def __init__(self, name = "", type = "", manacost = 0, potency = 0):
        self.name = ""
        self.type = ""
        self.potency = 0
        self.manacost = 0

    #TODO: Add different spells per class
    #TODO: Make this function print spells based on data structure
    def print_spells(self, job):
        if (job == "Hero"):
            print("Heal, Ruin")

    #Heal spell
    def heal(self, magic, hero):
        hero.set_hitpoints(hero.get_hitpoints() + magic)
        hero.set_manapoints(hero.get_manapoints()-5)

    #Non-elemental damage spell
    def ruin(self, magic, enemy):
        enemy.set_hitpoints(enemy.get_hitpoints()-magic)
        hero.set_manapoints(hero.get_manapoints()-5)