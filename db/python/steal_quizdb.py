import database
import json
import urllib.request

import sys

# Steals questions from quizdb

def try_key(dictionary, *keys):
    item = dictionary
    try:
        for k in keys:
            item = item[k]
        return item
    except KeyError:
        return ''

def store_tossup(tossup):
    """Stores a parsed QuizDB JSON tossup in the database"""
    database.add_tossup(
        try_key(tossup, 'answer'),
        try_key(tossup, 'category', 'name'),
        try_key(tossup, 'subcategory', 'name'),
        try_key(tossup, 'number'),
        try_key(tossup, 'difficulty'),
        try_key(tossup, 'question'),
        try_key(tossup, 'round'),
        try_key(tossup, 'tournament', 'name'),
        try_key(tossup, 'tournament', 'year'))

def store_bonus(bonus):
    """Stores a parsed QuizDB JSON bonus in the database"""
    database.add_bonus(
        try_key(bonus, 'formatted_answers', 0),
        try_key(bonus, 'formatted_answers', 1),
        try_key(bonus, 'formatted_answers', 2),
        try_key(bonus, 'category', 'name'),
        try_key(bonus, 'subcategory', 'name'),
        try_key(bonus, 'number'),
        try_key(bonus, 'difficulty'),
        try_key(bonus, 'formatted_texts', 0),
        try_key(bonus, 'formatted_texts', 1),
        try_key(bonus, 'formatted_texts', 2),
        try_key(bonus, 'formatted_leadin'),
        try_key(bonus, 'round'),
        try_key(bonus, 'tournament', 'name'),
        try_key(bonus, 'tournament', 'year')
    )

def steal(num):
    """Steals num number of search results"""
    with urllib.request.urlopen('https://www.quizdb.org/api/search?search[query]=&search[limit]=true') as file:
        text = json.loads(file.read())
    text = text['data']
    
    tossups = text['tossups']
    tossups = []
    for tossup in tossups:
        store_tossup(tossup)
    
    bonuses = text['bonuses']
    for bonus in bonuses:
        store_bonus(bonus)

try:
    steal(int(sys.argv[1]))
except ValueError:
    print(f'{sys.argv[1]} is not a number!')
    print('Usage: python steal_quizb.py <n>')
    print('where n is the number of random questions to steal')