import database
import parse_question
import read_file
import url_browser

# This module loads up multiple tournaments from the base page and loads them into the document

base_links = url_browser.load_base_page()

# Loops through all tournaments
for tournament_name, tournament_link in base_links:
    try:
        year = int(tournament_name[:4])
        tournament_name = tournament_name[4:].lstrip(': ,')
    except ValueError:
        year = None

    doc_info = url_browser.load_details(tournament_link)

    # Loops through all documents
    for doc_name, doc_link in url_browser.load_tournament_links(tournament_link):
        # If doc or docx file, parse with Document

        if (doc_name.split('.')[-1] in ('doc', 'docx')):
            # Read paragraphs
            paragraphs = read_file.read_docx(doc_link)

        elif (doc_name.split('.')[-1] == 'pdf'):
            print('PDFs are not supported')
            paragraphs = read_file.read_pdf(doc_link)
        
        # Extract pieces of text
        texts = read_file.extract_texts(paragraphs)
        frequencies = read_file.frequency_dict(paragraphs)
        question_answers = parse_question.parse_tossup(texts)

        # Input all questions ans answers
        # Extract questions and answers from text
        for i,question,answer in enumerate(question_answers):
            database.add_tossup(
                answer,
                doc_info.subject,
                'Pigeonology', # Subsubject
                i + 1, # Question Number
                doc_info.difficulty, # Difficulty
                question,
                1, # Round
                doc_info.name,
                doc_info.year)

database.cursor.close()

