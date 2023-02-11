import sqlite3
from flask import render_template,request,flash,redirect
from app import app
from random import shuffle
gr_lis = []
def get_data():
    connection = sqlite3.connect('./app/app.db')
    cursor = connection.cursor()
    cursor.execute('select ans1 from groceries')
    all_data = cursor.fetchall()
    all_data = [i[0] for i in all_data]
    cursor.execute('select ans2 from groceries')
    all_data1 = cursor.fetchall()
    all_data1 = [i[0] for i in all_data1]

    # gr_lis = all_data.copy()
    # shuffle(gr_lis)
    # gr_lis = gr_lis[:3]
    return all_data,all_data1
@app.route('/', methods = ['GET', 'POST'])
def index():
    global gr_lis
    all_data = get_data()
    return render_template('index.html',all_data = all_data[0],all_data1 = all_data[1], gr_lis = gr_lis)
@app.route('/add', methods = ['POST'])
def add():
    global gr_lis
    selected = request.form['selected']
    if selected not in gr_lis:
        gr_lis.append(selected)
    return redirect('/')
@app.route('/delete', methods=['POST'])
def delete():
    main_list = request.form.getlist('selected')
    global gr_lis
    for i in main_list:
        if i in gr_lis:
            gr_lis.remove(i)
    return redirect('/')
@app.route('/message', methods=['POST'])
def check_message():
    my_text = request.form['mes']
    my_file = 'file.txt'
    with open(my_file, 'a') as ok:
        f = ok.write(f'{my_text} \n')
    return redirect('/')
