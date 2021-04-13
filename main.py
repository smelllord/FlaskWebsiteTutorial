from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("tutorial.html")

app.run(host='0.0.0.0', port=8080)
