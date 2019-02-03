import mysql.connector

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
