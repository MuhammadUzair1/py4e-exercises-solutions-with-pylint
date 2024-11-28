'''
In this program we will be reading mailbox data (mbox.txt) and 
counting the number of email messages per organization (i.e. domain name of the email address). 
We will store the counts in a SQLite database with the following schema to keep track of the domains 
and the number of messages for each domain:
'''

import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('email_counts.db')
cur = conn.cursor()

# Create the Counts table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)
''')

# Open the mbox.txt file
with open('./files/mbox.txt', 'r', encoding='utf-8') as file:
    # Read through the file line by line
    for line in file:
        # Look for lines starting with 'From ' (email addresses are in these lines)
        if line.startswith('From '):
            # Extract the email address using regex
            email = line.split()[1]
            domain = email.split('@')[1]

            # Check if the domain is already in the database
            cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
            row = cur.fetchone()

            if row is None:
                # If domain is not found, insert it with count = 1
                cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
            else:
                # If domain is found, update the count
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit the transaction outside of the loop for efficiency
conn.commit()

# Close the database connection
conn.close()

print("Finished processing and updating the database.")
