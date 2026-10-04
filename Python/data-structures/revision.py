sequences = ["ATGC", "GGGGCCCC", "ATATATAT", "GCGC", "AATTGGCC", "TTTTAAA"]
for sequence in sequences:
    length = len(sequence)
    G_count = sequence.count("G")
    C_count = sequence.count("C")
    GC % = (G_count + C_count)/length * 100

    print(f"sequence: {sequence}")
    print(f"length: {length}")
    print(f"G: {G_count}")
    print(f"C: {C_count}")
    print(f"GC: {GC}%")
