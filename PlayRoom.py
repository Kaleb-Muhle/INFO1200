import random
import sys

#!/usr/bin/env python3

class Weapon:
    def __init__(self, name, damage, accuracy, speed):
        self.name = name
        self.damage = damage      # base hit damage
        self.accuracy = accuracy  # percent chance to hit (0-100)
        self.speed = speed        # action points gained per tick

    def __str__(self):
        return f"{self.name}: dmg={self.damage}, acc={self.accuracy}%, spd={self.speed}"

class Combatant:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.weapon = weapon
        self.gauge = 0  # action points accumulator

    def alive(self):
        return self.hp > 0

    def try_attack(self, target):
        hit_roll = random.uniform(0, 100)
        if hit_roll <= self.weapon.accuracy:
            # small damage variance
            dmg = max(1, int(random.normalvariate(self.weapon.damage, max(0.5, self.weapon.damage*0.15))))
            target.hp -= dmg
            print(f"{self.name} hits {target.name} with {self.weapon.name} for {dmg} dmg (target {max(0,target.hp)}/{target.max_hp})")
        else:
            print(f"{self.name} misses {target.name} with {self.weapon.name}")

def choose_weapon():
    # Define weapons per specification
    sword = Weapon("Sword", damage=4, accuracy=70, speed=40)  # least damage, fastest, middle accuracy
    spear = Weapon("Spear", damage=7, accuracy=85, speed=20)  # mid damage, highest accuracy, slowest
    axe   = Weapon("Axe",   damage=10, accuracy=55, speed=30) # most damage, worst accuracy, middle speed
    weapons = {"1": sword, "2": spear, "3": axe}

    print("Choose your weapon:")
    for k, w in weapons.items():
        print(f" {k}) {w}")
    choice = input("Enter 1/2/3: ").strip()
    if choice not in weapons:
        print("Invalid choice.")
        sys.exit(1)
    return weapons[choice], (sword, spear, axe)

def build_stick(weapons):
    # stick uses the worst of all other weapons (min damage, min accuracy, min speed)
    min_damage = min(w.damage for w in weapons)
    min_accuracy = min(w.accuracy for w in weapons)
    min_speed = min(w.speed for w in weapons)
    return Weapon("Stick", damage=min_damage, accuracy=min_accuracy, speed=min_speed)

def simulate(player, enemy):
    TICK_THRESHOLD = 100
    print(f"\nCombat start: {player.name} ({player.weapon}) vs {enemy.name} ({enemy.weapon})\n")
    round_count = 0
    while player.alive() and enemy.alive():
        round_count += 1
        # accumulate action gauges
        player.gauge += player.weapon.speed
        enemy.gauge += enemy.weapon.speed

        acted = False
        # allow multiple actions if gauge large
        while player.gauge >= TICK_THRESHOLD and enemy.alive() and player.alive():
            player.gauge -= TICK_THRESHOLD
            player.try_attack(enemy)
            acted = True

        while enemy.gauge >= TICK_THRESHOLD and player.alive() and enemy.alive():
            enemy.gauge -= TICK_THRESHOLD
            enemy.try_attack(player)
            acted = True

        if not acted:
            # if nobody reached threshold, advance a small time step to avoid infinite loop
            # small pause simulated by artificially bumping both gauges slightly (here just continue loop)
            # to keep output from being too spammy, we won't print idle ticks
            # To ensure termination if speeds are zero (shouldn't be), break.
            if player.weapon.speed <= 0 and enemy.weapon.speed <= 0:
                print("No one can act. Stalemate.")
                break

    print("\n--- Combat Result ---")
    if player.alive() and not enemy.alive():
        print(f"{player.name} wins!")
    elif enemy.alive() and not player.alive():
        print(f"{enemy.name} wins!")
    else:
        print("Draw.")

def main():
    random.seed()  # system time
    chosen_weapon, all_weapons = choose_weapon()
    player = Combatant("Player", hp=50, weapon=chosen_weapon)
    stick_weapon = build_stick(all_weapons)
    enemy = Combatant("Enemy (Stick)", hp=50, weapon=stick_weapon)
    simulate(player, enemy)

if __name__ == "__main__":
    main()