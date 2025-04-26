from CharacterClass import *
# List of opponents for the game
opponents = [
    Character(
        name="Battle Bug",
        resources={},
        stats={
            "maxhp": 30,
            "hp": 30,
            "atk": 3,
            "str": 3,
            "def": 3,
            "lvl": 1,
            "mana": 100,
            "maxmana": 100
        },
        state={"poisoned": 0},
        special={
            "poisonous": {
                "strength": 3,
                "accuracy": 3,
                "duration": 3,
                "cost": 0,
            }
        },
        inventory=["Empty"],
    ),
    Character(
        name="Battle Rat",
        resources={},
        stats={
            "maxhp": 40,
            "hp": 40,
            "atk": 8,
            "str": 5,
            "def": 5,
            "lvl": 1,
            "mana": 100,
            "maxmana": 100
        },
        state={"poisoned": 0},
        special={
            "poisonous": {
                "strength": 5,
                "accuracy": 5,
                "duration": 5,
                "cost": 0
            }
        },
        inventory=["Empty"],
    ),
    Character(
        name="Battle Bear",
        resources={},
        stats={
            "maxhp": 50,
            "hp": 50,
            "atk": 10,
            "str": 10,
            "def": 10,
            "lvl": 1,
            "mana": 100,
            "maxmana": 100
        },
        state={"poisoned": 0},
        special={
            "execute": {
                "cost" : 0
            }
        },
        inventory=["Empty"],
    ),
    Character(
        name="Battle Spider",
        resources={},
        stats={
            "maxhp": 30,
            "hp": 30,
            "atk": 5,
            "str": 5,
            "def": 3,
            "lvl": 1,
            "mana": 100,
            "maxmana": 100
        },
        state={"poisoned": 0},
        special={
            "poisonous": {
                "strength": 10,
                "accuracy": 3,
                "duration": 3,
                "cost": 0
            }
        },
        inventory=["Empty"],
    ),
]

# List of advanced opponents for the game
opponents2 = [
    Character(
        name="Battle Tortoise",
        resources={},
        stats={"maxhp": 100, "hp": 100, "atk": 5, "str": 1, "def": 12, "lvl": 1, "mana": 100, "maxmana": 100},
        state={"poisoned": 0},
        special={
            "regenerate": {
            "cost" : 20
            }
                },
        inventory=["Empty"]
    ),
    Character(
        name="Battle Hare",
        resources={},
        stats={"maxhp": 50, "hp": 50, "atk": 10, "str": 5, "def": 5, "lvl": 1, "mana": 100, "maxmana" : 100},
        state={"poisoned": 0},
        special={},
        inventory=["Empty"]
    ),
    Character(
        name="Battle Sparky",
        resources={},
        stats={"maxhp": 50, "hp": 50, "atk": 10, "str": 1, "def": 1, "lvl": 1, "mana": 100, "maxmana": 100},
        state={"poisoned": 0},
        special={"shock": {
            "cost" : 25
            }
        },
        inventory=["Empty"]
    ),
    Character(
        name="Battle Dog",
        resources={},
        stats={"maxhp": 40, "hp": 40, "atk": 8, "str": 8, "def": 8, "lvl": 1, "mana": 100, "maxmana": 100},
        state={"poisoned": 0},
        special={"chomp": {
            "cost": 0}},
        inventory=["Empty"]
    ),
]

# Shopkeeper character with initial stats and inventory
shopkeeper = Character(
    name="ShopKeeper",
    resources= None,
    stats={"gld" : 0},
    state=None,
    special=None,
    inventory=["heart", "shard", "stone",]
)

# Player character with default stats and empty inventory
player = Character(
    name="Default",
    resources={},
    stats={},
    state={"poisoned" : 0},
    special={},
    inventory=["Empty"]
)

# Tracker character to keep track of game progress
tracker = Character(
    name="Tracker",
    resources= {},
    stats={"Total Bonus": 0, "Enemies_defeated": 0},
    state= {},
    special= {},
    inventory=[]
)

def timer():
    time.sleep(1)