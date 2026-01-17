from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route("/")
def heart():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # Read POSTed form data
    item = request.form.get("item")
    quantity = request.form.get("quantity")

    if item != "lego" or quantity != "3":
        return render_template("try_again.html")

    # Pass data to template
    return render_template("result.html", item=item, quantity=quantity)

@app.route("/flag")
def flag():
    item = request.args.get("item")
    quantity = request.args.get("quantity")

    # Only unlock if URL tampered correctly
    if item == "lego" and quantity == "3":
        return render_template("flag.html")
    else:
        return render_template("try_again.html")

if __name__ == "__main__":
    app.run(debug=True)

