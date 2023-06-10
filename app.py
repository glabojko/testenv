from flask import Flask, render_template
import data_manager


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/child", methods=["POST", "GET"])
def child():
    return render_template('child.html')

if __name__ == '__main__':
    app()