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
        print "The %s has %d health and %d power." % (type(self).__name__, self.health, self.power)

    def attack(self, enemy):
        enemy.health -= self.power
        if type(self).__name__ == "Hero":
            print "You do %d damage to the %s." % (self.power, type(enemy).__name__)
            if enemy.health <= 0:
                print "The %s is dead." % type(enemy).__name__
        else:
            print "The %s does %d damage to you." % (type(self).__name__, self.power)
            if enemy.health <= 0:
                print "You are dead."


class Hero(Character):
    def __init__(self):
        # self.name = "hero"
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        # self.name = "goblin"
        self.health = 6
        self.power = 2


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
