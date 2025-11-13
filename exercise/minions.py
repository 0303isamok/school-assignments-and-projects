class Minion():
    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage

class Cannon_Minion(Minion):
    def __init__(self, health, speed, damage):
        super().__init__(health, speed, damage)
        health = health *2
    
    def take_damage(self, hit):
        cannon_shot = hit * 1.5
        super().take_damage(cannon_shot)


cannon = Cannon_Minion(100, 20, 40)
cannon.take_damage(20)
print(cannon.health)

