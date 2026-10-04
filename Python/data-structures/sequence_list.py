sequences = ["ATGCGTAC","GGCAAT","TTTGGGCC","ATATAT","GCGCGC"]
 
for sequence in sequences: 

    g_count = sequence.count("G")
    c_count = sequence.count("C")
    length  = (len(sequence))
    gc = (g_count + c_count) / len(sequence) * 100 

    print (f"sequence: {sequence}")
    print (f"length: {length}")
    print (f"len(sequence): {len(sequence)}")
    print (f"C: {c_count}")
    print (f"G: {g_count}")
    print (f"gc%: {gc}%")
