"""
This script reads data from CSV file and populates SQLite database with tables for artists, 
genres, albums, and tracks.
"""

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Create the tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

# Open the CSV file and process its data
with open(r'files\tracks\tracks.csv', encoding='utf-8') as handle:
    for line in handle:
        line = line.strip()
        pieces = line.split(',')

        if len(pieces) < 7:  # Ensure all required columns are present
            continue

        # Extract data from the CSV columns
        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]

        # Insert the artist into the Artist table
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert the genre into the Genre table
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert the album into the Album table
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insert the track into the Track table
        cur.execute(
            '''
            INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (name, album_id, genre_id, length, rating, count),
        )

# Commit the transaction to save changes
conn.commit()

# Close the database connection
conn.close()

print("Finished processing and populating the database.")
