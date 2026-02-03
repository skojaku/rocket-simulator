#!/usr/bin/env python3
"""
Space Rocket Fuel Calculator Game

A simple educational game to practice arithmetic operations.
Watch your rocket launch and track fuel consumption!
"""

import time
import sys
import os


def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
    return distance + fuel_rate


def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
    return current_fuel + fuel_used


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name != 'nt' else 'cls')


def draw_rocket():
    """Draw the rocket."""
    rocket = """    /\\
      /  \\
  |    |
  | 🚀 |
     |    |
 /|    |\\
/ |____| \\
 💨💨💨💨💨"""
    return rocket


def play_game():
    """Main game loop."""
    print("🚀 SPACE ROCKET FUEL CALCULATOR 🚀")
    print("\nYour rocket is launching!\n")

    # Game parameters
    starting_fuel = 100
    fuel_rate = 3
    max_altitude = 10

    current_fuel = starting_fuel

    for altitude in range(max_altitude):
        clear_screen()

        # Add blank space to simulate upward movement
        print('\n' * (max_altitude - altitude - 1))
        print(draw_rocket())
        print()

        # Calculate fuel usage
        fuel_used = calculate_fuel_cost(1, fuel_rate)
        current_fuel = calculate_remaining_fuel(current_fuel, fuel_used)

        print("=" * 40)
        print(f"Altitude: {altitude + 1}/{max_altitude}")
        print(f"Fuel used: {fuel_used} units")
        print(f"Remaining fuel: {current_fuel} units")
        print("=" * 40)

        # Check if out of fuel
        if current_fuel <= 0:
            print("\n💥 Out of fuel! Mission failed!")
            return False

        time.sleep(0.3)

    print("\n🎉 Mission complete!")
    print(f"Final fuel: {current_fuel} units")
    return True


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n🛑 Mission aborted.")
        sys.exit(0)
