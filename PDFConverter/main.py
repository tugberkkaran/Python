# Import pdf2docx package and Converter class
from pdf2docx import Converter

# Import os to create docx_path name automatically
import os

# Import time package and time function to give elapsed time
from time import time

# Defining start time
start_time = time()

# Write the path of the pdf document which you want to work on.
pdf_path = "pdf_file_name.pdf"

# Get the filename from the pdf_file
file_name = os.path.splitext(os.path.basename(pdf_path))[0]

# The file name is obtained by extracting the file name from pdf_file and removing the extension,
# then it is combined with .docx
docx_path = f"{file_name}.docx"

# Create an object by using Converter class
document = Converter(pdf_file=pdf_path)

# Call the convert method for changing pdf to docx
document.convert(docx_filename=docx_path)

# To clean memory
document.close()

# Defining end time
end_time = time()

# Defining elapsed time
elapsed_time = end_time - start_time

# Return information for the user.
print("Converting process has been completed.")
print("Process takes {:.2f} seconds.".format(elapsed_time))
