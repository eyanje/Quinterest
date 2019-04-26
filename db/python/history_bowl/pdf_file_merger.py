import glob, io, os, sys

from PyPDF2 import PdfFileReader, PdfFileMerger

def merge_pdfs(links, output):
    print(f'Merging to {output}')
    merger = PdfFileMerger()
    for link in links:
            with open(link, 'rb') as file:
                merger.append(
                    PdfFileReader(
                        file
                    )
                )
    
    merger.write(output)

links = list()

def add_files(uri):
    if os.path.isdir(uri):
        for base, dirs, files in os.walk(uri):
            
            for file in files:
                add_files(os.path.join(base, file))

            for dir in dirs:
                add_files(os.path.join(base, dir))
    elif os.path.splitext(uri)[1].lower() == '.pdf':
        links.append(uri)

def merge_from_file(uri):
    print(f'Merging from file {uri}')
    with open(uri) as file:
        for line in file:
            for g in glob.iglob(os.path.join(os.path.dirname(uri), line)):
                # print(os.path.join('.', os.path.relpath(os.path.join(os.path.dirname(uri), g))))
                add_files(os.path.join('.', os.path.relpath(g)))

    merge_pdfs(links, uri + '.pdf')

for arg in sys.argv:
    merge_from_file(arg)
