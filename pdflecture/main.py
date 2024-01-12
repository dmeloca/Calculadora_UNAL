import fitz  

def extract_line(pdf_path, pageIndex ,line):
    doc = fitz.open(pdf_path)  # Open the PDF document
    try:
        page = doc[pageIndex]  # Assuming you want to extract text from the second page (index 1)
        extractedText = page.get_text("text").split('\n')[line]  # Extract the first line
        return extractedText
    except IndexError:
        return "Error: The document may not have a second page."

    finally:
        doc.close()  # Close the PDF document

if __name__ == "__main__":
    pdf_path = str(input("[?] Ingrese la ruta del archivo pdf: "))
    userData = {'name': extract_line(pdf_path, 0, 0),
                'studyPlan': extract_line(pdf_path, 0, 14).replace("Plan de estudios ", ""),
                'papa': extract_line(pdf_path, 0, 18) }
    print(f"[!] Bienvenido, {userData['name']}")
    print(f"[!] Su Plan de estudios es: {userData['studyPlan']}")
    print(f"[!] Su P.A.P.A es: {userData['papa']}")
    print(userData)
