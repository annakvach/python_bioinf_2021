# my notes
# python3 ./prot_seq_gen.py
# /mnt/c/my_mnt_c/Code/my_github/python_bioinf_2021/genome.fa
# codon table

# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi NCBI
# https://biopython.org/wiki/SeqIO
# https://biopython.org/wiki/Seq
# https://biopython.org/docs/dev/api/Bio.Seq.html

'''
path_to_fasta = "/mnt/c/my_mnt_c/Code/my_github/python_bioinf_2021/genome.fa"
codon_table = 1
'''

from Bio import SeqIO
from Bio.Seq import Seq


# function


def dna_to_protein(path_to_fasta, codon_table):
    my_fasta = open(path_to_fasta, "r")
    all_coding_dna = SeqIO.parse(my_fasta, "fasta")
    for i in all_coding_dna:
        protein = Seq.translate(i.seq, table=codon_table)
        yield protein
    my_fasta.close()


# input data
print("Hello!")
path_to_fasta = input("Input path to the fasta file: ")
print()
codon_table = input("Input codon table. Default: Standart. \n"
                    "If you want another - choose it there https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi  \n"
                    ": ")

if codon_table == '':
    codon_table = 1

proin_seq = dna_to_protein(path_to_fasta, codon_table)

# to see next protein sequence
answer = True
while answer == True:
    answer_input = input("Do you want to see next protein sequence? \n"
               "answer (y/n): ")
    if answer_input == "y":
          print(next(proin_seq))
          answer = True
    elif answer_input == "n":
        print("Goodbye! Have a nice day!")
        answer = False


