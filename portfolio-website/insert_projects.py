import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

projects = [
    (
        "Lumina – Superhero Help Portal",
        "A mental wellness support website featuring Lumina, an interactive superhero guide built using HTML, CSS, and JavaScript.",
        "HTML, CSS, JavaScript, Vercel",
        "https://github.com/Devikrishna-PS/lumina-superhero-help-portal",
        "https://your-lumina.vercel.app",
        "lumina.png"
    ),
    (
        "Java Shopping Cart System",
        "Desktop shopping cart application built using Java and SQLite with product and billing management.",
        "Java, SQLite, NetBeans",
        "https://github.com/Devikrishna-PS/GadgetCart-Project",
        "",
        "gadget.png"
    ),
    (
        "Student Performance Prediction System",
        "Machine learning web application that predicts student academic performance using Python and Flask.",
        "Python, Flask, Machine Learning",
        "https://github.com/Devikrishna-PS/students-performance-",
        "https://your-streamlit-app.streamlit.app",
        "student.png"
    ),
    (
        "COA – RISC Pipeline Simulator",
        "Interactive simulator demonstrating the five stages of a RISC processor pipeline using Python and Flask.",
        "Python, Flask, HTML, CSS",
        "https://github.com/Devikrishna-PS/risc_pro",
        "",
        "coa.jpeg"
    )
]

cursor.executemany("""
INSERT INTO projects
(title, description, technologies, github, demo, image)
VALUES (?, ?, ?, ?, ?, ?)
""", projects)

conn.commit()
conn.close()

print("Projects inserted successfully!")