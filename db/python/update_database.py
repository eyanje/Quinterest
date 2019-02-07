import database
import read_docx
import read_tossup
import url_browser

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

        if (doc_name[-3:] == 'doc' or doc_name[-4:] == 'docx'):
            # Read paragraphs
            paragraphs = read_docx.read_docx(doc_link)

            # Extract pieces of text
            texts = read_docx.extract_texts(paragraphs)
            frequencies = read_docx.frequency_dict(paragraphs)
            question_answers = read_tossup.split_question_answers(texts)

            # Extract questions and answers from text
            for i in range(len(question_answers)):
                question,answer = question_answers[i]
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

        else:
            print('PDFs not supported')
        
database.cursor.close()

