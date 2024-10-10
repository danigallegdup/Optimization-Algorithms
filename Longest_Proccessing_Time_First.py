import heapq

def lpt_3_approximation(jobs, p):
    """
    3-Approximation algorithm for minimizing the makespan using LPT (Longest Processing Time first).
    
    :param jobs: A list of job processing times.
    :param p: The number of identical processors.
    :return: The estimated makespan using the 3-approximation LPT algorithm.
    """
    # Sort the jobs in decreasing order of processing time
    jobs_sorted = sorted(jobs, reverse=True)
    
    # Initialize a min-heap to represent the processors (each element is the total load on that processor)
    processors = [0] * p
    heapq.heapify(processors)
    
    # Greedily assign each job to the processor with the least current load
    for job in jobs_sorted:
        # Get the processor with the least load (smallest element in the heap)
        min_load = heapq.heappop(processors)
        # Assign the job to this processor
        min_load += job
        # Push the updated load back into the heap
        heapq.heappush(processors, min_load)
    
    # The makespan is the maximum load on any processor (i.e., the largest element in the heap)
    return max(processors)

# Test the algorithm
def run_tests():
    """
    Runs multiple test cases for the LPT algorithm and prints the results.
    """
    test_cases = [
        # Test case 1: Jobs that fit perfectly
        {
            "jobs": [10, 10, 10, 10],
            "processors": 2,
            "expected": 20
        },
        # Test case 2: Slight imbalance between job sizes
        {
            "jobs": [5, 8, 7, 10, 12],
            "processors": 3,
            "expected": 15  # Approximately 3x optimal (which is 12)
        },
        # Test case 3: All jobs are the same size
        {
            "jobs": [5, 5, 5, 5, 5, 5],
            "processors": 3,
            "expected": 10  # Optimal
        },
        # Test case 4: One large job and many small ones
        {
            "jobs": [1, 1, 1, 1, 50],
            "processors": 3,
            "expected": 50  # No matter what, the makespan is dominated by the large job
        },
        # Test case 5: Completely random job sizes
        {
            "jobs": [3, 7, 8, 4, 2, 12, 15],
            "processors": 4,
            "expected": 20  # Approximately 3x optimal (which is around 15)
        }
    ]

    print("Running Test Cases for LPT Algorithm (3-Approximation):")
    for i, test in enumerate(test_cases):
        jobs = test["jobs"]
        processors = test["processors"]
        expected = test["expected"]
        result = lpt_3_approximation(jobs, processors)
        print(f"Test Case {i+1}:")
        print(f"Jobs: {jobs}")
        print(f"Processors: {processors}")
        print(f"Expected Makespan: {expected}")
        print(f"Computed Makespan: {result}")
        print(f"Test {'Passed' if result <= expected else 'Failed'}")
        print("-------------------------------")

# Run the test cases
if __name__ == "__main__":
    run_tests()
