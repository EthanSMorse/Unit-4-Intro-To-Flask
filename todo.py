from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

todo = []

conn = pymysql.connect(
    database="emorse_todos",
    user="emorse",
    password="228246286",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)


@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT `description` FROM `todos`")
    results = cursor.fetchall()
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todo.append(new_todo)
    return render_template("todo.html.jinja", todos=todo)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    del todo[todo_index]
    return redirect('/')