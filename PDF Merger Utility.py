from PyPDF2 import PdfMerger
import sys

merger = PdfMerger()
for fname in sys.argv[1:]:
    merger.append(fname)
merger.write("merged.pdf")
merger.close()
print("Merged into merged.pdf")
