import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 20
        self.hp = 20
        self.attack = 10
        self.defense = 4
        self.gold = 10
        self.potions = 2
        self.xp = 0
        self.has_used_charged_attack = False

    def attack_monster(self, monster):
        if self.level < 10:
            damage = random.randint(self.attack-2, self.attack+2) - monster.defense
            if damage <= 0:
                damage = 1
            monster.hp -= damage
            print(f"{self.name} attacked {monster.name} and dealt {damage} damage!")
        elif self.level < 15:
            damage = random.randint(self.attack+4, self.attack+10) - monster.defense
            if damage <= 0:
                damage = 1
            monster.hp -= damage
            print(f"{self.name} attacked {monster.name} and dealt {damage} damage!")
        elif self.level < 25:
            damage = random.randint(self.attack+8, self.attack+14) - monster.defense
            if damage <= 0:
                damage = 1
            monster.hp -= damage
            print(f"{self.name} attacked {monster.name} and dealt {damage} damage!")
        elif self.level < 50:
            damage = random.randint(self.attack+14, self.attack+22) - monster.defense
            if damage <= 0:
                damage = 1
            monster.hp -= damage
            print(f"{self.name} attacked {monster.name} and dealt {damage} damage!")
        elif self.level < 100:
            damage = random.randint(self.attack+18, self.attack+32) - monster.defense
            if damage <= 0:
                damage = 1
            monster.hp -= damage
            print(f"{self.name} attacked {monster.name} and dealt {damage} damage!")              


    def is_alive(self):
        return self.hp > 0
    
    def use_potion(self, monster):
        if self.potions > 0:
            self.hp += self.max_hp // 2
            if self.hp > player.max_hp:
                self.hp = player.max_hp
            self.potions -= 1
            print(f"{player.name} used a potion and now has {self.hp}/{self.max_hp} HP!")
            monster.attack_player(player)
        else:
            print(f"{player.name} doesn't have any potions!")
            monster.attack_player(player)
            
    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 6
        self.defense += 4
        self.potions += 1
        print(f"{self.name} leveled up to level {self.level}!")
        
    def buy_potion(self):
        if self.gold >= 5:
            self.gold -= 5
            self.potions += 1
            print(f"{self.name} bought a potion for 5 gold!")
        else:
            print(f"{self.name} does not have enough gold to buy a potion.")
        
    def rest(self):
        if self.gold >= 60:
            self.gold -= 60
            self.hp = self.max_hp    
            print(f"\nYou have rested in the Inn.")
        else:
            print("\nThe Inn Keeper kicks you out of the Inn.")
            
        
    def charged_attack(self, monster):
            if not self.has_used_charged_attack:
                hit_chance = random.uniform(0, 1)
                if hit_chance < 0.75 and self.level < 10:
                    damage = random.randint(self.attack+5, self.attack+10)
                    monster.hp -= damage
                    print(f"{self.name} used a special attack and hit {monster.name} for {damage} damage!")
                elif hit_chance < 0.75 and self.level < 20:
                    damage = random.randint(self.attack+10, self.attack+20)
                    monster.hp -= damage
                    print(f"{self.name} used a special attack and hit {monster.name} for {damage} damage!")
                elif hit_chance < 0.75 and self.level < 50:
                    damage = random.randint(self.attack+20, self.attack+30)
                    monster.hp -= damage
                    print(f"{self.name} used a special attack and hit {monster.name} for {damage} damage!")
                elif hit_chance < 0.75 and self.level < 100:
                    damage = random.randint(self.attack+30, self.attack+45)
                    monster.hp -= damage
                    print(f"{self.name} used a special attack and hit {monster.name} for {damage} damage!")
                else:
                    print(f"{self.name}'s special attack missed!")

                self.has_used_charged_attack = True
            else:
                print(f"{self.name} has already used the charged attack in this battle.")
        
