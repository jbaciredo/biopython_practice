# Import libraries
from Bio import pairwise2
from Bio.Seq import Seq
 
# Creating sample sequences
seq1 = Seq("TGTGACTA")
seq2 = Seq("CATGGTCA")
 
seq_pl16 = Seq("TAGAGTCACACTTGCAAGTCTATATGTCTGCAGCATCGGACCGGTAATCGGCGCATTTTTAGTACTGCACAACCGAAGCG")
seq_t16 = Seq("AAC CTT TTG TTG CAA GTG TGA CTC TAC GCT TCG GTT GTG CGT")

seq_t16_nogap = Seq("AACCTTTTGTTGCAAGTGTGACTCTACGCTTCGGTTGTGCGT")

# Finding similarities
alignments = pairwise2.align.globalxx(seq_pl16, seq_t16_nogap)
 
# Showing results
for match in alignments:
    print(match)


