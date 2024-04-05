def convert(transposition):
    """
    converts a normal transposition into a series of neighbor transpositions
    :param transposition:
    :return:
    """
    i, j = transposition
    assert i != j
    i, j = min(i, j), max(i, j)

    return [(s, s + 1) for s in range(i, j)] + [(s, s + 1) for s in reversed(range(i, j - 1))]


def transform(first: str, second: str) -> None:
    trans = [x for x in first]
    moves = []
    for i, char in enumerate(second):
        if char == trans[i]:
            continue
        else:
            idx = trans.index(char)
            for a, b in convert((i, idx)):
                moves.append((a,b))
                trans[a], trans[b] = trans[b], trans[a]
    print(moves)
    print(''.join(trans))


if __name__ == '__main__':
    transform('MARINE', 'AIRMEN')
