# python3 ./prot_seq_gen.py
# /mnt/c/my_mnt_c/Code/my_github/python_bioinf_2021/genome.fa
# codon table

# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi NCBI
# https://biopython.org/wiki/SeqIO
# https://biopython.org/wiki/Seq
# https://biopython.org/docs/dev/api/Bio.Seq.html

from Bio import SeqIO
from Bio.Seq import Seq

'''path_to_fasta = input("Imput path to fasta file: ")
codon_table = input("Input codon table. Default: Standart. \n"
                    "If you want another - choose it https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi  \n"
                    ": ")

if codon_table == '':
    codon_table = "Standart"'''

path_to_fasta = "/mnt/c/my_mnt_c/Code/my_github/python_bioinf_2021/ex.txt"
codon_table = 1



def fun(path_to_fasta, codon_table):
    my_fasta = open(path_to_fasta, "r")
    all_coding_dna = SeqIO.parse(my_fasta, "fasta")
    for i in all_coding_dna:
        protein = Seq.translate(i.seq, table=codon_table)
        yield protein
    my_fasta.close()

h = fun(path_to_fasta, codon_table)

answer = True
while answer == True:
    answer_input = input("Do you want to see next protein seq? \n"
               "answer (Y/N): ")
    if answer_input == "Y":
          print(next(h))
          answer = True
    elif answer_input == "N":
        print("Goodbye! Have a nice day!")
        answer = False


