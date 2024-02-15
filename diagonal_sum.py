def get_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    current_val = 1

    for i in range(n):
        row = i
        col = 0
        while row >= 0:
            matrix[row][col] = current_val
            current_val += 1
            row -= 1
            col += 1

    for i in range(1, n):
        row = n - 1
        col = i
        while col < n:
            matrix[row][col] = current_val
            current_val += 1
            row -= 1
            col += 1

    return matrix


def find_sum(n,d):

    matrix = get_matrix(n)

    d -= 1

    diag = [0,d]
    diag_sum=0

    for i in range(n):

        for j in range(n):

            if [i,j] == diag:
                diag_sum+=matrix[i][j]

        diag[0]+=1
        diag[1]-=1

        if diag[0]<diag[1]:
            break

    print(diag_sum)


# Example usage:
n = 4

d = 2

find_sum(n,d)