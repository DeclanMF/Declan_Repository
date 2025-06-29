import time
import random

# --- Game Data ---
CARS = {
    "The Apex": {"vulnerabilities": ["hotwire", "engine_tamper"], "value": 50000, "status": "secure"},
    "The Sentinel": {"vulnerabilities": ["electronic_jam", "remote_access"], "value": 75000, "status": "secure"},
    "The Wanderer": {"vulnerabilities": ["physical_ram", "tire_slash"], "value": 30000, "status": "secure"}
}

DEFENSES = {
    "Reinforced Doors": {"cost": 100, "effectiveness": {"hotwire": 3, "physical_ram": 1}, "installed": False},
    "Advanced Alarm System": {"cost": 150, "effectiveness": {"electronic_jam": 1, "smash_window": 3},
                              "installed": False},
    "Automated Oil Slick": {"cost": 200, "effectiveness": {"getaway_attempt": 2}, "installed": False, "uses": 1},
    "Remote Immobilizer": {"cost": 500, "effectiveness": {"getaway_attempt": 3, "hotwire": 2}, "installed": False,
                           "cooldown": 3},
    "Guard Dog": {"cost": 500, "effectiveness": {"smash_window": 2, "physical_ram": 1}, "installed": False}
}

SYNDICATES = {
    "Ghost Riders": {"threats": ["hotwire", "electronic_jam", "remote_access"],
                     "narrative": "Known for their silent, digital incursions. They leave no trace... usually."},
    "Iron Claws": {"threats": ["tow_truck", "physical_ram", "smash_window"],
                   "narrative": "Brutal and unsubtle. They prefer brute force, often with heavy machinery."},
    "Shadow Brokers": {"threats": ["distraction", "misdirection", "decoy_alarm"],
                       "narrative": "Masters of deception. They confuse and misdirect before making their move."}
}

player_money = 2000
player_reputation = 0
current_garage_level = 1
stolen_cars_count = 0


# --- Game Functions ---

def clear_screen():
    # Basic clear for text-based games
    print("\n" * 50)


def display_header(title):
    clear_screen()
    print("-" * (len(title) + 4))
    print(f"| {title} |")
    print("-" * (len(title) + 4))
    print("\n")


def check_garage_status():
    display_header("GARAGE STATUS")
    print(f"Funds: ${player_money}")
    print(f"Reputation: {player_reputation}")
    print("\n--- Your Vehicles ---")
    for car_name, data in CARS.items():
        status = data["status"]
        if status == "stolen":
            print(f"- {car_name}: STOLEN!")
        else:
            print(f"- {car_name}: {status.capitalize()} (Value: ${data['value']})")
            print(f"  Vulnerabilities: {', '.join(data['vulnerabilities'])}")

    print("\n--- Installed Defenses ---")
    installed_any = False
    for def_name, data in DEFENSES.items():
        if data["installed"]:
            installed_any = True
            print(f"- {def_name}")
    if not installed_any:
        print("No defenses currently installed.")

    input("\nPress Enter to continue...")


def visit_parts_dealer():
    global player_money
    display_header("PARTS DEALER & UPGRADES")
    print(f"Current Funds: ${player_money}")
    print("\nAvailable Defenses:")
    for i, (def_name, data) in enumerate(DEFENSES.items()):
        status = "Installed" if data["installed"] else f"Cost: ${data['cost']}"
        print(f"{i + 1}. {def_name} ({status})")

    print("\n(Type 'back' to return to Garage)")

    while True:
        choice = input("Enter number to buy/install, or 'back': ").lower()
        if choice == 'back':
            break
        try:
            choice_idx = int(choice) - 1
            def_name = list(DEFENSES.keys())[choice_idx]
            def_data = DEFENSES[def_name]

            if def_data["installed"]:
                print(f"'{def_name}' is already installed.")
            elif player_money >= def_data["cost"]:
                player_money -= def_data["cost"]
                def_data["installed"] = True
                print(f"Successfully installed '{def_name}'! Funds remaining: ${player_money}")
                time.sleep(1)
                # Refresh display to show updated status
                visit_parts_dealer()
                return  # Exit after successful purchase
            else:
                print("Not enough funds!")
        except (ValueError, IndexError):
            print("Invalid choice.")

    input("\nPress Enter to continue...")


