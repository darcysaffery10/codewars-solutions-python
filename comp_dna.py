# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    output = ""
    comps = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    for letter in dna:
        output = output + comps[letter]
    return output  