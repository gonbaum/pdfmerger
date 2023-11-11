import os
import PyPDF2
import sys

def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def merge_pdfs(folder_path, output_pdf):
    pdf_merger = PyPDF2.PdfFileMerger()

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_files.sort()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        pdf_merger.append(pdf_path)

    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":

    documents_folder = get_resource_path('documents')
    output_pdf_file = get_resource_path('merged_documents.pdf')

    merge_pdfs(documents_folder, output_pdf_file)
    print(f"PDFs in '{documents_folder}' merged successfully. Output saved to '{output_pdf_file}'.")