def apply(lst, trans):
    first, second = trans
    lst[first], lst[second] = lst[second], lst[first]


word = ['S', 'T', 'O', 'P']
transpositions = [(0, 1), (1, 2), (2, 3)]

for transposition in transpositions:
    apply(word, transposition)
    
print(word)
