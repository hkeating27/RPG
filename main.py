from unit import Unit
from spell_list import Spell_List
from skill_list import Skill_List
from item_list import Item_List
from combat import Combat
from exploration import Exploration

hero = Unit(None, None, None, None, None, None, None, None, None)
enemy = Unit(None, None, None, None, None, None, None, None, None)
spells = Spell_List(None, None, None)
skills = Skill_List(None, None, None)
items = Item_List(None, None, None)
encounter = Combat(None, None, None)
exploration = Exploration(None, None, None)

#This program is full of TODOs in case I want to make it a full RPG
def main():
    #Peak of character customization
    val = input("Enter character name:\n")
    hero.set_name(val)
    #TODO: add different jobs
    hero.set_job("Hero")

    #Set Enemy stats
    #TODO: Multiple enemy types
    enemy.set_hitpoints(25), enemy.set_attack(2), enemy.set_experience(15), enemy.set_gold(4)
    encounter.battle(hero, enemy)
    #TODO: write movement loop
    val = input("Move direction: (n, s, e, or w)\n")
    exploration.moveOverworld(val)

    

#Actually starts the game
if __name__ == "__main__":
    main()