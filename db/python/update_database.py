import database
import read_docx
import read_tossup

paragraphs = read_docx.read_docx('http://quizbowlpackets.com/2239/Russian%20History%20Bee.docx')
texts = read_docx.extract_texts(paragraphs)
frequencies = read_docx.frequency_dict(paragraphs)
question_answers = read_tossup.split_question_answers(texts)

for i in range(len(question_answers)):
    question,answer = question_answers[i]
    database.add_tossup(answer, 'History', 'Russian History', i + 1, 'HS', question, 1, 'Pigeon Invitational', 2019)

database.cursor.close()