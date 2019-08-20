import random

class Senshi:
    name = ""
    category = ""
    attack = 0
    defense = 0
    speed = 0
    health = 0
    maxHealth = 0
    expertise = 0
    level = 0
    attackHistoric = []
    defenseHistoric = []

    def __init__(self, name, category, attack, defense, speed, health, expertise, level):
        self.name = name
        self.category = category
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.maxHealth = health
        self.expertise = expertise
        self.level = level


    def attacking(self):
        i = 0
        thisAttack = 0
        pool = self.attack
        if (self.category == "ninja"):
             pool += self.expertise
        while (i<=pool):
            thisAttack += random.randint(1, 6)
            i += 1
        self.attackHistoric.append(thisAttack)
        return thisAttack

    def defending(self):
        i = 0
        thisDefense = 0
        pool = self.defense
        if (self.category == "samurai"):
            pool += self.expertise
        while (i<=pool):
            thisDefense += random.randint(1, 6)
            i += 1
        self.defenseHistoric.append(thisDefense)
        return thisDefense

    def healing(self):
        if (self.category == "sorcerer"):
            heal = self.level + self.expertise
            if ((heal + self.health) >= self.maxHealth):
                self.health = self.maxHealth
            else:
                self.health += heal


    def hurted(self, damage, defended, attacker):
        hurt = damage - defended
        if (hurt > 0):
            self.health -= hurt
        else:
            self.health -= attacker.level
            if (attacker.category == "sorcerer"):
                self.health -= damage / 2


    def levelingUp(self):
        self.level += 1
        if (self.category == "ninja"):
            self.maxHealth += 10
            self.health += 10
            self.attack += 2
            if (self.level % 4 == 0):
                self.expertise += 1
                self.defense += 1
                self.speed += 1
        elif (self.category == "samurai"):
            self.maxHealth += 30
            self.health += 30
            self.defense += 2
            if (self.level % 4 == 0):
                self.expertise += 1
                self.attack += 1
                self.speed += 1
        elif (self.category == "sorcerer"):
            self.maxHealth += 5
            self.health += 5
            self.attack += 1
            self.defense += 1
            if (self.level % 4 == 0):
                self.expertise += 1
                if (random.randint(1, 2) % 2 == 0):
                    self.defense += 1
                else:
                    self.attack += 1
                self.speed += 1
