import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

certificates = [
    ("NPTEL – Programming in Java",
     "Elite + Silver certification from NPTEL.",
     "nptel.png"),

    ("HP LIFE – Certifications",
     "Completed HP LIFE certifications in Data Science & Analytics, Cyber Security, and AI for Beginners.",
     "HP-LIFE-Certifications.pdf"),

    ("QA Testing Internship",
     "Completed QA Testing Internship at ERA LLP.",
     "QA.jpeg"),

    ("AI & Machine Learning Internship",
     "Completed AI & Machine Learning Internship at SRAI Smart Solutions.",
     "SRAI-AI-Certificate.pdf"),

    ("Infosys Springboard – Courses",
     "Completed certification courses through Infosys Springboard in programming, technology, and professional skills.",
     "INFOSYS-Certificates.pdf"),

    ("One Million Prompters",
     "Completed the One Million Prompters initiative in AI prompting and Generative AI.",
     "One million -certificate.pdf"),

    ("NASA Space Apps Challenge",
     "Participated in the NASA Space Apps Challenge global hackathon.",
     "NASA-Certificate.pdf"),

    ("Academic Topper – Three Consecutive Semesters",
     "Secured the top position in B.Tech Computer Science & Engineering for three consecutive semesters.",
     "AcademicTopper-Certificate.pdf")
]

cursor.executemany("""
INSERT INTO certificates (name, description, pdf)
VALUES (?, ?, ?)
""", certificates)

conn.commit()
conn.close()

print("Certificates inserted successfully!")
