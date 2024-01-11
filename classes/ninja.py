from classes.character import Character
class Ninja(Character):

    def __init__( self , name, strength=15, speed=3, health=100):
        self.name = name
        super().__init__(strength, speed, health)
        self.blowgun_attack_count = 3

    def blowgun_attack(self,opponent):
        if self.blowgun_attack_count > 0:
            success_dodge = opponent.defense(self)
            if success_dodge == False:
                print("Attack is successful!")
                opponent.health -= self.strength*2
                self.blowgun_attack_count -= 1
                print("You've used 1 Blowgun Attack")
        else: 
            print("Attack was dodged!")
            print("You've used all your Blowgun Attacks!")