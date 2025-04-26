from Objects import *
from BattlemodeClass import *
import time

class Game:
    def __init__(self):
        # Initialize the game with no active battle and a player object
        self.battle = None
        self.player = player

    # MAIN MENU
    def main_menu(self):
        # Display the main menu and handle user commands
        print("Welcome to RPG.py, a text-based RPG that you can play in your terminal!")
        timer()
        commands = {
            "START": self.character_creator,  # Start the game by creating a character
            "QUIT": lambda: print("Goodbye."),  # Exit the game
            "HELP": lambda: print(
                "You will be prompted with various commands.\n"
                "Please enter your choice of command with accurate spelling.\n"
                "Commands are not case sensitive.\n"
                "In combat, different kinds of attacks scale off different stats.\n"
                "Enemies are randomly selected from different lists.\n"
                "When an enemy is killed, the next time you see them they will have leveled up. \n"
                "Enemies drop items that grant variable stat bonuses, they will automatically be equipped when you receive them."
            )  # Display help information
        }
        # Simulate user input for testing purposes
        game = "START"  #input("Start/Quit").strip().upper()
        if game in commands:
            commands[game]()  # Execute the corresponding command
            if game != "QUIT":
                self.main_menu()  # Return to the main menu if the game is not quitting
        else:
            print("Please enter a valid command.")
            timer()
            self.main_menu()  # Retry the main menu if input is invalid

    # CHARACTER CREATOR
    def character_creator(self):
        # Allow the player to choose a character class and set up their stats
        print("Please pick a class: Knight/Warrior/Rogue")
        timer()
        classes = {
            "KNIGHT": {
                "stats": {
                    "maxhp": 50,
                    "hp": 50,
                    "atk": 8,
                    "str": 8,
                    "def": 8,
                    "en": 100,
                    "maxen" : 100,
                    "gld": 0
                },
                "special": {
                    "shield bash": {
                        "cost":20
                    }
                }
            },
            "WARRIOR": {
                "stats": {
                    "maxhp": 40,
                    "hp": 40,
                    "atk": 5,
                    "str": 12,
                    "def": 5,
                    "en": 100,
                    "maxen" : 100,
                    "gld": 0
                },
                "special": { 
                    "execute": {
                        "cost": 0
                    }
                }
            },
            "ROGUE": {
                "stats": {
                    "maxhp": 40,
                    "hp": 40,
                    "atk": 12,
                    "str": 5,
                    "def": 5,
                    "en": 100,
                    "maxen" : 100,
                    "gld": 50
                },
                "special": {
                    "chomp":{
                        "cost": 0
                    }
                    }
            }
        }
        for class_name, details in classes.items():
            print(f"\nClass: {class_name}")
            #time.sleep(.5)
            print("Stats:")
            #time.sleep(.5)
            for stat, value in details["stats"].items():
                print(f"  {stat.capitalize()}: {value}")
                #time.sleep(.5)
            print("Special Abilities:")
            #time.sleep(.5)
            for ability, value in details["special"].items():
                print(f"  {ability.capitalize()}: {value}")
                #timer()
        class_choice = "KNIGHT" #input("Knight/Warrior/Rogue: ").strip().upper()  # Get user input for class choice
        print(f"You have chosen {class_choice}.")
        #timer()
        self.player.stats = classes[class_choice]["stats"]  # Assign chosen class stats to the player
        self.player.special = classes[class_choice]["special"]
        name = "BINGUS"  #input("Name your character: ")
        self.player.name = name  # Set the player's name
        print(self.player.check_status())  # Display the player's status
        #timer()
        self.command_menu()  # Proceed to the command menu

    # PLAYER CONTROL
    def command_menu(self):
        # Handle player commands during gameplay
        command_input = input(
            "Type 'BATTLE' to commence battle/'EQUIP' to check equipped items/'CHECK' to check player status/'SHOP' to see the store: "
        ).strip().upper()  # Get user input for commands
        command_dict = {
            "CHECK": lambda: print(self.player.check_status()),  # Check player status
            #"EQUIP": lambda: print(self.player.equipment_screen()),  # Manage equipment
            "SHOP": lambda: player.trade(player, shopkeeper),  # Access the shop
            "HELP": lambda: print(self.help()),
            "BATTLE" : lambda: self.battle_command()
        }
        if command_input in command_dict:
            command_dict[command_input]()  # Execute the corresponding command
            timer()
            self.command_menu()  # Return to the command menu
        else:
            print("Invalid command. Please try again.")
            timer()
            self.command_menu()  # Retry the command menu if input is invalid

    # PORTAL TO BATTLEMODE
    def battle_command(self):
        # Start a battle by initializing the battle mode
        print("Starting a battle...")
        timer()
        battle = BattleMode(self.player, None)  # Create a battle instance with the player
        selection_choice = input("Village or Forest?").strip().upper()
        if selection_choice == "VILLAGE":
            selection = battle.spawner(opponents)  # Spawn an opponent
        elif selection_choice == "FOREST":
            selection = battle.spawner(opponents2)
        self.battle = BattleMode(self.player, selection)  # Initialize the battle with the selected opponent
        self.battle.battleloop()  # Start the battle loop

    def help(self):
        return print(f"Power Attack: Lower accuracy, high damage variance, high damage potential.\n" 
    "Atttack: accurate, higher dmg floor, moderate damage ceiling.\n" 
    "Heal: moderately powerful heal \n"
    "Flee: 50-50 chance to flee combat, otherwise miss turn.")