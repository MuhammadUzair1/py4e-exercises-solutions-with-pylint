"""
This script reads a JSON file containing roster data and populates a SQLite database.
The database has tables for users, courses, and members with their roles.
It outputs a computed result from the database as specified.
"""

import json
import sqlite3

# Create connection object
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Set up the database schema
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Read filename from input
FILE_NAME = input('Enter file name: ')

# Use default if filename is not entered
if len(FILE_NAME) < 1:
    FILE_NAME = 'files/roster_data.json'  # Modified to use the correct sample filename

# Open and load JSON data
with open(FILE_NAME, encoding='utf-8') as file:
    json_data = json.load(file)

# Process the JSON data and populate the database
for entry in json_data:
    name, title, role = entry

    # Insert the user into the User table
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert the course into the Course table
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert the membership into the Member table
    cur.execute(
        '''
        INSERT OR REPLACE INTO Member (user_id, course_id, role) 
        VALUES (?, ?, ?)
        ''',
        (user_id, course_id, role),
    )

# Commit the changes
conn.commit()

# Execute and display the required query result
SQL_QUERY = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X 
FROM User 
JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
'''

for row in cur.execute(SQL_QUERY):
    print(str(row[0]))

# Close the cursor and connection
cur.close()
conn.close()
