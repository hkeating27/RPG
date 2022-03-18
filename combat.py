from unit import Unit
from spell_list import Spell_List
from skill_list import Skill_List
from item_list import Item_List

spells = Spell_List(None, None, None)
skills = Skill_List(None, None, None)
items = Item_List(None, None, None)

class Combat:
    def __init__(self, turn=0, exp=0, gold=0):
        self.turn = 0 #Turn does nothing. Will potentially be used to make speed relevent
        self.exp = 0
        self.gold = 0

    def battle(self, hero, enemy):
        print("A wild enemy appeared!")
        #Prints the starter HUD

        while (hero.get_hitpoints() > 0 and enemy.get_hitpoints() > 0):
            #Prints the (text) GUI
            print("\n" + str(hero.get_name()) + "  HP: " + str(hero.get_hitpoints()) + " MP: " + str(hero.get_manapoints()))
            val = input("Enter your action:\n1. Attack\n2. Skill\n3. Magic\n4. Item\n5. Wait\n")
            #Attack
            if (val == "1"):
                self.attack(hero, enemy)

            #Skill
            if (val == "2"):
                self.use_skill(hero, enemy)

            #Magic
            if (val == "3"):
                self.cast_magic(hero, enemy)

            #Item
            if (val == "4"):
                self.use_item(hero, enemy)
                
            #Checks victory condition
            #If the enemy has 0/negative health, the battle is won
            #TODO: Multiple enemies
            if (enemy.get_hitpoints() <= 0):
                #Prints victory screen and experience/gold gained
                print("\nVictory!")
                print("Experience gained: " + str(enemy.get_experience() ));
                print("Gold gained: " + str(enemy.get_gold()) );
                #Increases gold and experience. Wouldn't want false advertising
                hero.set_experience((hero.get_experience() + enemy.get_experience()))
                #If the hero has enough experience they level up
                if (hero.get_experience() > hero.get_level() * 10):
                    print("\n---------")
                    hero.set_level()
                #Increments gold
                hero.set_gold( hero.get_gold() + enemy.get_gold() )
                break #Ends the game
    
            #If the enemy is still alive, they attack
            #TODO: Allow enemies to do something more than attack
            if (enemy.get_hitpoints() > 0):
                #Prints the damage and decreases hero health
                #TODO: Make defense reduce damage
                print("Enemy attacked for " + str(enemy.get_attack()) + " damage!")
                hero.set_hitpoints(hero.get_hitpoints()-enemy.get_attack())
                #Loss condition (Hero has 0/negative health)
                if (hero.get_hitpoints() <= 0):
                    print("Game Over.")
                #print("\n" + str(hero.get_name()) + "  HP: " + str(hero.get_hitpoints()) + "  MP: " + str(hero.get_manapoints()))
        
            

    #Hero attacks physically
    def attack(self, hero, enemy):
        enemy.set_hitpoints(enemy.get_hitpoints() - hero.get_attack())
        print("\n" + str(hero.get_name()) + " attacked for " + str(hero.get_attack()) + " damage!")

    #Hero casts magic
    def cast_magic(self, hero, enemy):
        subval = input("Which spell do you cast?:\n1. Heal\n2. Ruin\n")
        #Heal
        if (subval == "1"):
            spells.heal(hero.get_magic(), hero)
            print("\n" + str(hero.get_name()) + " cast Heal and restored " + str(hero.get_magic()) + " health!")
        #Ruin
        if (subval == "2"):
            enemy.set_hitpoints(enemy.get_hitpoints() - hero.get_magic())
            print("\n" + str(hero.get_name()) + " cast Ruin for " + str(hero.get_magic()) + " damage!")

    #Hero uses skill
    def use_skill(self, hero, enemy):
        subval = input("Which skill do you use?:\n1. Double Strike\n")
        #Double Strike
        if (subval == "1"):
            skills.double_strike(hero, hero.get_attack(), enemy)
            print("\n" + str(hero.get_name()) + " struck twice and did " + str(hero.get_attack()*2) + " damage!")
 
    #Hero uses item
    def use_item(self, hero, enemy):
        subval = input("Which item do you use?:\n1. Herb (10 HP)\n2. Vulnerary (20 HP)\n")
        #Use Herb
        if (subval == "1"):
            items.use_herb(hero)
            print("\n" + str(hero.get_name()) + " used a Herb and healed 10 health!")
        #Use Vulnerary
        if (subval == "2"):
            items.use_vulnerary(hero)
            print("\n" + str(hero.get_name()) + " used a Vulnerary and healed 20 health!")

    #What the enemy does
    #TODO: Make this AI actually work
    def enemy_turn(self, hero, enemy):
        print("Enemy attacked for " + str(enemy.get_attack()) + " damage!\n")
        hero.set_hitpoints(hero.get_hitpoints()-enemy.get_attack())
        print(str(hero.get_name()) + " HP: " + str(hero.get_hitpoints()) + "/27")
            