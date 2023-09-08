N = int(input())
L = [int(i) for i in input().split()]
K = int(input())
# Sort the list of distances
sorted_list = sorted(L)

# Find the index of Aman's favorite planet in the sorted list
favorite_index = sorted_list.index(L[K - 1])

# Add 1 to the index to get the position (1-based)
favorite_position = favorite_index + 1

print(favorite_position)
