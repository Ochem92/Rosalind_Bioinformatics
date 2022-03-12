
#Open, read and line strip FASTA .txt file
#Input: FASTA .txt file
#Oputput: Stripped list of lines from the FASTA file
def read_file(filename):
    with open(filename, "r") as openfile:
        return [line.strip() for line in openfile.readlines()]

#Function to calculate the GC content of the sequence
#Input: string of DNA sequence
#Output: GC ratio in % of the DNA sequence, rounded to 0.001.
def calculate_GC_content(sequence):
    return((sequence.count("C")+sequence.count("G"))/len(sequence)*100)

#Strip '>' indicator from sequence ID
#Input: FASTA ID string
#Output: Cleaned FASTA ID string
def remove_FASTA_indicator(FASTA_ID):
    seqname = FASTA_ID[1:]
    return seqname

#Call function to create list from fileID
FASTA_file = read_file("FASTA_GC.txt")

#Create dict for the FASTA, sequence pairs
FASTA_Dict = {}

#Hold currently used ID for Key value in FASTA_Dict dict
FASTA_ID = ""

#Convert FASTA list into a (FASTA ID, sequence) pair, ensures sequence is one string.
for line in FASTA_file:
    if line.startswith(">"):
        FASTA_ID = line
        FASTA_Dict[FASTA_ID] = ""
    else:
        FASTA_Dict[FASTA_ID] += line

#use dict comprehenson to make new dict storing GC content and stripped seq ID.
GC_Dict = {remove_FASTA_indicator(key): calculate_GC_content(value) for key, value in FASTA_Dict.items()}

#Search for the result in GCdict that has the highest % GC content and return that key
HighestGCcontent = max(GC_Dict, key=GC_Dict.get)
#print ID of key with greatest GC content and the percentage
print(f"{HighestGCcontent}\n{round(GC_Dict[HighestGCcontent],6)}")