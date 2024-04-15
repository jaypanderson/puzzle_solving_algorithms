def sequence():
    first = list("MARINE")
    second = list("AIRMEN")
    transpose = []
    for i, char in enumerate(second):
        idx = first.index(char)
        if idx != i:
            transpose.append((i, idx))
            first[i], first[idx] = first[idx], first[i]
    print(transpose)
    return transpose


if __name__ == "__main__":
    sequence()
