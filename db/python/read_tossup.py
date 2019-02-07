
def split_question_answers(texts):
    question_answers = []
    for i in range(len(texts)):
        text = texts[i].upper()
        if ('ANSWER' in text):    
            answer = texts[i][text.find('ANSWER')+len('ANSWER'):].lstrip(':, ')
            if (text.startswith('ANSWER')):
                question = None
                for j in range(i - 1, 0, -1):
                    question = texts[i - i].strip()
                    if (len(question) > 4):
                        break
            else:
                question = texts[i][:text.find('ANSWER') - 1].rstrip()

            if (question == None):
                break
            question_answers.append((question, answer))
    return question_answers