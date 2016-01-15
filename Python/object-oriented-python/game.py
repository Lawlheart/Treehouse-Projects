from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
import os
import sys


class Game:

    def __init__(self):
        self.setup()
        self.updateUI()
        print("You encounter a {}".format(self.monster.__class__.__name__))
        while self.player.hp and (self.monster or self.monsters):
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hp:
            print("VICTORY!!")
        elif self.monster.hp or self.monsters:
            print("GAME OVER")
        else:
            print("With your last breath, you vanquish the monster!")

    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def updateUI(self):
        os.system('clear')
        print(self.player)
        print("Level {}".format(self.player.lv))
        print("Weapon: {}".format(self.player.weapon.capitalize()))
        print("------------------------------------------")

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("The {} attacks you with all its might!".format(
                self.monster.__class__.__name__))
            player_choice = input("do you try to dodge? (y/n) ").lower()
            print()
            if player_choice == 'y':
                if self.player.dodge():
                    print("You successfuly dodge the monster's "
                          "fearsome attack!")
                else:
                    self.player.hp -= self.monster.dmg
                    print("Your dodge fails! The monster hits you for"
                          " {} damage!".format(self.monster.dmg))
            else:
                self.player.hp -= self.monster.dmg
                print("You stand there as the monster wails on you. "
                      "Curious choice.")
        else:
            print("{} is loafing around! Now's your chance to strike!".format(
                self.monster.__class__.__name__))

    def player_turn(self):
        player_choice = input("Do you [A]ttack, [R]est, or [Q]uit? ").lower()
        self.updateUI()
        if player_choice == 'a':
            print("You attack with your {} and...".format(self.player.weapon))
            if self.player.attack():
                if self.monster.dodge():
                    print("The {} dodged your attack!".format(
                        self.monster.__class__.__name__))
                else:
                    print("You hit the {} for {} damage!!".format(
                        self.monster.__class__.__name__, self.player.lv))
                    self.monster.hp -= self.player.lv
            else:
                print("Miss. Terribly.".format(self.player.weapon))
        elif player_choice == 'r':
            print("You take a moment to heal. Regain 1 HP!")
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        print()
        if self.monster.hp <= 0:
            self.player.exp += self.monster.exp
            print("You defeated the {}! You gain {} XP".format(
                self.monster.__class__.__name__, self.monster.exp))
            if self.player.leveled_up():
                self.player.lv += 1
                self.player.exp -= 5
                self.player.hp += 5
                self.player.max_hp += 5
                print("Congratulations! You Leveled Up. "
                      "You are now level {}".format(self.player.lv))
            self.monster = self.get_next_monster()
            if self.monster:
                print("You encounter a {}".format(
                      self.monster.__class__.__name__))
                print()
        elif self.monster.hp <= self.monster.bloodied:
            print("The monster is nearing defeat!")
            print()


Game()
