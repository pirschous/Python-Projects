import sqlite3

# connect to database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT)''')

# list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through file names and add qualifying files to database
for filename in fileList:
    if filename.endswith('.txt'):
        c.execute('INSERT INTO files (filename) VALUES (?)', (filename,))
        conn.commit()

# query database to retrieve qualifying file names
c.execute('SELECT filename FROM files')
result = c.fetchall()

# print qualifying file names to console
print('Qualifying text files:')
for row in result:
    print(row[0])

# close database connection
conn.close()
