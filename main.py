from blosum62 import blosum
from pairwise_alignment import pairwise_alignment

seq_v = input(str("Insert sequence v: "))
seq_w = input(str("Insert sequence w: "))
penalty = int(input("Insert the penalty: "))
seq_v.upper()
seq_w.upper()

(seq_v, seq_w) = pairwise_alignment(seq_v, seq_w, blosum, penalty)

print("Nova sequencia v: ", seq_v, "\nNova sequencia w: ", seq_w)