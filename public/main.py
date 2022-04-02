from flask import Flask, request, render_template
import json

app = Flask(__name__, template_folder="../views")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    email = request.form.get("email")
    phone = request.form.get("phone")
    date = request.form.get("date")
    message = request.form.get("message")
    image = request.files.get("slika1")

#mimetype
    image.save("./image.png")
    file = open("contact.txt", "a")
    file.write(json.dumps({
        "email": email,
        "phone": phone,
        "date": date,
        "message": message,
    }))
    file.close()
    return render_template("index.html", contact=True)


app.run(use_reloader=True)
