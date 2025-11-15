class Minion():
    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage

    def take_damage(self, hit):
        self.health -= hit

    def attack(self, target):
        target.take_damage(self.damage)


class Cannon_Minion(Minion):
    def __init__(self, health, speed, damage):
        super().__init__(health, speed, damage)
        self.health = self.health *2
        self.damage = self.damage 
    def take_damage(self, hit):
        modified_hit = hit * 0.5
        super().take_damage(modified_hit)

class Range_Minion(Minion):
    def __init__(self, health, speed, damage):
        super().__init__(health, speed, damage)
        self.health = self.health * 0.8
        self.damage = self.damage * 2
class Fighter_Minion():
    pass


cannon = Cannon_Minion(100, 20, 40)
ranged = Range_Minion(100, 20, 40)


ranged.attack(cannon)
cannon.attack(ranged)

print(cannon.health)
print(ranged.health)

