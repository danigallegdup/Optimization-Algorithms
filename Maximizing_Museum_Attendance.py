import random
import time

def max_attendance(groups, capacity):
    """
    1/2-approximation algorithm to maximize museum attendance.

    :param groups: List of group sizes.
    :param capacity: Maximum number of people the museum can admit.
    :return: Maximum number of people that can be admitted using the algorithm.
    """
    # Sort groups in non-decreasing order
    groups_sorted = sorted(groups)

    # Set A: Start from the smallest group and admit groups until the total exceeds capacity
    sum_A = 0
    for group in groups_sorted:
        if sum_A + group <= capacity:
            sum_A += group
        else:
            break

    # Set B: Start from the largest group and admit groups until the total exceeds capacity
    sum_B = 0
    for group in reversed(groups_sorted):
        if sum_B + group <= capacity:
            sum_B += group
        else:
            break

    # Return the maximum attendance between the two strategies
    return max(sum_A, sum_B)

def brute_force_optimal(groups, capacity):
    """
    A brute force method to find the optimal number of people that can be admitted.
    This checks all possible combinations of groups (2^m possibilities) to find the optimal solution.
    
    :param groups: List of group sizes.
    :param capacity: Maximum number of people the museum can admit.
    :return: Optimal number of people that can be admitted.
    """
    from itertools import combinations

    best_attendance = 0
    n = len(groups)

    # Iterate through all possible combinations of groups
    for i in range(n+1):
        for combination in combinations(groups, i):
            total = sum(combination)
            if total <= capacity:
                best_attendance = max(best_attendance, total)

    return best_attendance

def demo_algorithm(groups, capacity):
    """
    Demonstrates the 1/2-approximation algorithm and compares it to the optimal solution.
    Prints the results.

    :param groups: List of group sizes.
    :param capacity: Maximum number of people the museum can admit.
    """
    # Run the algorithm and get the approximate solution
    start = time.time()
    approx_attendance = max_attendance(groups, capacity)
    end = time.time()
    algorithm_time = end - start

    # Run the brute force optimal solution for comparison
    start = time.time()
    optimal_attendance = brute_force_optimal(groups, capacity)
    end = time.time()
    brute_force_time = end - start

    # Display results
    print(f"Groups: {groups}")
    print(f"Capacity: {capacity}")
    print(f"Algorithm Approximate Attendance: {approx_attendance}")
    print(f"Optimal Attendance (Brute Force): {optimal_attendance}")
    print(f"Algorithm guarantees at least {approx_attendance / optimal_attendance * 100:.2f}% of the optimal solution")
    print(f"Algorithm Time: {algorithm_time:.6f} seconds")
    print(f"Brute Force Time: {brute_force_time:.6f} seconds")
    print("----------------------------------------------------")

# Example usage
if __name__ == "__main__":
    # Generate random test case
    num_groups = 10
    max_group_size = 50
    groups = [random.randint(1, max_group_size) for _ in range(num_groups)]
    capacity = random.randint(50, 150)

    # Run the demonstration
    demo_algorithm(groups, capacity)
