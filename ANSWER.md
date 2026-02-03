# 🚀 Rocket Simulator - Complete Solution

This document contains the step-by-step solution to **BOTH bugs** in the rocket simulator. **Don't peek unless you're really stuck!**

---

## Bug #1: ASCII Art Misalignment (Current Bug)

### Step 1: Identify the Problem

Run the game and look at the rocket:

```bash
python3 rocket_game.py
```

You'll see the rocket body is misaligned - some parts stick out too far to the right.

### Step 2: Find When It Broke

```bash
git log --oneline
```

You'll see:
```
7e7fca1 Update instructions: add time travel workflow for fixing ASCII art
be42526 Add README with debugging instructions
1726ed9 Refactor fuel calculation functions for better readability
4d4f218 Improve documentation
4ff531b Add fuel calculation system
99ee287 Add animation: rocket moves upward
7fbc52c Update rocket design              <-- This broke it!
a8f01cb Add rocket ASCII art               <-- This was correct! ✓
0692d4b Initial commit: basic game structure
```

**Key insight:** The ASCII art was correct in commit `a8f01cb`, then broken in `7fbc52c`.

### Step 3: Examine What Changed

Compare the correct version with the broken one:

```bash
git show 7fbc52c
```

You'll see:
```diff
def draw_rocket():
    """Draw the rocket."""
    rocket = """    /\\
-   /  \\          # Line 2: REMOVED 2 spaces at start
+      /  \\       # Line 2: ADDED too many spaces (3 extra)
  |    |
  | 🚀 |
-  |    |          # Line 5: REMOVED 2 spaces at start
+     |    |       # Line 5: ADDED too many spaces (3 extra)
 /|    |\\
```

**The Problem:** Lines 2 and 5 have wrong indentation.

### Step 4: Time Travel to Get the Correct Code ⏰

Now use Git as a time machine to go back and get the working version!

**Go back to the working commit:**
```bash
git checkout a8f01cb
```

You'll see a message like:
```
Note: switching to 'a8f01cb'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.
```

**Don't worry!** This is normal. You're just visiting the past in read-only mode.

**View the correct file:**
```bash
cat rocket_game.py
```

Or use `less`:
```bash
less rocket_game.py
# Press 'q' to quit
```

Find the `draw_rocket()` function and **copy the correct rocket ASCII art**:

```python
def draw_rocket():
    """Draw the rocket."""
    rocket = """    /\
   /  \
  |    |
  | 🚀 |
  |    |
 /|    |\
/ |____| \
 💨💨💨💨💨"""
    return rocket
```

**Pro tip:** You can also copy directly from your terminal or save it to a temporary file:
```bash
# Extract just the draw_rocket function
sed -n '/def draw_rocket/,/return rocket/p' rocket_game.py
```

### Step 5: Return to the Present

**Come back to the latest version:**
```bash
git checkout main
```

You'll see:
```
Previous HEAD position was a8f01cb Add rocket ASCII art
Switched to branch 'main'
```

You're back! The file `rocket_game.py` now shows the current (broken) version again.

### Step 6: Paste and Fix

Open `rocket_game.py` in your editor:
```bash
# Use your favorite editor
nano rocket_game.py
# or
code rocket_game.py
# or
vim rocket_game.py
```

Find the `draw_rocket()` function (around line 29) and **replace the broken ASCII art** with the correct one you copied:

**Before (Broken):**
```python
def draw_rocket():
    """Draw the rocket."""
    rocket = """    /\\
      /  \\           # WRONG: too many spaces
  |    |
  | 🚀 |
     |    |          # WRONG: too many spaces
 /|    |\\
/ |____| \\
 💨💨💨💨💨"""
    return rocket
```

**After (Fixed):**
```python
def draw_rocket():
    """Draw the rocket."""
    rocket = """    /\\
   /  \\             # CORRECT: 3 spaces
  |    |
  | 🚀 |
  |    |            # CORRECT: 2 spaces
 /|    |\\
/ |____| \\
 💨💨💨💨💨"""
    return rocket
```

### Step 7: Test and Commit

Test that it works:
```bash
python3 rocket_game.py
# Rocket should look properly aligned now!
```

Stage and commit your fix:
```bash
git add rocket_game.py
git commit -m "Fix rocket ASCII art alignment by copying from commit a8f01cb"
```

**What you learned:** How to use `git checkout <commit>` to time-travel and recover correct code!

---

## Bug #2: Math Functions (Current Bug)

### Step 1: Observe the Bug

Run the game and watch the fuel:

```bash
python3 rocket_game.py
```

**Problem:** Fuel starts at 100 and increases to 140! Should decrease to 70.

### Step 2: Find the Breaking Commit

```bash
git log --oneline
```

Look for suspicious commit:
```
1726ed9 Refactor fuel calculation functions for better readability  <-- Suspicious!
```

The word "refactor" often hides bugs. Let's investigate!

### Step 3: Examine What Changed

```bash
git show 1726ed9
```

You'll see:
```diff
def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
-   return distance * fuel_rate    # CORRECT: multiply
+   return distance + fuel_rate    # WRONG: addition!

def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
-   return current_fuel - fuel_used    # CORRECT: subtract
+   return current_fuel + fuel_used    # WRONG: addition!
```

**The Problem:**
- Changed `*` (multiply) to `+` (add)
- Changed `-` (subtract) to `+` (add)

### Step 4: Time Travel to See the Correct Code ⏰

