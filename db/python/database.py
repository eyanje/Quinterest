import mysql.connector

# This module connects to the database

quinterestdb = mysql.connector.connect(
    user="quinterestdb",
    passwd="quinterestdb",
    database="quinterestdb")

cursor = quinterestdb.cursor(buffered=True)

def add_tossup(answer, category, subcategory, question_number, difficulty, question, round, tournament, year):
    try:
        cursor.execute('SELECT * FROM `tossupsdbnew`'
            'WHERE '
            'Answer=%s AND '
            'Category=%s AND '
            'Subcategory=%s AND '
            '`Question #`=%s AND '
            'Difficulty=%s AND '
            'Question=%s AND '
            'Round=%s AND '
            'Tournament=%s AND '
            'Year=%s LIMIT 1',
            (answer, category, subcategory, question_number, difficulty, question, round, tournament, year)
        )
        if (cursor.fetchone() == None):
            cursor.execute('INSERT INTO tossupsdbnew '
                '(Answer, Category, Subcategory, `Question #`, Difficulty, Question, Round, Tournament, Year) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
                (answer, category, subcategory, question_number, difficulty, question, round, tournament, year))
        quinterestdb.commit()
    except mysql.connector.Error as error:
        print(f"""Error adding tossup
    {answer},
    {category},
    {subcategory},
    {question_number},
    {difficulty},
    {question},
    {tournament},
    {year}
    {error}""")

def add_bonus(answer1, answer2, answer3, category, subcategory, question_number, difficulty, question1, question2, question3, intro, round, tournament, year):
    try:
        cursor.execute('SELECT * FROM `bonusesdb`'
            'WHERE '
            'Answer1=%s AND '
            'Answer2=%s AND '
            'Answer3=%s AND '
            'Category=%s AND '
            'Subcategory=%s AND '
            '`Question #`=%s AND '
            'Difficulty=%s AND '
            'Question1=%s AND '
            'Question2=%s AND '
            'Question3=%s AND '
            'Intro=%s AND '
            'Round=%s AND '
            'Tournament=%s AND '
            'Year=%s LIMIT 1',
            (answer1, answer2, answer3, category, subcategory, question_number, difficulty, question1, question2, question3, intro, round, tournament, year)
        )
        if (cursor.fetchone() == None):
            cursor.execute('INSERT INTO bonusesdb '
                '(Answer1, Answer2, Answer3, Category, Subcategory, `Question #`, Difficulty, Question1, Question2, Question3, Intro, Round, Tournament, Year) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                (answer1, answer2, answer3, category, subcategory, question_number, difficulty, question1, question2, question3, intro, round, tournament, year))
        quinterestdb.commit()
    except mysql.connector.Error as error:
        print(f"""Error adding bonus
    Answer1: {answer1},
    Answer2: {answer2},
    Answer3: {answer3},
    Category: {category},
    Subcategory: {subcategory},
    Question #: {question_number},
    Difficulty: {difficulty},
    Question1: {question1},
    Question2: {question2},
    Question3: {question3},
    Intro: {intro},
    Tournament: {tournament},
    Year: {year}:
    {error}""")