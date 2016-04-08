def checkio(matrix):
    if any([matrix[i][i] for i in range(0, len(matrix))]) != 0:
        return False
    diags = [[matrix[y-x][x] for x in range(len(matrix)) if 0 <= y-x < len(matrix)] for y in range(2*len(matrix)-1)]
    for diag in diags:
        elements = [(diag[i], diag[-(i + 1)]) for i in range(0, len(diag))]
        if any(el[0] != -el[1] for el in elements):
            return False
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print(checkio([
    #     [0, 1, 2],
    #     [-1, 0, 1],
    #     [-2, -1, 0]]))
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
