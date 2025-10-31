class Character():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def take_damage(self, amount):
        self.health -= amount

warrior_1 = Character(100, 20)
warrior_1.take_damage(40)
print(warrior_1.health)
