# Lab 00: Python Fundamentals Refresher

Welcome to lab zero! As we bridge into algorithm design, this lab is meant to help you dust off your Python skills. 

These problems are deliberately open-ended. You have the flexibility to design the specific logic, but you must correctly utilize the required language features. Be sure to write some test cases to ensure your code is working as intended.

**Instructions**: clone this repo and create a file `lab00.py` containing the functions below. You may work in groups of up to 3, but everyone should submit their own lab. Push your work back to your repo and submit the link to your repo in this [Google form](https://forms.gle/8bSUEc4Qc3LAruyy7).

---

## Part 1: Nested `for` Loops and 2D Lists
**The Scenario:** You need to process a 2D grid of raw sensor readings, flattening the data into a single sequence while filtering out noise.

**Your Task:** Write a function `flatten_and_filter(matrix)` that takes a list of lists containing integers.
1. Use nested `for` loops to iterate through each row, and each item within that row.
2. Filter the items to keep only even `int` elements. 
3. Cube each of these filtered elements (e.g., `x ** 3`).
4. Append the results to a single 1D list and return it.

---

## Part 2: State Tracking with `while` Loops
**The Scenario:** You need to calculate the number of steps required for a starting integer to resolve to 1 under the rules of the Collatz conjecture.

**Your Task:** Write a function `collatz_steps(n)` that uses a `while` loop.
1. Define a loop that continues as long as `n > 1`.
2. Inside the loop, if `n` is even, divide it by 2 (using integer division `//`).
3. If `n` is odd, multiply it by 3 and add 1.
4. Keep track of how many total steps (iterations) it takes to reach 1, and return that count.

---

## Part 3: Mapping Data with Dictionaries
**The Scenario:** You are analyzing a string of genetic data and need to determine the frequency of each nucleotide.

**Your Task:** Write a function `nucleotide_count(sequence)`.
1. Accept a string representing a sequence (e.g., `"GATTACA"`).
2. Iterate through the string and populate a dictionary counting the occurrences of each character.
3. Ensure your code safely handles the first time it encounters a character without throwing a `KeyError` (you may use `.get()` or a manual `if/else` check).
4. Return the resulting dictionary.

---

## Part 4: Intersections and `set` Logic
**The Scenario:** You have two separate lists of student IDs representing rosters for CS 202 and CS 303, and you need to find the enrollment overlaps and differences.

**Your Task:** Write a function `compare_enrollments(roster_a, roster_b)`.
1. Convert the two input lists into Python `set` objects.
2. Using built-in set operations, return a new dictionary containing:
   - `"both"`: IDs present in both rosters.
   - `"only_a"`: IDs exclusively in roster A.
   - `"only_b"`: IDs exclusively in roster B.
   - `"all_unique"`: A combined set of every unique ID across both rosters.
  
---

## Lab Assessment

1. As you wrote this Python code, which concept felt the most unfamiliar?

The most unfamiliar part for me was working with nested loops in Part 1. I don’t use 2D lists very often, so looping through each row and then each value made me slow down a bit. Once I got the pattern, it made sense.

3. Did you encounter any technical issues during this lab?

The only small issue I ran into was in Part 3. At first, I tried increasing the dictionary count without checking if the key existed, which caused an error. Using .get() fixed it right away. Everything else worked fine.

5. Looking back at Part 2, how did you logically verify that your `while` loop would not result in an infinite loop?

I checked how the Collatz rules behave. Even numbers always get smaller because they’re divided by 2, and odd numbers eventually turn into even numbers after the 3n + 1 step. Since the value keeps moving toward smaller numbers, it will eventually reach 1. I also tested a few inputs to make sure the loop always finished.
