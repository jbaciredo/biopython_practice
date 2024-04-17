# Import libraries
from Bio import Align
from Bio.Seq import Seq
 
# Creating sample sequences
seq1 = Seq("TGTGACTA")
seq2 = Seq("CATGGTCA")
 
# Calling method
aligner = Align.PairwiseAligner()
 
# Showing method attributes
print(aligner)
 
# Finding similarities
alignments = aligner.align(seq1, seq2)
 
# Showing results
for alignment in alignments:
    print(alignment)