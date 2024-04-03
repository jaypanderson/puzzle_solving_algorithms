"""
recursion solution to solve a problem on leet code. to see if we can find a path in the matrix that spells out a word
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.
"""

def backtrack(board, i, j, word, length, height, seen):
    vectors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    if board[i][j] != word[0]:
        return False
    word = word[1:]
    if len(word) == 0:
        return True
    seen.append((i, j))
    for y, x in vectors:
        if (i + y, j + x) in seen:
            continue
        if 0 <= i + y <= height and 0 <= j + x <= length:
            if backtrack(board, i + y, j + x, word, length, height, seen):
                return True
    seen.pop()
    return False


def exist(board: list[list[str]], word: str) -> bool:
    seen = []
    length = len(board[0]) - 1
    height = len(board) - 1
    if length == 1 and height == 1 and len(word) == 1:
        return board[0][0] == word
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(board, i, j, word, length, height, seen):
                return True
    return False


if __name__ == '__main__':
    print(exist([['a']], 'a'))
