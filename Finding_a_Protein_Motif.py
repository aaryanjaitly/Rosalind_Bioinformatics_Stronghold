"""
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""
"""
Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

from urllib.request import urlretrieve
import re
import os

Seq_ID = []
while True:
    try:
        line = input()
        line = line
    except EOFError:
        break
    Seq_ID.append(line)

FILES = []
for i in Seq_ID:
    file_name = i[0:6] + ".fasta"
    FILES.append(file_name)
    url = ("https://rest.uniprot.org/uniprotkb/"+file_name)
    urlretrieve(url, file_name)


for file, id in zip(FILES, Seq_ID):
    with open(file, 'r') as f:
        if os.path.getsize("./"+file) == 0:
            FILES.remove(file)
            Seq_ID.remove(id)
        else:
            next(f)
            lines = f.read().replace('\n', '')
            Sequene = lines.strip()
            mstart = [m.start(0)+1 for m in re.finditer(pattern = r'(?=(N[^P][ST][^P]))', string=Sequene)]
            if(mstart != []):
                print(id)
                print(' '.join(str(x) for x in mstart))
            
os.system("rm *.fasta")