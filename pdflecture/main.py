import fitz  

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF document
    text = ""
    counter = 1
    for page_number in range(doc.page_count):
        page = doc[page_number]
        text += str(counter) + page.get_text()
        counter += 1
    doc.close()  # Close the PDF document
    return text

if __name__ == "__main__":
    pdf_path = str(input("[?]Ingrese la ruta del archivo pdf: "))
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
