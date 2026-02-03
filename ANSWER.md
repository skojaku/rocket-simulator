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
be42526 Add README with debugging instructions
1726ed9 Refactor fuel calculation functions for better readability
4d4f218 Improve documentation
4ff531b Add fuel calculation system
99ee287 Add animation: rocket moves upward
7fbc52c Update rocket design              <-- This broke it!
a8f01cb Add rocket ASCII art               <-- This was correct
0692d4b Initial commit: basic game structure
```

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

### Step 4: Compare with Working Version

Look at the previous commit to see the correct spacing:

```bash
git show a8f01cb:rocket_game.py | grep -A 9 "def draw_rocket"
```

### Step 5: Fix the Bug

Edit `rocket_game.py`, function `draw_rocket()` (around line 29):

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

### Step 6: Test and Commit

```bash
python3 rocket_game.py  # Rocket should look aligned now
git add rocket_game.py
git commit -m "Fix rocket ASCII art alignment"
```

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

### Step 4: Understand the Impact

**Math breakdown:**

**Correct (before bug):**
- Step 1: Fuel cost = 1 × 3 = 3 units
- Remaining = 100 - 3 = 97 units
- Step 2: Cost = 1 × 3 = 3, Remaining = 97 - 3 = 94
- ...
- Step 10: Remaining = 100 - (10 × 3) = 70 units ✓

**Broken (current):**
- Step 1: Fuel cost = 1 + 3 = 4 units (wrong!)
- Remaining = 100 + 4 = 104 units (fuel increases!!)
- Step 2: Cost = 1 + 3 = 4, Remaining = 104 + 4 = 108
- ...
- Step 10: Remaining = 140 units ✗

### Step 5: Compare with Working Version

See the correct version:

```bash
git show 4ff531b:rocket_game.py | grep -A 3 "def calculate"
```

### Step 6: Fix the Bug

Edit `rocket_game.py`, lines 14-21:

**Before (Broken):**
```python
def calculate_fuel_cost(distance, fuel_rate):
    """Calculate fuel needed for a given distance."""
    return distance + fuel_rate    # WRONG


def calculate_remaining_fuel(current_fuel, fuel_used):
    """Calculate remaining fuel after consumption."""
    return current_fuel + fuel_used    # WRONG
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

```bash
python3 rocket_game.py  # Fuel should go from 100 → 70
git add rocket_game.py
git commit -m "Fix fuel calculation operators: use * and -"
```

---

## Summary of Both Bugs

### Bug #1: ASCII Art
- **Location:** Commit `7fbc52c` ("Update rocket design")
- **Problem:** Lines 32 and 35 in `draw_rocket()` have wrong spacing
- **Fix:** Change 6 spaces to 3 spaces (line 32), and 5 spaces to 2 spaces (line 35)

### Bug #2: Math Functions
- **Location:** Commit `1726ed9` ("Refactor fuel...")
- **Problem:** Wrong operators in lines 16 and 21
- **Fix:**
  - Line 16: Change `+` to `*`
  - Line 21: Change `+` to `-`

---

## Key Git Commands Used

```bash
# 1. View commit history
git log --oneline

# 2. See what changed in a specific commit
git show 7fbc52c
git show 1726ed9

# 3. View a file from a specific commit
git show a8f01cb:rocket_game.py

# 4. Compare two commits
git diff a8f01cb 7fbc52c

# 5. See line-by-line history
git blame rocket_game.py
git blame -L 14,21 rocket_game.py

# 6. Search for commits by message
git log --grep="design"
git log --grep="fuel"

# 7. Find when code changed
git log -S "distance * fuel_rate"
```

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

## Learning Takeaways

1. **Commit messages can be misleading:** "Refactor" and "Update design" hid bugs
2. **Small changes matter:** Even spacing in ASCII art affects display
3. **Operators are critical:** `+` vs `*` and `-` completely change logic
4. **Git is a time machine:** Always look at history when debugging
5. **Compare commits:** `git show` and `git diff` reveal what broke
6. **Test after changes:** Both commits should have been tested before committing

---

## Bonus Challenge: Prevent Future Bugs

Add tests to catch these bugs automatically!

Create `test_rocket.py`:

```python
from rocket_game import calculate_fuel_cost, calculate_remaining_fuel

def test_fuel_cost():
    assert calculate_fuel_cost(1, 3) == 3, "Fuel cost should multiply distance by rate"
    assert calculate_fuel_cost(5, 2) == 10, "5 * 2 should equal 10"

def test_remaining_fuel():
    assert calculate_remaining_fuel(100, 3) == 97, "Should subtract fuel used"
    assert calculate_remaining_fuel(50, 10) == 40, "50 - 10 should equal 40"

def test_mission():
    """Test a full mission"""
    fuel = 100
    for _ in range(10):
        fuel_used = calculate_fuel_cost(1, 3)
        fuel = calculate_remaining_fuel(fuel, fuel_used)
    assert fuel == 70, "After 10 steps, should have 70 units left"

if __name__ == "__main__":
    test_fuel_cost()
    test_remaining_fuel()
    test_mission()
    print("✅ All tests passed!")
```

Run tests:
```bash
python3 test_rocket.py
```

Now if someone breaks the math again, the tests will catch it!

---

**Congratulations, Space Engineer! You've successfully debugged both bugs!** 🎉🚀

You've learned:
- How to use Git to find bugs in history
- How to compare code across commits
- How small changes can break functionality
- The importance of testing after "refactoring"
