class Tournament:
    def __init__(self):
        self.name = str()
        self.year = 1970
        self.difficulty = 'HS'
        self.rounds = []
    def __getitem__(self, index):
        return self.rounds[index]

class Round:
    def __init__(self, round_num):
        self.round_num = round_num
        self.questions = []
    def __getitem__(self, index):
        return self.questions[index]
        
class Tossup:
    def __init__(self):
        self.question = str()
        self.answer = str()

def parse_tossup(texts):
    """Returns a Tournament from the texts"""
    tournament = Tournament()
    
    tournament.rounds.append(Round(1))
    
    for i in range(len(texts)):
        text = texts[i].upper()
        # Find the answer first
        if (text.startswith('ANSWER')):
            tossup = Tossup()
            tossup.answer = texts[i][text.find('ANSWER')+len('ANSWER'):].lstrip(':, ')
            # Find the answer from the previous paragaphs
            if (text.startswith('ANSWER')):
                tossup.question = None
                for j in range(i - 1, 0, -1):
                    tossup.question = texts[i - 1].strip()
                    if (len(tossup.question) > 4):
                        break

            if (tossup.question == None):
                break
            tournament.rounds[-1].questions.append(tossup)
        elif 'ROUND' in text:
            try:
                round_end_loc = text.find('ROUND ') + len('ROUND ')
                round_num = int(text[round_end_loc:text.find(' ', round_end_loc)])
                tournament.rounds.append(Round(round_num))
            except ValueError:
                pass
    return tournament
