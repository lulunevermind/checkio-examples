#https://checkio.org/mission/matrix-pattern/solve/


def checkio(pattern, image):

    def explore(arr, combination, i, j):
        """
        for each column in the combination we have to find
        compare it with what is present in the map (arr)
        """
        for row in combination:
            for count, item in enumerate(row):

                # compare the map with the combination value we're up to
                # if it doesn;t match, return False and stop
                if arr[i + count][j] != item:
                    return False
            j += 1
        return True

    def find_combination_in_arr(arr, combination, ):
        for i, row in enumerate(arr):
            for j, item in enumerate(row):

                # if we have found the start of the combination, then start exploring
                if item == combination[0][0]:
                    if explore(arr, combination, i, j):
                        arr[i][j] = 3 if arr[i][j] == 1 else 2
                        return arr
    print(find_combination_in_arr(image, pattern))
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]])

    # assert checkio([[1, 0], [1, 1]],
    #                [[0, 1, 0, 1, 0],
    #                 [0, 1, 1, 0, 0],
    #                 [1, 0, 1, 1, 0],
    #                 [1, 1, 0, 1, 1],
    #                 [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
    #                                       [0, 3, 3, 0, 0],
    #                                       [3, 2, 1, 3, 2],
    #                                       [3, 3, 0, 3, 3],
    #                                       [0, 1, 1, 0, 0]]
    # assert checkio([[1, 1], [1, 1]],
    #                [[1, 1, 1],
    #                 [1, 1, 1],
    #                 [1, 1, 1]]) == [[3, 3, 1],
    #                                 [3, 3, 1],
    #                                 [1, 1, 1]]
    # assert checkio([[0, 1, 0], [1, 1, 1]],
    #                [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    #                 [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #                 [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    #                 [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    #                 [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    #                 [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
    #                                                      [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
    #                                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                      [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
    #                                                      [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
    #                                                      [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
    #                                                      [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #                                                      [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
    #                                                      [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
    #                                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
