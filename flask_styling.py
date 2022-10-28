from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("styling/home.html")

@app.route("/containers")
def containers():
    return render_template("styling/containers.html")

@app.route("/grid")
def grid():
    return render_template("styling/grid.html")

@app.route("/page")
def fullpage():
    return render_template("styling/fullpage.html")

@app.route ("/flex")
def flex():
    return render_template("/styling/flex.html")

@app.route("/flex_page")
def flex_page():
    return render_template("/styling/flex_page.html")

if __name__ == "__main__":
    app.run(debug=True)
