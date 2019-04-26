import pdf_file_merger
import os

for base, dirs, files in os.walk('./Merged'):
    for file in files:
        if os.path.splitext(file)[1].lower() == '':
                pdf_file_merger.merge_from_file(os.path.join(base, file))
