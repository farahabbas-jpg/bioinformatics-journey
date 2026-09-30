with open("dna.txt", "r") as file:
    sequence = file.read().strip()

    sequence = sequence.strip()

print(sequence)
print("Length", len(sequence))
print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))

if all(base in "ATGC" for base in sequence):
    print("Sequence is valid DNA")
else:
    print("Invalid DNA sequence")

    for base in sequence:
        if base not in "ATGC":
            print("Invalid base:", base)

gc_count = sequence.count("G") + sequence.count("C")
gc_percentage = (gc_count / len(sequence)) * 100

print("GC%:", round(gc_percentage, 2))
