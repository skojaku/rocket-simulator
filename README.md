# 🚀 Rocket Simulator - Git Debugging Exercise

## The Problem

Welcome, Space Engineer! This rocket fuel calculator has **TWO bugs** in the current version:

1. **Bug #1**: The rocket ASCII art is misaligned
2. **Bug #2**: The fuel calculations are completely wrong - fuel keeps increasing!

Your mission: Use Git to find which commits introduced these bugs and fix them.

## Getting Started

```bash
git clone https://github.com/skojaku/rocket-simulator.git
cd rocket-simulator
python3 rocket_game.py
```

**What you'll notice:**
- The rocket looks weird/misaligned
- Fuel starts at 100 units but **increases** to 140 instead of decreasing!

## Your Mission

### Part 1: Fix the ASCII Art Bug

The rocket's body is misaligned in the current version.

**Tasks:**
1. Look at the rocket when you run the game - see the problem?
2. Use `git log --oneline` to see all commits
3. Find which commit broke the ASCII art (Hint: look for "Update rocket design")
4. Find the commit BEFORE the break where it was correct (Hint: "Add rocket ASCII art")
5. **Time travel to the working version:**
   ```bash
   git checkout <commit-hash-before-break>
   cat rocket_game.py  # Look at the draw_rocket() function
   ```
6. **Copy the correct ASCII art** from the `draw_rocket()` function
7. **Return to the present:**
   ```bash
   git checkout main
   ```
8. Open `rocket_game.py` and **paste the correct ASCII art** into `draw_rocket()`
9. Test that the rocket looks correct: `python3 rocket_game.py`
10. Stage and commit your fix:
    ```bash
    git add rocket_game.py
    git commit -m "Fix rocket ASCII art alignment"
    ```

**This teaches you:** How to use Git as a time machine to recover correct code!

### Part 2: Fix the Math Bug

The fuel calculation functions are broken.

**Tasks:**
1. Find which commit broke the fuel calculations (Hint: "Refactor fuel...")
2. Use `git show <commit-hash>` to see what changed
3. Fix the two functions in `rocket_game.py`:
   - `calculate_fuel_cost()` - Line 16 (should multiply, not add)
   - `calculate_remaining_fuel()` - Line 21 (should subtract, not add)
4. Test your fix - fuel should decrease from 100 to 70
5. Commit your fix: `git commit -m "Fix fuel calculation operators"`

## Expected Behavior

When both bugs are fixed:
- **Rocket:** Should be properly aligned
- **Starting fuel:** 100 units
- **Fuel rate:** 3 units per step
- **Maximum altitude:** 10 steps
- **Final fuel:** 100 - (10 × 3) = **70 units remaining**

---

## Git Cheatsheet

### Viewing History

```bash
# View all commits (most recent first)
git log

# View commits in one line each (easier to scan)
git log --oneline

# View commits with a visual graph
git log --oneline --graph --all

# View commits that changed a specific file
git log --oneline rocket_game.py
```

### Inspecting Commits

```bash
# See what changed in a specific commit
git show <commit-hash>
git show 7fbc52c

# See only the diff for a specific file
git show <commit-hash> rocket_game.py

# Compare two commits
git diff <old-commit> <new-commit>
git diff a8f01cb 7fbc52c

# Compare a file between two commits
git diff <old-commit> <new-commit> rocket_game.py
```

### Finding Who Changed What

```bash
# See line-by-line history of a file
git blame rocket_game.py

# See blame for specific line range (e.g., the draw_rocket function)
git blame -L 10,25 rocket_game.py
```

### Searching History

```bash
# Find commits that mention "fuel"
git log --grep="fuel"

# Find commits where specific code was changed
git log -S "distance * fuel_rate"

# Find when a pattern was added or removed
git log -G "distance.*fuel_rate"
```

### Time Travel to Old Commits

```bash
# Go back to an old commit (read-only mode)
git checkout <commit-hash>

# View a file at that old commit
cat rocket_game.py
less rocket_game.py

# IMPORTANT: Return to the present (latest version)
git checkout main

# Alternative: View old file without leaving current commit
git show <commit-hash>:rocket_game.py
```

### Comparing Current vs. Past

```bash
# See all changes since a specific commit
git diff <commit-hash> HEAD

# See what changed in just one file since a commit
git diff <commit-hash> HEAD rocket_game.py

# See changes in your working directory (not yet committed)
git diff
```

### Useful Workflow Commands

```bash
# Check what you've changed
git status
git diff

# Stage your changes
git add rocket_game.py

# Commit your fix
git commit -m "Your commit message"

# See your recent commits
git log --oneline -5
```

---

## Tips for Finding the Bugs

1. **Start with `git log --oneline`** to get an overview of all changes
2. **Look for suspicious commit messages** like "refactor" or "update design"
3. **Use `git show <commit>`** to see exactly what each commit changed
4. **ASCII art bug:** Was introduced early in history (commits 2-3)
5. **Math bug:** Was introduced near the end (commit 7)
6. **Compare with previous commits** using `git diff` to see what was working before

## Learning Goals

- Navigate commit history with `git log`
- Inspect specific commits with `git show`
- Compare versions with `git diff`
- Use `git blame` to track line-by-line changes
- Understand how bugs can be introduced through seemingly innocent changes
- Practice reading commit messages critically
- Debug using Git as a time-travel tool

Good luck, Space Engineer! 🛠️

**Stuck?** Check the `answer` branch for a complete solution:
```bash
git checkout answer
cat ANSWER.md
```
