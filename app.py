from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    output = ""

    if request.method == "POST":

        user_text = request.form.get("user_text")

        output = user_text

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)