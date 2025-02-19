import random
from character import Character
from enemies import generate_enemy
from lore import get_intro_lore

def main():
    print("Welcome to the Fantasy Text Adventure Game!")
    print(get_intro_lore())
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
