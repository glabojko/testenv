from flask import Flask, render_template, request
import data_manager


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():

    return render_template('index.html')

@app.route("/child", methods=["POST", "GET"])
def child():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        pesel = request.form.get('pesel')
    data_manager.add_child_to_database(id, name, pesel)
    return render_template('child.html', id=id, name=name, pesel=pesel)

if __name__ == '__main__':
    app()