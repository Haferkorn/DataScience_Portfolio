from pathlib import Path
import PyPDF2
import docx

#Access the PDF File you want to censor
file = open('Haferkorn.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(file)
#Change this line if you want to censor information NOT on the first page
first_page = pdf.getPage(0)

#Store your Text
page_text=first_page.extractText()


sensible_information=input("Please enter all the Information you want to censor (SEPTERATED with ,")
def clean_data(sensible_information_string):
    sensible_data=sensible_information_string.split(",")
    return sensible_data

def censor(phrase,sensible_content_list):
    for sensible_content in sensible_content_list:
        if sensible_content in phrase:
            phrase=phrase.replace(sensible_content, "CENSORED")      
    return write_in_doc(phrase)

def write_in_doc(phrase):
    file_format="docx"#input("In which format do you want to store your information: txt or docx")
    if file_format=="txt":
        with open("Anette.txt", "w") as text_file:
            text_file.write(phrase)
    elif file_format=="docx":
        mydoc = docx.Document()
        mydoc.add_paragraph(phrase)
        mydoc.save("Anette_H.docx")   

print(censor(page_text, clean_data(sensible_information)))