def main_garage_menu():
    while True:
        display_header(f"GUARDIAN GARAGE - LEVEL {current_garage_level}")
        print("What would you like to do?")
        print("1. Check Garage Status")
        print("2. Visit Parts Dealer (Buy Defenses)")
        print("3. Undertake a New Operation (Start a mission)")
        print("4. Exit Game")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_garage_status()
        elif choice == '2':
            visit_parts_dealer()
        elif choice == '3':
            if not any(car["status"] == "secure" for car in CARS.values()):
                print("\nAll your cars have been stolen! Game Over.")
                time.sleep(2)
                return False  # End game
            return True  # Proceed to mission setup
        elif choice == '4':
            print("Exiting Guardian Garage. See you next time!")
            return False  # End game
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


def choose_target_car():
    display_header("SELECT TARGET FOR DEFENSE")
    available_cars = [name for name, data in CARS.items() if data["status"] == "secure"]
    if not available_cars:
        return None

    print("Which car will you focus your defenses on for the next threat?")
    for i, car_name in enumerate(available_cars):
        print(f"{i + 5}. {car_name}")

    while True:
        try:
            choice_idx = int(input("Enter number: ")) - 1
            if 0 <= choice_idx < len(available_cars):
                return available_cars[choice_idx]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


def conduct_operation(target_car_name):
    global player_reputation, stolen_cars_count, player_money

    target_car = CARS[target_car_name]

    # Randomly select a syndicate and their threat
    syndicate_name = random.choice(list(SYNDICATES.keys()))
    syndicate_info = SYNDICATES[syndicate_name]
    thief_approach = random.choice(syndicate_info["threats"])

    display_header(f"OPERATION: PROTECT THE {target_car_name.upper()}!")
    print(f"Intel Report: A new threat emerges from the '{syndicate_name}' syndicate.")
    print(f"{syndicate_info['narrative']}")
    print(f"Their scouts indicate they'll attempt a '{thief_approach.replace('_', ' ')}' maneuver.")
    print(f"\nTarget Car Vulnerabilities: {', '.join(target_car['vulnerabilities'])}")
    input("\nPrepare for impact! Press Enter...")

    thief_progress = 0
    max_thief_progress = 5  # How many successful thief actions before car is stolen
    turns_taken = 0
    max_turns = 10  # Max turns before police arrive (or they give up)

    # Cooldowns for defenses
    defense_cooldowns = {def_name: 0 for def_name in DEFENSES}

    while thief_progress < max_thief_progress and turns_taken < max_turns:
        turns_taken += 1
        print(f"\n--- Turn {turns_taken} ---")
        print(f"Thief Progress: {thief_progress}/{max_thief_progress}")

        # Decrement cooldowns
        for def_name in defense_cooldowns:
            if defense_cooldowns[def_name] > 0:
                defense_cooldowns[def_name] -= 1

        print("\nWhat action do you take?")
        available_actions = []
        for i, (def_name, data) in enumerate(DEFENSES.items()):
            if data["installed"]:
                cooldown_status = ""
                if "cooldown" in data and defense_cooldowns[def_name] > 0:
                    cooldown_status = f" (Cooldown: {defense_cooldowns[def_name]} turns)"
                elif "uses" in data:
                    cooldown_status = f" (Uses Left: {data['uses']})"
                available_actions.append(f"{len(available_actions) + 1}. {def_name}{cooldown_status}")

        if not available_actions:
            print("No defenses available. You rely on luck!")
        else:
            for action in available_actions:
                print(action)
            print(f"{len(available_actions) + 1}. Do Nothing (Observe)")

        action_choice = input("Enter your choice: ")

        chosen_defense_name = ""
        chosen_defense_data = {}
        try:
            choice_idx = int(action_choice) - 1
            if 0 <= choice_idx < len(available_actions):
                chosen_defense_name = available_actions[choice_idx].split('.')[1].split('(')[0].strip()
                chosen_defense_data = DEFENSES[chosen_defense_name]

                if "cooldown" in chosen_defense_data and defense_cooldowns[chosen_defense_name] > 0:
                    print(f"'{chosen_defense_name}' is on cooldown. Choose another action.")
                    continue  # Skip this turn's defense action
                if "uses" in chosen_defense_data and chosen_defense_data["uses"] <= 0:
                    print(f"'{chosen_defense_name}' has no uses left. Choose another action.")
                    continue

                print(f"You activate: {chosen_defense_name}!")
                if "cooldown" in chosen_defense_data:
                    defense_cooldowns[chosen_defense_name] = chosen_defense_data["cooldown"]
                if "uses" in chosen_defense_data:
                    chosen_defense_data["uses"] -= 1

            elif choice_idx == len(available_actions):  # Do nothing option
                print("You decide to observe the situation.")
            else:
                print("Invalid action. You hesitate.")
        except (ValueError, IndexError):
            print("Invalid input. You hesitate.")

        # --- Thief's Action ---
        print(f"\nThe {syndicate_name} attempt a '{thief_approach.replace('_', ' ')}'!")

        # Calculate defense effectiveness
        defense_value = 0
        if chosen_defense_name and thief_approach in chosen_defense_data.get("effectiveness", {}):
            defense_value = chosen_defense_data["effectiveness"][thief_approach]
            print(f"Your {chosen_defense_name} provides {defense_value} points of defense!")
        elif chosen_defense_name and chosen_defense_data["installed"]:
            print(
                f"Your {chosen_defense_name} isn't specifically effective against {thief_approach.replace('_', ' ')}.")

        # Thief's base success chance (can be randomized or based on level)
        thief_power = random.randint(1, 5) + (current_garage_level - 1) * 50  # Thieves get tougher

        # Adjust thief power if target car is vulnerable
        if thief_approach in target_car["vulnerabilities"]:
            thief_power += 2
            print(f"WARNING! The {target_car_name} is vulnerable to this attack!")

        net_effect = thief_power - defense_value

        if net_effect > 0:
            thief_progress += net_effect
            print(f"The thieves made {net_effect} progress! Current progress: {thief_progress}/{max_thief_progress}")
            # Optional: Add consequences for car damage, alarm being disabled etc.
        else:
            print("You successfully deterred the thieves!")
            thief_progress = max(0, thief_progress - 1)  # Push them back slightly

        time.sleep(2)

    # --- End of Operation ---
    print("\n--- OPERATION RESOLVED ---")
    if thief_progress >= max_thief_progress:
        print(f"FAILURE! The {target_car_name} has been stolen by the {syndicate_name}!")
        CARS[target_car_name]["status"] = "stolen"
        stolen_cars_count += 1
        player_reputation = max(0, player_reputation - 10)  # Reputation hit
        player_money += 100  # Consolation money for parts
    else:
        print(f"SUCCESS! You successfully defended the {target_car_name} from the {syndicate_name}!")
        player_reputation += 15  # Reputation gain
        player_money += 500  # Reward
        # Reset some defenses for next round if they have uses
        for def_name, data in DEFENSES.items():
            if "uses" in data and data["uses"] < DEFENSES[def_name].get("max_uses", 1):  # If you add max_uses
                data["uses"] = DEFENSES[def_name].get("max_uses", 1)  # Reset uses

    input("\nPress Enter to return to garage...")


