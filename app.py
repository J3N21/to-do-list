"""
    Project - Replicating the "Reminders" from iPhone using Flask
    Author:  Jailynne Estevez (jesteveznolasco@bennington.edu)
    Date: 12/10/2019
"""
from flask import Flask, request
from flask import render_template
from flask import redirect
import csv

app = Flask(__name__)

@app.route('/')
def tasks_list():
    database = open("/Users/jailynneestevez/PycharmProjects/todolist/database.csv", 'r')
    csvreader = csv.reader(database)
    return render_template('list.html', csvreader=csvreader)

@app.route('/task', methods=['POST'])
def add_task():
    database = open("/Users/jailynneestevez/PycharmProjects/todolist/database.csv", 'a')
    if request.method == 'POST':
        database.write(request.form["content"] + "," + request.form['date'] + "\n")
        return redirect('/')
    else:
        return 'Error', redirect('/')

@app.route('/delete', methods=['POST'])
def delete_tasks():
    database = open("/Users/jailynneestevez/PycharmProjects/todolist/database.csv", 'w')
    database.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()
