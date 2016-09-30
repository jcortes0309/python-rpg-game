"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
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
        print "\t%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "\t%s received %d damage." % (self.name, points)
        if self.health <= 0:
            if self.name == "zombie":
                pass
            else:
                print "\t%s is dead." % self.name

    def print_status(self):
        print "\t%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print "\tHero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        if not self.alive():
            return
        print "\t%s attacks %s" % (self.name, enemy.name)
        if enemy.name == "shadow":
            if random.random() >= .10:
                enemy.receive_damage(self.power * 0)
            else:
                if random.random() <= .2:
                    enemy.receive_damage(self.power * 2)
                else:
                    enemy.receive_damage(self.power)
        else:
            if random.random() <= .2:
                enemy.receive_damage(self.power * 2)
            else:
                enemy.receive_damage(self.power)
        time.sleep(1.5)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "\t%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 8
        self.power = 3
        self.recuperate = 2

    def regenerate(self):
        if random.random() <= .20:
            self.health += self.recuperate
        else:
            pass

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 1
        self.power = 1

    def alive(self):
        if random.random() <= .25:
            print "%s has left." % self.name
            return False
        else:
            return True

class Borg(Character):
    def __init__(self):
        self.name = 'borg'
        self.health = 6
        self.power = 2
        self.recuperate = 4

    def regenerate(self):
        self.health += self.recuperate

    def attack(self, enemy):
        if not self.alive():
            return
        print "\t%s attacks %s" % (self.name, enemy.name)
        if random.random() <= .4:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)


class Thief(Character):
    def __init__(self):
        self.name = 'thief'
        self.health = 12
        self.power = 2




class Battle(object):
    def do_battle(self, hero, enemy):
        print "\n====================="
        print "Hero faces the %s" % enemy.name
        print "=====================\n"
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "\n-----------------------"
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
                print "\tGoodbye."
                exit(0)
            else:
                print "\tInvalid input %r" % input
                continue
            enemy.attack(hero)
            if enemy.name == "medic" or enemy.name == "borg":
                enemy.regenerate()
                print "\tOH NO! THE %s REGENERATED %d HEALTH!" % (enemy.name.upper(), enemy.recuperate)
                time.sleep(2.0)
            else:
                pass
            # if enemy.name == 'thief':
        if hero.alive():
            print "\tYou defeated the %s" % enemy.name
            return True
        else:
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "\t%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "\t%s's power increased to %d." % (hero.name, hero.power)

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "\n====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
# enemies = [Goblin(), Wizard(), Medic(), Shadow(), Zombie(), Borg(), Thief()]
enemies = [Thief()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        if enemy.name == 'borg':
            print "\tYOU HAVE BEEN ASSIMILATED!!"
        else:
            pass
        print "\tYOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "\tYOU WIN!"
