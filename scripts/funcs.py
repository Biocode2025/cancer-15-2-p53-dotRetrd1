import random

def Transcription(dna):
  map = {'A': 'A', 'T': 'U', 'G': 'G', 'C': 'C'}
  dna = dna.upper()
  return ''.join(map.get(n, '') for n in dna)

def Translation(rna, d, frame=2):
    protein = []
    rna = rna.upper()
    for i in range(frame, len(rna) - (len(rna)-frame)%3, 3):
        protein.append(d[rna[i:i+3]])
    return ''.join(protein)

def pointMutate(dna, pos):
    bases = ['A','T','G','C','DEL','INS']
    new_base = random.choice(bases)
    if new_base == 'DEL':
        mutated_dna = dna[:pos] + dna[pos+1:]
        return mutated_dna
    elif new_base == 'INS':
        insert_base = random.choice(['A', 'T', 'G', 'C'])
        mutated_dna = dna[:pos] + insert_base + dna[pos:]
        return mutated_dna
    while new_base == dna[pos]:
        new_base = random.choice(bases [:-2]) 
    mutated_dna = dna[:pos] + new_base + dna[pos+1:]
    return mutated_dna