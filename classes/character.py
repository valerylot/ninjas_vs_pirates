import random
# from game import *
class Character:
    def __init__(self, strength, speed, health):
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , opponent):
        success_dodge = opponent.defense(self)
        if success_dodge == False:
            print("Attack is successful!")
            opponent.health -= self.strength
        else:
            print("Attack was dodged!")
        return self
    
    def defense(self, attacker):
        speed_roll = random.randint(0,6)
        print(f"{self.name} rolled a {speed_roll}")
        if speed_roll < self.speed:
            return True
        else:
            return False
