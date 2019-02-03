
def split_question_answers(texts):
    question_answers = []
    for i in range(len(texts)):
        text = texts[i].upper();
        if ('ANSWER' in text):
            question = texts[i - 1]
            answer = texts[i]
            answer = answer[text.find('ANSWER')+len('ANSWER'):]
            answer = answer.lstrip(':, ')
            question_answers.append((question, answer))
    return question_answers