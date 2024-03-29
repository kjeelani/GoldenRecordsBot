import sqlite3 as sql
import pandas as pd
import os
import shutil

conn = sql.connect('submissions.sql')
c = conn.cursor()

# c.execute('''CREATE TABLE competitions (
#                 id TEXT PRIMARY KEY,
#                 theme TEXT,
#                 description TEXT,
#                 closed BOOLEAN
#             )
#            ''')

# c.execute('''CREATE TABLE submissions (
#                 comp_id TEXT,
#                 username TEXT,
#                 title TEXT,
#                 description TEXT,
#                 date TEXT,
#                 audio_src TEXT
#             )
#            ''')

def print_database(table):
    try:
        print('\n',pd.read_sql(f'SELECT * from {table}', conn))
    except:
        return

def reset_testing():
    c.execute('DELETE FROM competitions')
    c.execute('DELETE FROM submissions')
    shutil.rmtree("./audio")
    os.mkdir("./audio")

#reset_testing() #remove this ONLY to reset database and clear audio files
print_database('competitions')
print_database('submissions')


conn.commit()
conn.close()