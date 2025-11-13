import random

class Character():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def take_damage(self, amount):
        self.health -= amount
    

class Assassin(Character):
    def __init__(self, health, damage):
        super().__init__(health, damage)
        self.toughness = 0.90

    def take_damage(self, amount):
        modified_amount_armor = amount * self.toughness
        super().take_damage(modified_amount_armor)
        

class Vagabond(Character):
    def __init__(self, health, damage):
        super().__init__(health, damage)
        self.critical_strike = 1.50

    def take_damage(self, amount):
        modified_amount_crit = amount * self.critical_strike
        super().take_damage(modified_amount_crit)
        
assassin = Assassin(100, 20)
vagabond = Vagabond(100, 20)
count = 1
while vagabond.health > 0 and assassin.health > 0:
    print("Assassin's start HP:")
    print(assassin.health, end=" ")
    print("hp")
    print("-"*3)
    assassin.take_damage(random.randint(30, 40))


    print("Vagabond's start HP:")
    print(vagabond.health, end=" ")
    print("hp")
    print("-"*3)
    vagabond.take_damage(random.randint(10, 30))

    print(f"|ROUND {count}|")


    print("Assassin's HP:", end=" ")
    print(assassin.health)
    print("Vagabond's HP:", end=" ")
    print(vagabond.health)
    count += 1
    if vagabond.health <= 0 and assassin.health <= 0:
        print("They are both dead")
    elif vagabond.health <= 0:
        print("Vagabond is dead", end=" ")
        print("Assassin is Champion")
    elif assassin.health <= 0:
        print("Assassin is dead", end=" ")
        print("Vagabond is Champion")
    
