#!/usr/bin/env python3
"""
Space Rocket Fuel Calculator Game
"""

import time
import sys


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

    print(draw_rocket())
    print()

    for i in range(10):
        print(f"Position: {i + 1}/10")
        time.sleep(0.5)

    print("\n🎉 Mission complete!")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n🛑 Mission aborted.")
        sys.exit(0)
