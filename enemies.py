import random

class Enemy:
    def __init__(self, name, hp, attack, defense, attacks):
        self.name = name
        self.hp = int(hp * 1.2)  # Increase enemy HP slightly
        self.attack = attack
        self.defense = int(defense * 1.1)  # Increase enemy defense slightly
        self.attacks = attacks  # Dictionary of attack types

    def perform_attack(self):
        attack_type = random.choice(list(self.attacks.keys()))
        return attack_type, self.attacks[attack_type]

def generate_enemy(player_level):
    enemy_types = [
        ("Goblin", 60, 5, 3, {"Light Attack": 5, "Medium Attack": 8, "Heavy Attack": 12}),
        ("Orc", 85, 8, 5, {"Light Swing": 7, "Medium Swing": 12, "Heavy Smash": 18}),
        ("Skeleton", 72, 6, 4, {"Bone Jab": 6, "Sword Slash": 10, "Crushing Blow": 15}),
        ("Troll", 108, 10, 7, {"Scratch": 9, "Punch": 14, "Club Smash": 20}),
        ("Wolf", 66, 7, 4, {"Bite": 6, "Claw": 10, "Pounce": 14}),
        ("Vampire", 90, 9, 5, {"Drain": 8, "Shadow Strike": 13, "Dark Embrace": 17}),
    ]
    
    weights = [max(1 - (player_level * 0.1), 0.1) for _ in enemy_types]  # Decrease easier enemies over time
    demon_chance = min(0.005 * (2 ** (player_level - 1)), 1.0)  # Demon spawn chance doubles per level
    
    if random.random() < demon_chance:
        return Enemy("Demon", 96, 12, 6, {"Fireball": 10, "Dark Slash": 15, "Hellfire": 22})
    else:
        return Enemy(*random.choices(enemy_types, weights=weights, k=1)[0])
