import sqlite3
connection = sqlite3.connect('app.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE groceries
                  (ans1 TEXT, ans2 TEXT)''')
groceries = ['Grand Theft Auto V',
             'The Witcher 3',
             'Red Dead Redemption II',
             'God of Wdsar ',
             'Resident Evil 2',
             'Mafia 1 remake',
             'Days Gone',
             'Undertale']
groceries1 = ['Minecraft',
             'Stalker all parts',
             'Mass efect',
             'Fallout',
             'Mafia 2',
             'Day r',
             '60 seconds',
             'The forest']
for x in groceries:
    cursor.execute(f'''INSERT INTO groceries(ans1, ans2) VALUES
                    {(x,'-----------------')}''')
for a in groceries1:
    cursor.execute(f'''INSERT INTO groceries(ans1, ans2) VALUES
                    {('-------------------',a)}''')

connection.commit()
connection.close()