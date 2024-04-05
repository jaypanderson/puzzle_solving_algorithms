def transform(first, second):
    assert len(first) == len(second)
    n = len(first)
    assert set(first) == set(range(n))
    assert set(second) == set(range(n))

    transpositions = []
    current = list(first)
    for i in range(n):
        if current[i] != second[i]:
            idx = current.index(second[i])
            assert idx != i
            transpositions.append((i, idx))
            current[i], current[idx] = current[idx], current[i]
        assert current[i] == second[i]
    return transpositions


if __name__ == '__main__':
    print(transform([3, 4, 0, 2, 1], [0, 1, 3, 4, 2]))

