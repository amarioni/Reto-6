from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/amoblamiento")
def amoblamiento():
    return render_template("amoblamiento.html")

@app.route("/driwall")
def driwall():
    return render_template("driwall.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/exito")
def exito():
    return render_template("exito.html")

@app.route("/presu")
def presu():
    return render_template("presu.html")

@app.route("/tyc")
def tyc():
    return render_template("tyc.html")

if __name__ == "__main__":
    app.run(debug=True)
