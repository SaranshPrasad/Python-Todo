from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo_items = []
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")
@app.route("/add", methods=["POST", "GET"])
def add():
    global todo_items
    if request.method == "POST":
        items = request.form.get('items')
        todo_items.append(items)
        return render_template("index.html", list_items=todo_items)
    return render_template("index.html", list_items=todo_items)

@app.route("/delete/<task>", methods=["POST"])
def delete(task):
    global todo_items
    todo_items.remove(task)
    return redirect('/add')

