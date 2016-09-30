"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character(object):
    # def __repr__(self):
    #     return self

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print "The %s has %d health and %d power." % (self.__class__.__name__, self.health, self.power)

class Hero(Character):
    def __init__(self):
        # self.name = "hero"
        self.health = 10
        self.power = 5

    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the goblin." % self.power
        if goblin.health <= 0:
            print "The goblin is dead."

class Goblin(Character):
    def __init__(self):
        # self.name = "goblin"
        self.health = 6
        self.power = 2

    def attack(self, enemy):
        enemy.health -= self.power
        print "The goblin does %d damage to you." % self.power
        if hero.health <= 0:
            print "You are dead."


hero = Hero()
goblin = Goblin()

while goblin.alive() > 0 and hero.alive() > 0:
    hero.print_status()
    goblin.print_status()
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        hero.attack(goblin)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if goblin.health > 0:
        # Goblin attacks hero
        goblin.attack(hero)
