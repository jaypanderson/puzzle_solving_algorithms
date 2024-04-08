def odd_or_even(start, end, perm) -> None:
    original = [x for x in range(start, end)]
    swaps = 0
    for i in range(len(perm)):
        if perm[i] != original[i]:
            idx = original.index(perm[i])
            perm[i], perm[idx] = perm[idx], perm[i]
            swaps += 1
    if swaps % 2 == 0:
        print('Even')
    else:
        print('Odd')


def new_odd_or_even(perm, index=1) -> None:
    n = len(perm)
    visited = [False] * n
    cycle_count = 0

    for i in range(n):
        if not visited[i]:
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j] - index
                cycle_length += 1

            if cycle_length % 2 == 0:
                cycle_count += 1

    if cycle_count % 2 == 0:
        print('Even')
    else:
        print('Odd')










if __name__ == '__main__':
    new_odd_or_even([2, 1, 0, 4, 3], 0)  #[2 ,1, 0, 4, 3], [3, 2, 1, 5, 4]
