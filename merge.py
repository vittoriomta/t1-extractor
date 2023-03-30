import pandas as pd
import os
import fitz


def merge():
    # read in the CSV file with the PDF filenames and sort by the 'Filename' column
    df = pd.read_excel('output/Data_sorted.xlsx')

    # create a new PDF file to write the merged PDFs to
    output_path = 'output/T1.pdf'
    pdf_out = fitz.open()

    # iterate over each row in the sorted dataframe and add the corresponding PDF to the merged PDF
    for _, row in df.iterrows():
        # open the input PDF file using PyMuPDF
        input_path = os.path.join('upload', row['Filename'])
        pdf_in = fitz.open(input_path)
        
        # iterate over each page in the input PDF and add it to the output PDF
        for page in pdf_in:
            pdf_out.insert_pdf(pdf_in, from_page=page.number, to_page=page.number)
        
        # close the input PDF file
        pdf_in.close()

    # save the merged PDF to disk
    pdf_out.save(output_path)
    pdf_out.close()
