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

#Add your list of data the should be censored
sensible_information=input("Please enter all the Information you want to censor (SEPTERATED with ,")
#function that cleans the Data and transforms it to a list
def clean_data(sensible_information_string):
    sensible_data=sensible_information_string.split(",")
    return sensible_data

#censoring function 
def censor(phrase,sensible_content_list):
    for sensible_content in sensible_content_list:
        if sensible_content in phrase:
            phrase=phrase.replace(sensible_content, "CENSORED")      
    return write_in_doc(phrase)

#writing the text in a txt or docx file
def write_in_doc(phrase):
    file_format=input("In which format do you want to store your information: txt or docx")
    if file_format=="txt":
        with open("Anette.txt", "w") as text_file:
            text_file.write(phrase)
    elif file_format=="docx":
        mydoc = docx.Document()
        mydoc.add_paragraph(phrase)
        mydoc.save("Anette_H.docx")   

print(censor(page_text, clean_data(sensible_information)))
