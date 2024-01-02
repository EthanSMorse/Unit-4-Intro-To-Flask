from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = ['Build Muscle', 'Bing Chilling']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todo.append(new_todo)
    return render_template("todo.html.jinja", todos=todo)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    del todo[todo_index]
    return redirect('/')