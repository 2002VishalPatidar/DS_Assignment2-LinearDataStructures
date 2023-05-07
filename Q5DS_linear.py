def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    
    for x in arr:
        if freq[x] > 1 and x not in duplicates:
            duplicates.append(x)
    
    return duplicates
arr = [4, 2, 3, 4, 6, 2, 5]
duplicates = find_duplicates(arr)
print(duplicates)  