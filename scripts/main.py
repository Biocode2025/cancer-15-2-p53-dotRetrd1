from pathlib import Path
import random

base = Path(__file__).resolve().parent
dataDir = base.parent / "data"
outDir = base.parent / "results"
from funcs import Transcription, Translation, pointMutate

dSeq = open(dataDir / "p53_sequence.fa").read().strip()
codon_AA = open(dataDir / "codon_AA.txt").read().strip().splitlines()
codon_dict = {}
for line in codon_AA:
    codon, aa = line.split()
    codon_dict[codon] = aa


rSeq = Transcription(dSeq)          #transcribe DNA to RNA
pSeq = Translation(rSeq, codon_dict)    #translate RNA to Protein

#mutate
for i in range(3):
    pos = random.randint(0, len(dSeq) - 1)
    dSeq = pointMutate(dSeq, pos)

rSeq1 = Transcription(dSeq)              #transcribe DNA to RNA after mutation
pSeq1 = Translation(rSeq1, codon_dict)   #translate RNA to Protein after mutation

stopDiff = pSeq1.count('*') - pSeq.count('*')       #count difference in stop codons
print(f"Number of new stop codons introduced due to mutation: {stopDiff}")

#output
outFile1 = outDir / "originalDNA.fa"
outFile2 = outDir / "mutatedDNA.fa"
outFile3 = outDir / "originalProtein.fa"
outFile4 = outDir / "mutatedProtein.fa"
outFile5 = outDir / "ReportAndAnswer.txt"
with open(outFile1, 'w') as f:
    f.write("Original DNA Sequence:\n")
    f.write(dSeq + "\n\n")
with open (outFile2, 'w') as f:
    f.write("Mutated DNA Sequence:\n")
    f.write(dSeq + "\n\n")
with open(outFile3, 'w') as f:
    f.write("Original Protein Sequence:\n")
    f.write(''.join(pSeq) + "\n\n")
with open(outFile4, 'w') as f:
    f.write("Mutated Protein Sequence:\n")
    f.write(''.join(pSeq1) + "\n")
with open(outFile5, 'w') as f:
    f.write("Report and Answer:\n")
    f.write(f"Number of new stop codons introduced due to mutation: {stopDiff}\n")
    f.write("My conclusion: " \
    "The protein sequence on average seem to get shorter because usually more stop codons are introduced than removed however\n" \
    " this is not always the case and its not uncommon for the protein sequence to get longer or remain the same, \nit just seems statistically " \
    "less likely.")
