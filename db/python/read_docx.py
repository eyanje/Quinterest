from docx import Document

import io
import urllib.request

def read_docx(path):
    path = '%20'.join(path.split(' '))
    try:
        with urllib.request.urlopen(path) as file:
                document = Document(io.BytesIO(file.read()))
                return document.paragraphs
    except urllib.error.HTTPError as error:
        print(f'Error loading docx {path}: {error}')

def extract_texts(paragraphs):
    texts = []
    for paragraph in paragraphs:
        texts.append(paragraph.text)
    return texts

def frequency_dict(paragraphs):
    frequencies = {}
    for paragraph in paragraphs:
        for word in paragraph.text.split():
            if (word not in frequencies):
                frequencies[word] = 0
            frequencies[word] += 1
    return frequencies