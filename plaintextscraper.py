import pdfplumber

pdf_path = r"C:\Users\Seth Sander\OneDrive\Desktop\Textbooks\CYB 310\Practical Malware Analysis.pdf"
output_path = r"C:\Users\Seth Sander\OneDrive\Desktop\Textbooks\CYB 310\Practical_Malware_Analysis.txt"

with pdfplumber.open(pdf_path) as pdf:
    with open(output_path, "w", encoding="utf-8") as f:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                f.write(f"\n--- Page {page_number} ---\n")
                f.write(text)
                f.write("\n")

print("Text extraction complete!")
