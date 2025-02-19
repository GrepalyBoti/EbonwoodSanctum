# Fantasy Text Adventure Game

## Introduction
Welcome to the **Fantasy Text Adventure Game**! This is a turn-based RPG where you embark on a thrilling journey, encountering various enemies, leveling up your character, and exploring the dark world of **Eldoria**.

## Features
- Choose from **three unique classes**: Warrior, Mage, and Rogue.
- Engage in combat with a variety of **enemies**, each with unique attack styles.
- Enemies scale in difficulty as you progress, with rarer, tougher enemies appearing at higher levels.
- Manage your health, rest, and strategize your attacks based on your character class.
- Immerse yourself in a **rich fantasy lore** with an evolving storyline.

## File Structure
The game is organized into separate modules for **better maintainability**:

```
/game
│── main.py         # Runs the game
│── character.py    # Handles player character attributes and attacks
│── enemies.py      # Defines enemy attributes and attack patterns
│── lore.py         # Contains game story and introduction
│── README.md       # Project documentation
```

## How to Play
1. Run the game using:
   ```sh
   python main.py
   ```
2. Choose your character class.
3. Explore the world, fight enemies, and level up!
4. Rest when needed and strategize your attacks.
5. Defeat the **Demon Boss** at higher levels!

## Character Classes
- **Warrior**: Strong physical attacks with high durability.
- **Mage**: Uses elemental magic for high-damage ranged attacks.
- **Rogue**: Fast and stealthy with critical strike abilities.

## Enemy Scaling
- Common enemies appear more frequently at lower levels.
- Stronger enemies increase in spawn rate as you level up.
- The **Demon Boss** has a very low spawn rate initially but becomes more likely as you progress.

## Future Improvements
- Add an inventory system for potions and weapons.
- Introduce more character classes.
- Expand the lore and add quests.

## Contributions
Feel free to **contribute** to this project! Fork the repository and submit pull requests for improvements.

## License
This project is **open-source** and free to use under the MIT License.
