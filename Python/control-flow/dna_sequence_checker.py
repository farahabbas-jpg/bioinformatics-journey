sequence = "ATGCGGAT"

print(sequence)

length = len(sequence)
print(length)

if length >= 5 and "G" in sequence:
    print("Sequence passes")
else:
    print("Sequence fails")
