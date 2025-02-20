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
