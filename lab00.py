# Part 1: Nested for Loops and 2D Lists
def flatten_and_filter(matrix):
    result = []
    for row in matrix:
        for value in row:
            if value % 2 == 0:
                result.append(value ** 3)
    return result


# Part 2: State Tracking with while Loops
def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


# Part 3: Mapping Data with Dictionaries
def nucleotide_count(sequence):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Part 4: Intersections and set Logic
def compare_enrollments(roster_a, roster_b):
    set_a = set(roster_a)
    set_b = set(roster_b)

    return {
        "both": set_a & set_b,
        "only_a": set_a - set_b,
        "only_b": set_b - set_a,
        "all_unique": set_a | set_b
    }
