def findp(N,S):
    permutation = list(range(1, N + 1))
    result = []

    for direction in S:
        if direction == 'I':
            result.append(permutation.pop(0))  # Append the smallest available number
        elif direction == 'D':
            result.append(permutation.pop())  # Append the largest available number

    result.append(permutation.pop())  # Add the last remaining number
    
    return result

# Example usage:
# N = 6
# S = "IIIDI"
# print(findp(N, S)) 

def smallest_lexicographic_permutation(N, S):
    min_num = 1  # The smallest available number
    max_num = N  # The largest available number
    result = []

    for direction in S:
        if direction == 'I':
            result.append(min_num)  # Append the smallest available number
            min_num += 1
        elif direction == 'D':
            result.append(max_num)  # Append the largest available number
            max_num -= 1

    # Add the last remaining number
    result.append(min_num)

    return result

# Example usage:
N = 6
S = "IIIDI"
print(smallest_lexicographic_permutation(N, S))  # Output: [1, 2, 3, 4, 3, 4]
