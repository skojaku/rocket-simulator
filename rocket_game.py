#!/usr/bin/env python3
"""
Space Rocket Fuel Calculator Game
"""

import time
import sys
import os


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

    max_altitude = 10

    for altitude in range(max_altitude):
        clear_screen()

        # Add blank space to simulate upward movement
        print('\n' * (max_altitude - altitude - 1))
        print(draw_rocket())
        print()

        print("=" * 40)
        print(f"Altitude: {altitude + 1}/{max_altitude}")
        print("=" * 40)

        time.sleep(0.3)

    print("\n🎉 Mission complete!")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n🛑 Mission aborted.")
        sys.exit(0)
