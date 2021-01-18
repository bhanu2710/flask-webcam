from flask import render_template, Flask

app = Flask(__name__)
@app.route("/")
def webcam():
    return render_template("webcam.html")

if __name__ == "__main__":
    app.run(debug=True)