# --- Game Start ---
if __name__ == "__main__":
    display_header("WELCOME TO GUARDIAN GARAGE: THE URBAN GAUNTLET")
    print("In a city plagued by organized crime, your unique collection of vehicles is under threat.")
    print("It's up to you to fortify your garage and outwit the criminal syndicates.")
    print("Good luck, mechanic!")
    input("\nPress Enter to begin your journey...")

    game_running = True
    while game_running:
        game_running = main_garage_menu()  # Goes to garage menu, returns False to exit game

        if game_running:  # If player chose to undertake a mission
            target_car_for_mission = choose_target_car()
            if target_car_for_mission:
                conduct_operation(target_car_for_mission)
            else:
                print("No cars left to defend! Game Over.")
                game_running = False

            if stolen_cars_count >= len(CARS):
                print("\nAll your vehicles have been lost. The city's criminal underworld has claimed victory.")
                game_running = False
            elif player_reputation < -50:  # Example of a fail state
                print("\nYour reputation is in tatters. No one trusts you to defend their vehicles anymore.")
                game_running = False

            # Progress to next level condition (e.g., successful defense of all cars for this round)
            if all(car["status"] == "secure" for car in
                   CARS.values()) and current_garage_level < 3:  # Example for 3 levels
                current_garage_level += 1
                player_money += 1000  # Bonus for leveling up
                print(f"\n--- GARAGE LEVEL UP! ---")
                print(f"You've proven your skills! Now at Garage Level {current_garage_level}. New challenges await!")
                print(f"Bonus: ${1000} added to your funds!")
                input("Press Enter to continue...")
                # You might unlock new defenses or cars here too

    print("\n--- GAME OVER ---")
    print("Thanks for playing Guardian Garage!")
