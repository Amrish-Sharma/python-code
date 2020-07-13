import os

import PyPDF2

# welcome user

print('This is Programming Assignment 5!')

print('Today, we will be encrypting some pdf files!')

print()

print('Here are all the files located in the source folder: ')

# Source and destination

source = '.\\Source\\'

destination = '.\\Destination\\'

thisdir = os.getcwd()

# Path for source location

#path = os.getcwd()

source_content = os.listdir(thisdir + source)

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".pdf"):
            print(os.path.join(r, file))

# write the filenames to the screen

#for content in source_content:

#print('- ' + content)

print('Loading the pdf files....')

print('Encrypting and writing pdf files to destination folder....')

for content in source_content:

# choosing only pdf files from the source folder to open

    if content.endswith('.pdf'):

        pdf_file = open(source + content, 'rb')

        pdf_file_reader = PyPDF2.PdfFileReader(pdf_file)

        pdf_file_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_file_reader.numPages):
            pdf_file_writer.addPage(pdf_file_reader.getPage(page_num))

# the password = 'enigma'

            pdf_file_writer.encrypt('enigma')

    # write the new files to the destination folder

            encryted_file_path = destination + 'encrypted_' + content

            result_pdf = open(encryted_file_path, 'wb')

            pdf_file_writer.write(result_pdf)

        result_pdf.close()

print('The pdf files have been encrypted to the recommended destination folder.')

# declare path for destination folder

destination_content = os.listdir(thisdir + destination)

# searching through the destination folder

# writing pdf files on screen

print('New encrypted pdf files have been detected in the destination folder:')

for content in destination_content:

# choosing only pdf files from the destination folder to print

    if content.endswith('.pdf'):

        print('- ' + content)

# Final touch

print("Have a wonderful day!")

print('That completes this Programming Assignment!')