def town(player):
    print("\n==============================")
    print("          TOWN WINDOW         ")
    print("==============================")
    print("\nYou are in the town.")
    print(f"You have {player.gold} gold.")
    print("\n1. Visit the shop")
    print("2. Rest at the inn(requires 60 gold to rest in Inn)")
    print("3. Leave the town")
    choice = input("\nWhat would you like to do? ")
    if choice == "1":
        print("\nWelcome to the shop!")
        print("1. Buy a potion for 5 gold")
        print("2. Exit the Shop")
        shop_choice = input("What would you like to do? ")
        if shop_choice == "1":
            player.buy_potion()
            print(f"\nYou now have {player.potions} potions!")
        elif shop_choice == "2":
            town(player)
        else:
            print("Invalid choice.")
        town(player)
    elif choice == "2":
        player.rest()
        town(player)
    elif choice == "3":
        print("\nYou leave the town.")
    else:
        print("Invalid choice.")
        town(player)
        
def display_player_stats(player):
    print(f"\n{player.name}'s Stats:")
    print(f"Level: {player.level}")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Gold: {player.gold}")
    print(f"Potions: {player.potions}")
    print(f"XP: {player.xp}/{player.level * 10}")

def fight_window(player, monster):
    print("\n==============================")
    print("        BATTLE WINDOW         ")
    print("==============================")
    print(f"Lvl.{player.level} {player.name}: {player.hp}/{player.max_hp} HP, {player.potions} potions")
    print(f"{monster.name}: {monster.hp}/{monster.max_hp} HP")
    print("==============================")
    print("\n1. Attack")
    print("2. Charged Attack(Can only be used once per battle)")
    print("3. Use potion")
    print("4. Run away")
    print("5. Display Stats")
    print("6. Quit the Game")
        
class Monster:
    def __init__(self, name, level, max_hp, attack, defense, gold, xp):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.xp = xp
    
    def attack_player(self, player):
        if self.level < 5:
            damage = random.randint(self.attack, self.attack+4) - player.defense
            if damage <= 0:
                damage = 1
            player.hp -= damage
            print(f"{self.name} attacked {player.name} and dealt {damage} damage!")
        elif self.level < 10:
            damage = random.randint(self.attack+2, self.attack+8) - player.defense
            if damage <= 0:
                damage = 1
            player.hp -= damage
            print(f"{self.name} attacked {player.name} and dealt {damage} damage!")
        elif self.level < 15:
            damage = random.randint(self.attack+4, self.attack+10) - player.defense
            if damage <= 0:
                damage = 1
            player.hp -= damage
            print(f"{self.name} attacked {player.name} and dealt {damage} damage!")
        elif self.level < 25:
            damage = random.randint(self.attack+6, self.attack+12) - player.defense
            if damage <= 0:
                damage = 1
            player.hp -= damage
            print(f"{self.name} attacked {player.name} and dealt {damage} damage!")
        elif self.level < 100:
            damage = random.randint(self.attack+8, self.attack+14) - player.defense
            if damage <= 0:
                damage = 1
            player.hp -= damage
            print(f"{self.name} attacked {player.name} and dealt {damage} damage!")

    def is_alive(self):
        return self.hp > 0

