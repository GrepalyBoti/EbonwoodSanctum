import random

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.max_hp = self.calculate_max_health()
        self.hp = self.max_hp
        self.attack = 10
        self.defense = 5
        self.experience = 0
        self.attacks = self.get_class_attacks()
    
    def get_class_attacks(self):
        class_attacks = {
            "Warrior": {"Slash": 10, "Heavy Strike": 15, "Berserk": 20},
            "Mage": {"Fireball": 12, "Lightning Bolt": 18, "Arcane Blast": 25},
            "Rogue": {"Quick Stab": 8, "Shadow Strike": 14, "Deadly Poison": 22}
        }
        return {atk: dmg + (self.level * 2) for atk, dmg in class_attacks.get(self.char_class, {"Basic Attack": 10}).items()}

    def attack_enemy(self, enemy, attack_type):
        damage = self.attacks.get(attack_type, 10) - enemy.defense
        if damage > 0:
            enemy.hp -= damage
        return damage

    def level_up(self):
        self.level += 1
        self.max_hp = self.calculate_max_health()
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        self.attacks = self.get_class_attacks()  # Update attack values on level up

    def calculate_max_health(self):
        return 100 + (self.level - 1) * 20
    
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

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

def main():
    print("Welcome to the Fantasy Text Adventure Game!")
    player_name = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    class_choice = input("Enter the number of your choice: ")

    classes = { "1": "Warrior", "2": "Mage", "3": "Rogue" }
    player_class = classes.get(class_choice, "Warrior")
    
    player = Character(player_name, player_class)
    print(f"Welcome, {player.name} the {player.char_class}!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. View Character")
        print("3. Rest")
        print("4. Short rest")
        print("9. Exit Game")
        action = input("Enter the number of your choice: ")
        
        if action == "1":
            encounter = random.choice(["enemy", "nothing"])
            if encounter == "enemy":
                enemy = generate_enemy(player.level)
                print(f"A wild {enemy.name} appears!")
                while enemy.hp > 0 and player.hp > 0:
                    print(f"Your HP: {player.hp}/{player.max_hp}, Enemy HP: {enemy.hp}")
                    print("Choose an attack:")
                    for i, attack in enumerate(player.attacks.keys(), 1):
                        print(f"{i}. {attack}")
                    attack_choice = input("Enter the number of your choice: ")
                    attack_list = list(player.attacks.keys())
                    if attack_choice.isdigit() and 1 <= int(attack_choice) <= len(attack_list):
                        attack_type = attack_list[int(attack_choice) - 1]
                        damage = player.attack_enemy(enemy, attack_type)
                        print(f"You used {attack_type} and dealt {damage} damage to the {enemy.name}.")
                        if enemy.hp > 0:
                            attack_type, enemy_damage = enemy.perform_attack()
                            player.hp -= max(0, enemy_damage - player.defense)
                            print(f"The {enemy.name} used {attack_type} and dealt {enemy_damage} damage to you.")
                        else:
                            print(f"You defeated the {enemy.name}!")
                            player.experience += 50
                            if player.experience >= 100:
                                player.level_up()
                                player.experience = 0
                                print(f"Congratulations! You've leveled up to level {player.level}!")
                    else:
                        print("Invalid choice, try again.")
            else:
                print("You walk into the dark woods deeper.")
        elif action == "9":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
