def flat_list(array):
    return eval('[' + str(array).replace('[', '').replace(']', '') + ']')

if __name__ == '__main__':
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], '2nd fail'
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], '3rd fail'
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], '4rd fail'