def encounter(player):
    encounter_type = random.choices(["monster", "town"], [0.9, 0.1])[0]
    
    if encounter_type == "monster":
        monster_list = []
        if player.level < 3:
            monster_list = [
                Monster("Goblin", 1, 10, 5, 3, 5, 1),
                Monster("Giant Spider", 2, 14, 6, 1, 8, 1),
            ]
        elif player.level < 5:
            monster_list = [
                Monster("Goblin", 1, 10, 5, 3, 5, 1),
                Monster("Giant Spider", 2, 14, 6, 1, 8, 1),
                Monster("Skeleton Warrior", 5, 20, 8, 6, 12, 2),
                Monster("Orc", 5, 15, 12, 4, 10, 2)
            ]
        elif player.level < 24:
            monster_list = [
                Monster("Goblin", 1, 10, 5, 3, 5, 1),
                Monster("Giant Spider", 2, 14, 6, 1, 8, 1),
                Monster("Skeleton Warrior", 5, 20, 8, 6, 12, 2),
                Monster("Orc", 5, 15, 12, 4, 10, 2),
                Monster("Witch", 10, 20, 10, 5, 20, 3),
                Monster("Troll", 10, 16, 7, 10, 15, 3)
            ]
        elif player.level < 100:
            monster_list = [
                Monster("Goblin", 1, 10, 5, 3, 5, 1),
                Monster("Giant Spider", 2, 14, 6, 1, 8, 1),
                Monster("Skeleton Warrior", 5, 20, 8, 6, 12, 2),
                Monster("Orc", 5, 15, 12, 4, 10, 2),
                Monster("Witch", 5, 20, 10, 5, 20, 3),
                Monster("Troll", 5, 16, 7, 10, 15, 3),
                Monster("Dragon", 7, 20, 10, 10, 50, 10)
            ]

        monster = random.choice(monster_list)
        level_diff = player.level - monster.level
        if level_diff > 0:
            scale_factor = 1 + 0.7 * level_diff
        else:
            scale_factor = 1
        monster.max_hp = int(monster.max_hp * scale_factor)
        monster.hp = monster.max_hp
        monster.attack = int(monster.attack * scale_factor)
        monster.defense = int(monster.defense * scale_factor)
        monster.gold = int(monster.gold * scale_factor)
        monster.xp = int(monster.xp * scale_factor)
        print(f"\nYou encountered a level {monster.level} {monster.name}!")
        while monster.is_alive() and player.is_alive():
            fight_window(player, monster)
            choice = input()
            print("")
            if choice == "1":
                player.attack_monster(monster)
                if monster.is_alive():
                    monster.attack_player(player)
                else:
                    print(f"You defeated the {monster.name}!")
                    player.gold += monster.gold
                    player.xp += monster.xp
                    print(f"You gained {monster.gold} gold and {monster.xp} XP!")
                    if player.xp >= player.level * 5:
                        player.level_up()
                        print(f"{player.name} is now level {player.level}!")
                        break
            elif choice == "2":
                player.charged_attack(monster)
                if monster.is_alive():
                    monster.attack_player(player)
                else:
                    print(f"You defeated the {monster.name}!")
                    player.gold += monster.gold
                    player.xp += monster.xp
                    print(f"You gained {monster.gold} gold and {monster.xp} XP!")
                    if player.xp >= player.level * 5:
                        player.level_up()
                        print(f"{player.name} is now level {player.level}!")
                        break
            elif choice == "3":
                player.use_potion(monster)
            elif choice == "4":
                print(f"{player.name} ran away from the {monster.name}!")
                break
            elif choice == "5":
                display_player_stats(player)
            elif choice == "6":
                exit()
            else:
                print("Invalid choice, try again.")
        if not player.is_alive():
            print(f"{player.name} was defeated by the {monster.name}. Game over!")
        elif not monster.is_alive():
            if monster.name == "Dragon":
                print(f"Congratulations! {player.name} defeated the {monster.name} and saved the kingdom!")
                print("1. Continue to play?")
                print("2. Exit")
                player_decision = input("")
                if player_decision == "1":
                    return
                elif player_decision == "2":
                    exit()
            else:
                print(f"{player.name} defeated the {monster.name} and received {monster.gold} gold and {monster.xp} XP!")
    elif encounter_type == "town":
        town(player)

print("\n                    ==============================")
print("                               Encounter          ")
print("                    ==============================")
print("\nThis is a turn-based fight game. You will encounter mutliple monster to fight against. ")
print("If you beat the Dragon the game will finished but you can still continue with your adventure")
player_name = input("\nEnter your username: ")
player = Player(player_name)
print(f"Welcome, {player_name}! Let's start the game.")

while player.is_alive():
    encounter(player)
    if not player.is_alive():
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() == "y":
            player = Player(player_name)
            print(f"Welcome back, {player_name}! Let's try again.")
        else:
            print("Thanks for playing!")