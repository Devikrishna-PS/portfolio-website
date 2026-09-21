from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    conn = sqlite3.connect("portfolio.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template("projects.html", projects=projects)

@app.route("/certificates")
def certificates():
    conn = sqlite3.connect("portfolio.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM certificates")
    certificates = cursor.fetchall()

    conn.close()

    return render_template("certificates.html", certificates=certificates)

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        conn = sqlite3.connect("portfolio.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO messages (name, email, subject, message)
        VALUES (?, ?, ?, ?)
        """, (name, email, subject, message))

        conn.commit()
        conn.close()

        return render_template("contact.html", success=True)

    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
