# This is a simple text-based game used to illustrate object-oriented-programming in Python.
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power and %d coins" % (self.name, self.health, self.power, self.coins)

class Ogre(Character):
    def __init__(self):
        self.name = 'ogre'
        self.health = 10
        self.power = 5
        self.coins = 20

        # Double the damage 30% of the time
    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)

        # Make the hero generate double damage points during an attack with a probabilty of 20%
        if random.random() < 0.3:
            enemy.receive_damage(2 * self.power)
            print "double points"
        else:
            enemy.receive_damage(self.power)
            print "single points"

        time.sleep(1.5)

class Victim(Character):
    def __init__(self):
        self.name = 'victim'
        self.health = 10
        self.power =5
        self.coins = 20

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power =5
        self.coins = 20

    # Make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
    def receive_damage(self, points):
        if random.random() < 0.2:
            self.health += 2
            print "got two extra points"
        else:
            self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

## Shadow class
class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power =5
        self.coins = 20
    # Make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
    def receive_damage(self, points):
        if random.random() < 0.1:
            self.health -= points
            print "shadow was hit"
            print "%s received %d damage." % (self.name, points)
        else:
            print "missed"

        if self.health <= 0:
            print "%s is dead." % self.name
# Hero class
class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

        # You will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
        self.armor = 0

        #add evade attribute
        self.evade = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)

        # Make the hero generate double damage points during an attack with a probabilty of 20%
        if random.random() < 0.2:
            enemy.receive_damage(2 * self.power)
            print "double points"
        else:
            enemy.receive_damage(self.power)
            print "single points"

        # Hero encounter victim, gets coins
        if enemy.health <= 0 and type(enemy) == Victim:
            hero.coins += 5
            print "Met victim"
        time.sleep(1.5)

    #Evade
    def receive_damage(self, points):
        if self.evade <= 10:
            p = 2.5 * self.evade + 5
        else:
            p = 30
        print "value of evade is: %d"  % self.evade
        print "value of p is: %d"  % p
        if p / 100.0 > random.random():
            self.health -= points
            print "hero got hit"
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

# Class Zombie
class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power =5
        self.coins = 20

    def alive(self):
        return True

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s should have died, but is still alive." % self.name

# Come up with at least two other characters with their individual characteristics, and implement them.


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 20

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 20

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)


#   Make a SuperTonic item to the store, it will restore the hero back to 10 health points.
class SuperTonic(object):
    cost = 7
    name = 'supertonic'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

#   Add an Armor item to the store. Buying an armor will add 2 armor points to the hero -
#   You will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.

class Armor(object):
    cost = 7
    name = 'armor'
    def apply(self, character):
        print 'before, armor = %d' % character.armor
        character.armor += 2
        print 'after,  armor = %d' % character.armor
        print "%s's armor increased to %d." % (character.name, character.armor)

# Add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
class Evade(object):
    cost = 15
    name = 'evade'
    def apply(self, character):
        print 'before, evade = %d' % character.evade
        character.evade += 2
        print 'after,  evade = %d' % character.evade
        print "%s's evade increased to %d." % (character.name, character.evade)

class Shopping(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                if item.cost <= hero.coins:
                    print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)

            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Shadow(), Zombie(), Ogre(), Victim()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
