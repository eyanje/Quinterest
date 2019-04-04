import read_file
import parse_question
import database
import re,sys

print(f'Opening {sys.argv[1]}')

texts = read_file.extract_texts(read_file.read_docx(sys.argv[1]))

if texts:

    year = re.search(r'([1-3][0-9][0-9][0-9])', sys.argv[1])[0]

    subject = input('Subject: ')
    subsubject = input('Subsubject: ')
    difficulty = input('Difficulty: ')
    name = input('Tournament Name: ')

    tournament = parse_question.parse_tossup(texts)

    for round in tournament:
        for i,tossup in enumerate(round):
            database.add_tossup(
                tossup.answer,
                subject,
                subsubject, # Subsubject
                i + 1, # Question Number
                tournament.difficulty, # Difficulty
                tossup.question,
                round.round_num, # Round
                name,
                year)