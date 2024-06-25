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
    
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.hp -= damage
        return damage

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3

    def calculate_max_health(self):
        return 100 + (self.level - 1) * 20
    

class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

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

    # Example of a simple game loop
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
                enemy = Enemy("Goblin", 50, 5, 2)
                print(f"A wild {enemy.name} appears!")
                while enemy.hp > 0 and player.hp > 0:
                    print(f"Your HP: {player.hp}, Enemy HP: {enemy.hp}")
                    print("1. Attack")
                    print("2. Run")
                    combat_action = input("Enter the number of your choice: ")
                    if combat_action == "1":
                        damage = player.attack_enemy(enemy)
                        print(f"You dealt {damage} damage to the {enemy.name}.")
                        if enemy.hp > 0:
                            enemy_damage = max(0, enemy.attack - player.defense)
                            player.hp -= enemy_damage
                            print(f"The {enemy.name} dealt {enemy_damage} damage to you.")
                        else:
                            print(f"You defeated the {enemy.name}!")
                            player.experience += 50
                            if player.experience >= 100:
                                player.level_up()
                                print(f"Congratulations! You've leveled up to level {player.level}.")
                    elif combat_action == "2":
                        print("You ran away!")
                        break
                    if player.hp <= 0:
                        print("You have been defeated. Game over.")
                        return
            else:
                print("You walk in to the dark woods deeper.")
        elif action == "2":
            print(f"Name: {player.name}")
            print(f"Class: {player.char_class}")
            print(f"Level: {player.level}")
            print(f"HP: {player.hp}")
            print(f"Attack: {player.attack}")
            print(f"Defense: {player.defense}")
        elif action == "3":
            print("You rest and recover your strength.")
            player.hp = 100  # Simplified full heal
        elif action == "4":
            print("You rest and recover your strength.")
            player.hp += 50 # Simplified half heal
        elif action == "9":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
