get_dna = input('Please enter DNA sequence: \n')
dna_r = get_dna[::-1]
dna_comp = dna_r.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
dna_loud = dna_comp.upper()
print(dna_loud)
