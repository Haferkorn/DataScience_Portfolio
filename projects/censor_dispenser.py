from pathlib import Path
import PyPDF2


file = open('Haferkorn.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(file)

first_page = pdf.getPage(0)
pdf_path = (
    Path.home()
    / "Haferkorn.pdf"
    / "censor_dispenser.py"
)
outputpath=Path.home()/"Anette.txt"

page_text=first_page.extractText()


def censsor(phrase,sensible_content_list):
    for sensible_content in sensible_content_list:
        if sensible_content in phrase:
            phrase=phrase.replace(sensible_content, "CENSSORED")      
    return write_in_doc(phrase)

def write_in_doc(phrase):
    with open("Anette.txt", "w") as text_file:
        text_file.write(phrase)

print(censsor(page_text, ["Haferkorn","Anette", "28.02.1997","Stuttgart"]))