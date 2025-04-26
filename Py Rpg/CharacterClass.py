import random
import time
import math

class Character:
    def __init__(self, name, stats, resources, state, special, inventory):
        # Initialize the character with a name, stats, and inventory.
        self.name = name
        self.stats = stats
        self.resources = resources
        self.state = state
        self.special = special
        self.inventory = inventory

    # INFORMATION #
    def check_status(self):
        # Returns the character's name, stats, and inventory.
        return f"Name: {self.name}, Stats: {self.stats}, Special: {self.special}, Inventory: {self.inventory}."

    # DEFENSE #
    def def_roll(self):
        defense_roll = random.randint(1, self.stats["def"])
        return defense_roll

    def dmg_red(self, dmg):
        def_roll = self.def_roll()
        if def_roll >= dmg:
            print(f"{self.name} blocks the attack!")
            time.sleep(1)
        else:
            dmg_final = dmg - def_roll
            print(f"{self.name} blocks {def_roll} dmg.")
            time.sleep(1)
            self.rec_dmg(dmg_final)

    def heal(self):
        # Heal the character by a random amount based on their strength.
        heal = random.randint(self.stats["str"], self.stats["str"] * 2)
        self.stats["hp"] += heal
        print(f"{self.name} heals {heal} dmg, and now has {self.stats['hp']} hp left.")
        time.sleep(1)
        
    def regenerate(self):
        heal = random.randint(0, self.stats["str"])
        self.stats["hp"] += heal
        regen = int(self.stats["maxen"] * .25)
        self.stats["en"] += regen
        print(f"{self.name} regens {regen} energy and {heal} hp.")

    # CHECKS #
    def rec_dmg(self, dmg):
        # Reduce the character's HP by the damage received.
        self.stats["hp"] -= dmg
        if dmg < 0:
            dmg = 0
        if self.stats["hp"] < 0:
            self.stats["hp"] = 0
        print(f"{self.name} takes {dmg} dmg and has {self.stats['hp']} hp left.")
        time.sleep(1)

    def alive_check(self):
        # Check if the character is still alive (HP > 0).
        return self.stats["hp"] > 0

    def attack_check(self, target, att_roll, def_roll):
        if att_roll >= def_roll:
            return True
        else:
            print(f"{target.name} blocks the attack!")
            time.sleep(1)
            return False

    # INVENTORY MANAGEMENT #
    def equip_gem(self, item, tracker):
        # Equip an item and apply its effects to the character's stats.
        gem_effects = {
            "shard": {
                "stat": "atk",
                "bonus": lambda: random.randint(2, 5),
                "message": lambda bonus: f"The shard glitters, granting you {bonus} atk."
            },
            "heart": {
                "stat": "maxhp",
                "bonus": lambda: random.randint(5, 10),
                "message": lambda bonus: f"The heart throbs, granting you {bonus} max hp."
            },
            "stone": {
                "stat": "def",
                "bonus": lambda: random.randint(2, 5),
                "message": lambda bonus: f"A sturdy stone. Increases def by {bonus}."
            },
            "gold": {
                "stat": "gld",
                "bonus": lambda: max(1, min(100, round(random.gauss(50, 10)))),
                "message": lambda bonus: f"Shiny! You found {bonus} gold pieces. Total gold: {self.stats['gld']}."
            }
        }

        if item in gem_effects:
            effect = gem_effects[item]
            bonus = effect["bonus"]()
            self.stats[effect["stat"]] += bonus
            if effect["stat"] != "gld":
                tracker.stats["Total Bonus"] += bonus
            print(effect["message"](bonus))
            time.sleep(1)
        else:
            print(f"{item} cannot be equipped.")
            time.sleep(1)

    def trade(self, player, target):
        # Trade items between the player and a shopkeeper.
        from Objects import tracker
        print(
            f"For sale: {target.inventory}\n"
            "Price: 50 gold each \n"
            f"You have {player.stats['gld']} gold. \n"
            "Type in what item you want to purchase."
        )
        time.sleep(1)
        gem_choice = input()
        if player.stats["gld"] >= 50:
            player.stats["gld"] -= 50
            target.stats["gld"] += 50
            self.equip_gem(gem_choice, tracker)
        else:
            print("You don't have the money!")
            time.sleep(1)

    # SPECIAL EFFECTS #
    # Dynamically detects, selects, calls a pa
    def special_call(self, target):
        # command = check if the special attribute has a value:
        if self.special:
            command = next(iter(self.special.keys()))
            cost = self.special[command]["cost"]
             # Check if the ability has a cost and if the player has enough energy

    # Deduct the energy cost
            self.cost(cost)
            command_dic = {
                "poisonous": lambda: self.special_attack_poison(target),
                "execute": lambda: self.special_attack_execute(target),
                "regenerate": lambda: self.heal(),
                "shock": lambda: self.special_attack_shock(target),
                "shield bash": lambda: self.special_attack_shieldbash(target),
                "chomp": lambda: self.special_attack_chomp(target)
            }
            # match the special attribute to a command in the dictionary and run it
            command_dic[command]()

    # Records energy cost of ability
    def cost(self, cost):
        if cost > 0 and self.stats.get("en", 0) > cost:
            self.stats["en"] -= cost
            print(f"-{cost} energy, {self.stats['en']} en left")
            time.sleep(1)

    # list of attacks:
    def attack(self, target):
        # Perform a basic attack. Damage is calculated based on attack and a random str bonus.
        att_roll = random.randint(1, self.stats["atk"] * 2)
        if self.attack_check(target, att_roll, target.def_roll()) == True:
            bns = random.randint(1, self.stats["str"])
            dmg = self.stats["atk"] + bns
            print(f"{self.name} attacks for {dmg}!")
            time.sleep(1)
            target.dmg_red(dmg)

    def power_attack(self, target):
        # Perform a power attack. Damage is doubled but the attack roll is smaller.
        att_roll = random.randint(1, self.stats["atk"])
        if self.attack_check(target, att_roll, target.def_roll()) == True:
            dmg = random.randint(self.stats["str"], self.stats["str"] * 3)
            print(f"{self.name} attacks for {dmg}!")
            time.sleep(1)
            target.dmg_red(dmg)
    # poison inflict
    def special_attack_poison(self, target):
        if target.state["poisoned"] < 1:
            poison_resist = target.def_roll()
            if self.special["poisonous"]["accuracy"] > poison_resist:
                target.state["poisoned"] += self.special["poisonous"]["duration"]
                print(f"Poison inflicted!")
                time.sleep(1)
                self.poison(target)
            else:
                print(f"{target.name} resisted the poison!")
                time.sleep(1)
        else:
            self.poison(target)

    # poison tick
    def poison(self, target):
        if target.state["poisoned"] > 0:
            p_dmg = random.randint(1, self.special["poisonous"]["strength"])
            print(f"Poison! {target.name} has {target.state['poisoned']} turns of poison left.")
            time.sleep(1)
            target.rec_dmg(p_dmg)
            target.state["poisoned"] -= 1

    # execute
    def special_attack_execute(self, target):
        if target.stats["hp"] < target.stats["maxhp"] * .30:
            att_roll = random.randint(0, self.stats["atk"])
            if self.attack_check(target, att_roll, target.def_roll()) == True:
                print(f"{self.name} casts execute!")
                time.sleep(1)
                missing_hp = target.stats["maxhp"] - target.stats["hp"]
                dmg = math.ceil(missing_hp * .15)
                target.rec_dmg(dmg)

    # shock
    def special_attack_shock(self, target):
            dmg = math.ceil(target.stats["maxhp"] * .10)
            print(f"Zap! {self.name} shocks {target.name} for {dmg} dmg!")
            time.sleep(1)
            target.rec_dmg(dmg)

    def special_attack_shieldbash(self, target):
            dmg = random.randint(0, self.stats["def"])
            print(f"Shield bash does {dmg} dmg!")
            time.sleep(1)
            target.rec_dmg(dmg)

    def special_attack_chomp(self, target):
            att_roll = random.randint(1, self.stats["atk"])
            if self.attack_check(target, att_roll, target.def_roll()) == True:
                dmg = random.randint(1, self.stats["atk"])
                bns = random.randint(0, self.stats["str"])
                final_dmg = dmg + bns
                print(f"Chomp!")
                time.sleep(1)
                target.dmg_red(final_dmg)
                self.stats["hp"] += int(final_dmg * .5)
                print(f"{self.name} heals for {int(final_dmg * .5)}")
                time.sleep(1)