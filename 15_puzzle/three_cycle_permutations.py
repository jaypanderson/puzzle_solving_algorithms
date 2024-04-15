"""
returns a list of three cycle transposes that are need to reach the second list from the first list.
"""

def transform_by_3_cycles(first, second):
    assert len(first) == len(second)
    n = len(first)
    assert set(first) == set(range(n))
    assert set(second) == set(range(n))
    cycles = []
    current = list(first)
    for i in range(n - 2):
        if current[i] != second[i]:
            idx = current.index(second[i])
            spare = i + 1 if idx != i + 1 else i + 2
            assert i != idx and i != spare and idx != spare
            cycles.append((idx, i, spare))
            current[i], current[idx], current[spare] = current[idx], current[spare], current[i]
        assert current[i] == second[i]
    return cycles


if __name__ == '__main__':
    print(transform_by_3_cycles(
        [3, 4, 0, 2, 1, 5],
        [0, 5, 1, 4, 3, 2]))
