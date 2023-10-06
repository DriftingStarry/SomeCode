import math

def calculate_possibilities(N, M):
    # Calculate the number of different possibilities
    possibilities = math.comb(N + M - 1, N - 1)
    return possibilities

# Example usage
N = 5  # Number of oases
M =10  # Number of deserts

possibilities = calculate_possibilities(N, M)
print(f"The number of different possibilities is: {possibilities}")
