from GameClass import *

if __name__ == "__main__":
    game = Game()
    game.main_menu()

#refactor player_command

# Expand items/equipment/loot:
def equipment_system():
    #Item Class?
    #item objects hold commands for methods that adjust character attributes: equip, un_equip.
    #Slots for equipment?
    #Methods that 
    return

# Expand character System: (ECS)
# differentiate between resource stats and more static stats.
# Abstract attribute catagories?
#
prototype = Character(
    name="Default",
    stats={"maxhp": 10, "maxmana": 10,  # HP/Mana
           "str": 0, "atk": 0, "def": 0},  # Melee Combat Triad
    resources={"hp": 0,
               "mana": 0,
               "gld": 0},
    state={"poisoned": 0},  # State slots
    special={},
    inventory={}
)