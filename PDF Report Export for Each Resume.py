from fpdf import FPDF

def generate_pdf_report(candidate_name, score, skills, output_path="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Resume Report - {candidate_name}", ln=1, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"ATS Score: {score}%", ln=1)
    pdf.cell(200, 10, txt="Top Skills Extracted:", ln=1)
    for skill in skills:
        pdf.cell(200, 10, txt=f"- {skill}", ln=1)
    pdf.output(output_path)
