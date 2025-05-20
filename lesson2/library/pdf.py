from fpdf import FPDF

# יצירת קובץ PDF חדש
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# כותרת מרכזית
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Bat Sheva Itamar - Resume", ln=True, align='C')
pdf.ln(10)

# פרטים אישיים
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Contact Information:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Email: s0556764078@gmail.com | Phone: 055-6764078", ln=True)
pdf.ln(5)

# רקע אישי
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Professional Summary:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "Quick learner with strong logical thinking and self-learning abilities. "
                      "Highly effective both independently and within collaborative tech teams. "
                      "Excellent problem-solving skills, time management, and task execution.")
pdf.ln(5)

# ניסיון מקצועי
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Professional Experience:", ln=True)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Exam Management System Developer | Beit Hinuch Seminary | 2025", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "- Developed a system for managing exams, student registrations, and grade tracking.\n"
                      "- Successfully implemented within the seminary and deployed on an internal IIS server.\n"
                      "- Technologies: Node.js, React, MongoDB.")
pdf.ln(5)

# פרויקטים נוספים
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Additional Projects:", ln=True)
pdf.set_font("Arial", size=12)
projects = [
    "Business Management System – Developed a system with API and intuitive UI. (Node.js, React, MongoDB)",
    "Web API Development – Built an API managing JSON data with a customized user interface. (JavaScript, Node.js, JSON)",
    "Version Control System – Designed a Git-like system with CLI interface. (Python)",
    "C# Multi-Layered System – Built a business data management system following a 3-layer architecture.",
    "Online Exam Simulation – Developed a web-based exam simulator with automated question handling. (JavaScript, HTML, CSS)"
]

for project in projects:
    pdf.multi_cell(0, 8, "- " + project)

pdf.ln(5)

# השכלה
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Education:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "2023-2025 | Software Engineering Diploma - MAHAT.\n"
                      "Ultra-Code Training Program by Kama-Tech. High academic performance.")
pdf.ln(5)

# כישורים טכניים
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Technical Skills:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "Programming Languages: C#, Java, Python, Assembler, C++, C, JavaScript\n"
                      "Frameworks & Libraries: .NET, Node.js, jQuery, React, Angular, TypeScript\n"
                      "Technologies: Entity Framework, WinForms, GCP, XML, QA\n"
                      "Databases: SQL, MongoDB, Access\n"
                      "Operating Systems: Windows, Linux\n"
                      "Tools & Environments: VS Code, Postman, Visual Studio, PyCharm, IntelliJ IDEA, Eclipse")
pdf.ln(5)

# קורסים
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Courses & Certifications:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "Algorithms, Data Structures, Operating Systems, Mathematics, Digital Systems, "
                      "Computer Architecture, Networks & Communication, System Analysis, Selenium & UT, "
                      "WinForms, BI, Design Patterns, Real-Time Systems, Tech English.")
pdf.ln(5)

# שפות
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Languages:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "Hebrew – Native\nEnglish – High Level")

# שמירת הקובץ
pdf_output_path = "Bat_Sheva_Itamar_Resume.pdf"
pdf.output(pdf_output_path)

# החזרת הנתיב להורדה
print(f"PDF saved as: {pdf_output_path}")
