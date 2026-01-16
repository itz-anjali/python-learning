# merge pdfs in pdf
import os
from PyPDF2 import PdfMerger

print(" wellcome to merger pdf world:~")

path= "/" # set a/c to ypur path

current_dir = os.listdir(path)
current_dir.sort()
merge = PdfMerger()
for pdfs in current_dir:
    
    if pdfs.endswith(".pdf"):
        full_path = f"{path}/{pdfs}"
        merge.append(full_path)

merge.write("Result.pdf")
merge.close()

print("done")