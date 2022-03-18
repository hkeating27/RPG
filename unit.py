class Unit:

    #TODO: differentiate between current and max hit and mana points
    def __init__(self, name = "", job = "", level = 1, hitPoints = 0, manaPoints = 0, attack = 0, magic = 0, speed = 0, defense = 0, resistance = 0, experience = 0, gold = 0):
        self.name = ""
        self.job = ""
        self.level = 1
        self.hitPoints = 27
        self.manaPoints = 13
        self.attack = 10
        self.magic = 5
        self.speed = 7
        self.defense = 7
        self.resistance = 5
        self.experience = 0
        self.gold = 0

    #Name
    def set_name(self, str):
        self.name = str

    def get_name(self):
        return self.name

    #Job
    #TODO: Add extra jobs
    def set_job(self, str):
        self.job = str

    def get_job(self):
        return self.job

    #Level
    #TODO: Make level ups job-based and adding new abilities
    #This doesn't set a level so much as increment, but set_level is used for consistency
    def set_level(self):
        self.level = self.level + 1
        print(str(self.name) + " advanced to level " + str(self.level))
        self.hitPoints += 7
        print("Hit Points increased to " + str(self.hitPoints))
        self.manaPoints += 5
        print("Mana Points increased to " + str(self.manaPoints))
        self.attack += 5
        print("Attack increased to " + str(self.attack))
        self.magic += 5
        print("Magic increased to " + str(self.magic))
        self.speed += 5
        print("Speed increased to " + str(self.speed))
        self.defense += 5
        print("Defense increased to " + str(self.defense))
        self.resistance += 5
        print("Resistance increased to " + str(self.resistance))


    def get_level(self):
        return self.level

    #Hit Points
    def set_hitpoints(self, num):
        self.hitPoints = num

    def get_hitpoints(self):
        return self.hitPoints;

    #Mana Points
    def set_manapoints(self, num):
        self.manaPoints = num

    def get_manapoints(self):
        return self.manaPoints;

    #Attack
    def set_attack(self, num):
        self.attack = num

    def get_attack(self):
        return self.attack;

    #Magic
    def set_magic(self, num):
        self.magic = num

    def get_magic(self):
        return self.magic

    #Speed
    def set_speed(self, num):
        self.speed = num

    def get_speed(self):
        return self.speed

    #Defense
    def set_defense(self, num):
        self.defense = num

    def get_defense(self):
        return self.defense

    #Resistance
    def set_resistance(self, num):
        self.resistance = num

    def get_resistance(self):
        return self.resistance

    #Experience
    def set_experience(self, num):
        self.experience = num

    def get_experience(self):
        return self.experience

    #Gold
    def set_gold(self, num):
        self.gold = num

    def get_gold(self):
        return self.gold