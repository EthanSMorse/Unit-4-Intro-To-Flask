from flask import Flask, render_template, request

app = Flask(__name__)

todo = ['Build Muscle', 'Bing Chilling']

@app.route('/', methods=['GET', 'POST'])
def index():
    new_todo = request.form["new_todo"]
    todo.append(new_todo)
    return render_template("todo.html.jinja", todos=todo)