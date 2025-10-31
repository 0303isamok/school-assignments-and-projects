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
print("Assassin's health before combat")
print(assassin.health)
assassin.take_damage(40)
print("Vagabond's health before combat")
print(vagabond.health)
vagabond.take_damage(30)

print(assassin.health)
print(vagabond.health)
