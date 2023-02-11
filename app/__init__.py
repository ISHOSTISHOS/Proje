from flask import Flask
app = Flask(__name__)
from app import routes
print('Success')
print('Exercise 1')
file_name='text_message.txt'
with open(file_name,'w') as ok:
    hey=ok.write('I have two hobbies football and horizontal bar tricks')
with open(file_name) as ok:
    g=ok.read()
    print(g)