#Compare Hamming distance between two sequences
DNAseq1 = input("Please enter first sequence: \n")
DNAseq2 = input("Please enter second sequence: \n")
def hem_distance_counter(DNAseq1, DNAseq2):
    hem_distance = 0
    for nucleotide in range(len(DNAseq1)):
        if DNAseq1[nucleotide] != DNAseq2[nucleotide]:
            hem_distance += 1
        else:
            continue
    return hem_distance

print(f"The Hemming score between sequences is {hem_distance_counter(DNAseq1,DNAseq2)}")
    
