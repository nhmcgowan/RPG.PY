import random
from Objects import *
import time

class BattleMode:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    

    # Picks a random enemy from a list and resets its stats
    def spawner(self, opponents):
        selected_opponent = random.choice(opponents)
        self.enemy_reset(selected_opponent)
        print(f"{selected_opponent.name} has spawned! {selected_opponent.stats}")
        time.sleep(1)
        return selected_opponent

    # Resets enemy stats and levels up the enemy
    def enemy_reset(self, selected_opponent):
        if selected_opponent.stats["hp"] < selected_opponent.stats["maxhp"]:
            selected_opponent.stats["hp"] = selected_opponent.stats["maxhp"]
            selected_opponent.stats["lvl"] += 1
            selected_opponent.stats["en"] = selected_opponent.stats["maxen"]
            self.enemy_lvlup(selected_opponent)

    # Levels up the enemy by increasing its stats randomly
    def enemy_lvlup(self, selected_opponent):
        for key, value in selected_opponent.stats.items():
            if key not in ["lvl", "hp"]:
                selected_opponent.stats[key] += random.randint(1, 3)

    ## COMBAT LOGIC ##
    # Main battle loop that alternates turns between player and enemy
    def battleloop(self):
        while self.player.alive_check() and self.enemy.alive_check():
            # Enemy's turn
            print(f"{self.enemy.name}'s turn!")
            timer()
            self.enemy_commands()
            if not self.player.alive_check():
                print(f">>>>> {self.player.name} has died. GAME OVER!")
                timer()
                self.reset()
                break

            # Player's turn
            self.player_commands()
            if not self.enemy.alive_check():
                print(f"{self.enemy.name} has been defeated! YOU WIN!")
                timer()
                tracker.stats["Enemies_defeated"] += 1
                timer()
                self.loot()
                self.reset()
                break
    

    ## PLAYER ACTIONS ##
    # Handles player commands during their turn
    def player_commands(self):
        print(f"{self.player.name}'s turn!")
        timer()
        command_dic = {
            "ATTACK": self.player.attack,
            "POWER ATTACK": self.player.power_attack,
            "HEAL": self.player.heal,
            "FLEE": self.attempt_flee,
            "POISON": self.player.special_attack_poison,
            "EXECUTE": self.player.special_attack_execute,
            "REGENERATE": self.player.regenerate,
            "SHOCK": self.player.special_attack_shock,
            "BASH": self.player.special_attack_shieldbash,
            "CHOMP": self.player.special_attack_chomp
        }
        while True:
            command = input("Type a command! Attack, Power Attack, Heal, Flee: ").upper().strip()
            if command in command_dic:
                if command in ["FLEE", "HEAL"]:
                    command_dic[command]()  # Directly execute HEAL or FLEE
                else:
                    # Integrate calc_dmg logic here
                    cost = self.special[command]["cost"]
                    self.player.cost(cost)
                    command_dic[command](self.enemy)  # Execute the attack
                break  # Exit the loop after a valid command is processed
            else:
                print("Invalid Command. Please try again.")
                timer()


    # Handles player's attempt to flee from combat
    def attempt_flee(self):
        flee_attempt = 1
        if flee_attempt > 0:
            print("You fled combat!")
            timer()
            self.reset()
        else:
            print("Flee attempt failed!")
            timer()

    # Handles loot dropped by the enemy after being defeated
    def loot(self):
        dropped_gem = random.choice(["heart", "gold", "shard", "stone"])
        print(f"{self.enemy.name} dropped a {dropped_gem}!")
        timer()
        self.player.equip_gem(dropped_gem, tracker)

    # Resets the game state after combat or game over
    def reset(self):
        from GameClass import Game
        portal = Game()
        if self.player.stats["hp"] == 0:
            print(self.player.check_status())
            timer()
            print(tracker.check_status())
            timer()
            portal.main_menu()
        else:   
            self.player.stats["hp"] = self.player.stats["maxhp"]
            self.player.state["poisoned"] = 0
            self.player.stats["en"] = self.player.stats["maxen"]
            portal.command_menu()
       
    ## ENEMY ACTIONS ##
    # Handles enemy commands during their turn
    def enemy_commands(self):
        command_dic = {
            "ATTACK": self.enemy.attack,
            "POWER ATTACK": self.enemy.power_attack,
            "HEAL": self.enemy.heal
        }
        command_choice = "ATTACK"  # Default choice
        intel = random.randint(1, 3)

        # Decide whether to heal or attack based on enemy's HP and intelligence
        if self.enemy.stats["hp"] <= self.enemy.stats["maxhp"] * 0.3 and intel < 2:
            command_choice = "HEAL"
            command_dic[command_choice]() 
        # Integrate calc_dmg logic here
        if command_choice != "HEAL":
            self.enemy.special_call(self.player)
            command_dic[command_choice](self.player)  # Execute the chosen command