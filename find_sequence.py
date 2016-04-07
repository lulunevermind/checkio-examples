def checkio(matrix):

    def n_in_row(l):
        stack = 0
        prev = None
        for el in l:
            if el == prev:
                stack += 1
            else:
                stack = 0
            prev = el
            if stack >= 3:
                return True
        return False

    for row in matrix:
        if n_in_row(row):
            return True

    for col in zip(*matrix):
        if n_in_row(col):
            return True

    def diags_matrix(matrix):
        return [[matrix[y-x][x] for x in range(len(matrix)) if 0 <= y-x < len(matrix)] for y in range(2*len(matrix)-1)]

    def flip_matrix_90(matrix):
        return list(zip(*matrix[::-1]))

    diags1 = diags_matrix(matrix)
    for row in diags1:
        if n_in_row(row):
            return True
    diags2 = diags_matrix(flip_matrix_90(matrix))
    for row in diags2:
        if n_in_row(row):
            return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    # result = checkio([
    #     [7, 7, 7, 2, 1, 1],
    #     [1, 1, 7, 3, 1, 5],
    #     [2, 3, 1, 2, 5, 1],
    #     [1, 1, 1, 5, 1, 4],
    #     [4, 6, 5, 1, 3, 1],
    #     [1, 1, 9, 1, 2, 1]
    # ])
    # print('RESULT -->> %s' % result)
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
