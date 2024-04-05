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
    pass


if __name__ == '__main__':
    print(convert((2, 5)))
    transform('MARINE', 'AIRMEN')
