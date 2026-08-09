sequence = "ATGAAATTTCCCGGG"

print("Sequence:", sequence)
print("Length:", len(sequence))

print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))
gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
at_content = (sequence.count("A") + sequence.count("T")) / len(sequence) * 100

print("GC content:", gc_content, "%")
print("AT content:", at_content, "%")

