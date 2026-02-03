# 🚀 Rocket Simulator - Git Debugging Exercise

## The Mission

Welcome, Space Engineer! Our rocket fuel calculator worked perfectly at one point, but now it has two critical bugs. The rocket looks misaligned when it launches, and somehow the fuel keeps increasing instead of decreasing. Your mission is to use Git as a time machine to find when these bugs were introduced and fix them.

## Getting Started

```bash
git clone https://github.com/skojaku/rocket-simulator.git
cd rocket-simulator
python3 rocket_game.py
```

You'll immediately see both problems: the rocket body doesn't line up correctly, and the fuel goes from 100 units up to 140 units. A rocket that gains fuel as it flies? That's not how physics works!

---

## Part 1: Fix the Misaligned Rocket

The rocket's ASCII art is broken. Some lines stick out too far to the right. Your goal is to travel back in Git history to find when the rocket looked correct, copy that working version, and bring it forward to fix the current code.

### Steps

1. Use `git log --oneline` to view the commit history
2. Find the commit that says "Update rocket design" (this broke it)
3. Find the commit just before that: "Add rocket ASCII art" (this was correct)
4. Time travel to the working version:
   ```bash
   git checkout <commit-hash-of-working-version>
   ```
5. View the file and copy the correct `draw_rocket()` function:
   ```bash
   cat rocket_game.py
   ```
6. Return to the present:
   ```bash
   git checkout main
   ```
7. Open `rocket_game.py` in your editor and paste the correct ASCII art
8. Test it: `python3 rocket_game.py`
9. Commit your fix:
   ```bash
   git add rocket_game.py
   git commit -m "Fix rocket ASCII art alignment"
   ```

**What you're learning:** Git lets you checkout old commits to see exactly how the code looked in the past. This is like having a time machine for your codebase.

---

## Part 2: Fix the Fuel Calculations

The math is completely wrong. The fuel calculation functions use addition when they should use multiplication and subtraction. You'll use Git to find when this happened and what the correct operators should be.

### Steps

1. Use `git log --oneline` to find the suspicious commit
2. Look for "Refactor fuel calculation functions" (the word "refactor" often hides bugs!)
3. See what changed in that commit:
   ```bash
   git show <commit-hash>
   ```
4. Time travel to the commit just before the break to see the correct code:
   ```bash
   git checkout <previous-commit-hash>
   ```
5. Look at the `calculate_fuel_cost()` and `calculate_remaining_fuel()` functions
6. Note the correct operators: `*` for multiplication and `-` for subtraction
7. Return to the present:
   ```bash
   git checkout main
   ```
8. Fix the two functions in `rocket_game.py` (around lines 14-21)
9. Test it: `python3 rocket_game.py` (fuel should decrease from 100 to 70)
10. Commit your fix:
    ```bash
    git add rocket_game.py
    git commit -m "Fix fuel calculation operators"
    ```

**What you're learning:** Seemingly innocent "refactoring" can introduce bugs. Git history helps you spot exactly what changed.

---

## Expected Results

When both bugs are fixed, your rocket should launch cleanly with aligned ASCII art, and the fuel should decrease from 100 units at the start down to 70 units after traveling 10 steps (using 3 units per step).

---

## Essential Git Commands

Here are the key commands you'll use:

**Viewing history:**
```bash
git log --oneline              # See all commits, one per line
git show <commit-hash>         # See what changed in a specific commit
```

**Time travel:**
```bash
git checkout <commit-hash>     # Go back to an old commit (read-only)
git checkout main              # Return to the present
```

**Making changes:**
```bash
git diff                       # See what you changed
git add <file>                 # Stage your changes
git commit -m "message"        # Commit your fix
```

**Advanced techniques:**
```bash
git log --grep="fuel"          # Find commits mentioning "fuel"
git log -S "distance * fuel"   # Find when specific code changed
git diff <old> <new>           # Compare two commits
git blame <file>               # See who changed each line
```

---

## Tips

When you use `git checkout <commit-hash>`, you'll see a message about "detached HEAD state." Don't worry! This just means you're in read-only mode, viewing an old version. You can look around, copy code, but you're not changing anything. Just use `git checkout main` to return to the present.

The ASCII art bug happened early in the history (commits 2-3), while the math bug was introduced much later (commit 7). Both were introduced by commits with innocent-sounding messages.

---

## Need Help?

If you get stuck, check the `answer` branch for a complete step-by-step solution:

```bash
git checkout answer
cat ANSWER.md
```

Good luck, Space Engineer! 🛠️
