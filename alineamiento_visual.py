# Import libraries
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.pairwise2 import format_alignment

# Creating sample sequences (no debe haber espacio entre los caracteres)
seq1 = Seq("TAGAGTCACACTTGCAAGTCTATATGTCTGCAGCATCGGACCGGTAATCGGCGCATTTTTAGTACTGCACAACCGAAGCG")
seq2 = Seq("AACCTTTTGTTGCAAGTGTGACTCTACGCTTCGGTTGTGCGT")

# Finding similarities
alignments = pairwise2.align.globalxx(seq1, seq2)

# Showing results
for alignment in alignments:
	print(format_alignment(*alignment))
