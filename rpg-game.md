# RPG Game

You will base your game on rpg-5.py and make mods to the game.

## Characters

2. make the hero generate double damage points during an attack with a probabilty of 20%
3. make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
4. make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
5. make a Zombie character that doesn't die even if his health is below zero
6. come up with at least two other characters with their individual characteristics, and implement them.
7. Give each character a number of "prize coins". For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.

## Items

1. make a SuperTonic item to the store, it will restore the hero back to 10 health points.
2. add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
3. add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
4. come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.

## Bonus

1. allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
2. make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
