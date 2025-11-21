from PyPDF2 import PdfReader, PdfWriter

pdfs = ["file1.pdf", "file2.pdf"]   # Input PDF files
writer = PdfWriter()

for pdf in pdfs:
    reader = PdfReader(pdf)
    # Adding only page 0 (first page) from each PDF
    writer.add_page(reader.pages[0])

with open("merged_output.pdf", "wb") as f:
    writer.write(f)

print("Selected pages merged into merged_output.pdf")
