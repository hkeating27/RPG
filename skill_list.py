from unit import Unit

class Skill_List:

    def __init__(self, name = "", manacost = 0, potency = 0):
        self.name = ""
        self.type = ""
        self.potency = 0
        self.manacost = 0

    #TODO: compatibility with a data structure full of skills
    def print_skills(self, job):
        if (job == "Hero"):
            print("Double Strike")

    #Hero class can only learn one skill right now
    def double_strike(self, hero, attack, enemy):
        enemy.set_hitpoints(enemy.get_hitpoints()-(2*attack))
        hero.set_manapoints(hero.get_manapoints()-3)