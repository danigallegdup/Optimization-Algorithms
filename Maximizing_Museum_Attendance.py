import time
from itertools import combinations

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
    best_attendance = 0
    n = len(groups)

    # Iterate through all possible combinations of groups
    for i in range(n+1):
        for combination in combinations(groups, i):
            total = sum(combination)
            if total <= capacity:
                best_attendance = max(best_attendance, total)

    return best_attendance

def demo_algorithm(groups, capacity, log_file, test_number):
    """
    Demonstrates the 1/2-approximation algorithm and compares it to the optimal solution.
    Logs the results to a file.

    :param groups: List of group sizes.
    :param capacity: Maximum number of people the museum can admit.
    :param log_file: The file to write the results to.
    :param test_number: The test case number for labeling results.
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

    # Log results to file
    with open(log_file, "a") as f:
        f.write(f"Test {test_number} Results:\n")
        f.write(f"Groups: {groups}\n")
        f.write(f"Capacity: {capacity}\n")
        f.write(f"Algorithm Approximate Attendance: {approx_attendance} people\n")
        f.write(f"Optimal Attendance (Brute Force): {optimal_attendance} people\n")
        if optimal_attendance == approx_attendance:
            f.write(f"both algorthmns found the same {approx_attendance }\n")
        else:
            f.write(f"Algorithm guarantees at least {approx_attendance / optimal_attendance * 100:.2f}% of the optimal solution\n")
        f.write(f"Algorithm Time: {algorithm_time:.6f} seconds\n")
        f.write(f"Brute Force Time: {brute_force_time:.6f} seconds\n")
        f.write("----------------------------------------------------\n")

def run_tests(log_file, num_tests=5):
    """
    Runs multiple tests and logs the results.

    :param log_file: The file to write the results to.
    :param num_tests: Number of tests to run.
    """
    test_cases = [
        ([15, 30, 35, 50, 55], 65),  # Test Case 1
        ([5, 10, 20, 50, 55], 60),   # Test Case 2
        ([5, 10, 15, 25, 30], 50),   # Test Case 3
        ([10, 20, 25, 30, 40, 50], 70),  # Test Case 4
        ([15, 35, 45, 55, 65], 70)   # Test Case 5
    ]

    # Run the specified test cases
    for test_num, (groups, capacity) in enumerate(test_cases, 1):
        demo_algorithm(groups, capacity, log_file, test_num)

# Example usage
if __name__ == "__main__":
    # Define the log file
    log_file = "results.txt"

    # Clear the log file at the start of the test
    with open(log_file, "w") as f:
        f.write("Museum Attendance Algorithm Results\n")
        f.write("==================================\n")

    # Run tests and log the results
    run_tests(log_file)

    print(f"Results have been logged to {log_file}")