**Go back to before the bug (one commit before):**
```bash
git checkout 4ff531b
# Or use: git checkout 1726ed9~1
```

**View the correct functions:**
```bash
grep -A 2 "def calculate" rocket_game.py
```

You'll see:
```python
def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
    return distance * fuel_rate
--
def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
    return current_fuel - fuel_used
```

**Note the correct operators:** `*` and `-`

### Step 5: Return to Present

```bash
git checkout main
```

### Step 6: Fix the Math

Open `rocket_game.py` and fix lines 14-21:

**Before (Broken):**
```python
def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
    return distance + fuel_rate    # WRONG: should be *


def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
    return current_fuel + fuel_used    # WRONG: should be -
```

**After (Fixed):**
```python
def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
    return distance * fuel_rate    # CORRECT: Multiply


def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
    return current_fuel - fuel_used    # CORRECT: Subtract
```

### Step 7: Test and Commit

Test:
```bash
python3 rocket_game.py
# Fuel should go from 100 → 70 now!
```

Commit:
```bash
git add rocket_game.py
git commit -m "Fix fuel calculation operators: change + to * and -"
```

---

## Summary of Time Travel Workflow

### The Pattern You Learned:

1. **Find the bug** in current code
2. **Use `git log`** to find when it broke
3. **Identify the commit before the break** (the working version)
4. **Time travel back:** `git checkout <good-commit>`
5. **Copy the correct code** from the old version
6. **Return to present:** `git checkout main`
7. **Paste the fix** into current code
8. **Test and commit**

### Key Commands:

```bash
# Step back in time
git checkout <commit-hash>

# Look around
cat file.py
less file.py

# Come back to present
git checkout main

# Alternative: View old file without moving
git show <commit-hash>:file.py
```

---

## Summary of Both Bugs

### Bug #1: ASCII Art
- **Location:** Commit `7fbc52c` ("Update rocket design")
- **Working version:** Commit `a8f01cb`
- **Problem:** Lines 32 and 35 in `draw_rocket()` have wrong spacing
- **Fix:** Time traveled to `a8f01cb`, copied correct ASCII art, pasted it back

### Bug #2: Math Functions
- **Location:** Commit `1726ed9` ("Refactor fuel...")
- **Working version:** Commit `4ff531b` (or `1726ed9~1`)
- **Problem:** Wrong operators in lines 16 and 21
- **Fix:**
  - Line 16: Change `+` to `*`
  - Line 21: Change `+` to `-`

---

## Final Expected Output

After fixing both bugs:

```
🚀 SPACE ROCKET FUEL CALCULATOR 🚀

Your rocket is launching!

    /\       ← Aligned correctly
   /  \
  |    |
  | 🚀 |
  |    |     ← Aligned correctly
 /|    |\
/ |____| \
 💨💨💨💨💨

========================================
Altitude: 10/10
Fuel used: 3 units
Remaining fuel: 70 units      ← Decreased correctly!
========================================

🎉 Mission complete!
Final fuel: 70 units
```

---

## Key Git Commands You Mastered

```bash
# 1. View commit history
git log --oneline

# 2. See what changed in a specific commit
git show <commit-hash>

# 3. TIME TRAVEL: Go back to an old commit
git checkout <commit-hash>

# 4. Return to the present
git checkout main

# 5. View old file without moving (alternative)
git show <commit-hash>:filename

# 6. Compare two commits
git diff <old-commit> <new-commit>

# 7. Find when code changed
git log -S "distance * fuel_rate"

# 8. See line-by-line history
git blame filename
```

---

## Learning Takeaways

1. **Git is a time machine:** You can always go back and see how code used to work
2. **Detached HEAD is safe:** It's just read-only mode for viewing history
3. **Copy from the past:** When you find working code in history, you can bring it forward
4. **Commit messages can mislead:** "Refactor" and "Update" can hide bugs
5. **Small changes matter:** Even spacing breaks ASCII art; wrong operators break logic
6. **Always test after "refactoring":** Both bugs should have been caught with testing

---

## Bonus: Prevent Future Bugs

Add tests to catch bugs automatically!

Create `test_rocket.py`:

```python
from rocket_game import calculate_fuel_cost, calculate_remaining_fuel

def test_fuel_cost():
    assert calculate_fuel_cost(1, 3) == 3, "Fuel cost should multiply"
    assert calculate_fuel_cost(5, 2) == 10, "5 * 2 = 10"

def test_remaining_fuel():
    assert calculate_remaining_fuel(100, 3) == 97, "Should subtract"
    assert calculate_remaining_fuel(50, 10) == 40, "50 - 10 = 40"

def test_full_mission():
    """Test a complete 10-step mission"""
    fuel = 100
    for _ in range(10):
        fuel_used = calculate_fuel_cost(1, 3)
        fuel = calculate_remaining_fuel(fuel, fuel_used)
    assert fuel == 70, f"Expected 70 units remaining, got {fuel}"

if __name__ == "__main__":
    test_fuel_cost()
    test_remaining_fuel()
    test_full_mission()
    print("✅ All tests passed!")
```

Run tests:
```bash
python3 test_rocket.py
```

---

**Congratulations, Space Engineer!** 🎉🚀

You've mastered:
- ✓ Using Git to find bugs in history
- ✓ Time traveling to old commits
- ✓ Recovering correct code from the past
- ✓ Understanding how bugs get introduced
- ✓ The importance of testing after changes
