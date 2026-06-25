from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("audit_report.pdf")

styles = getSampleStyleSheet()

with open("audit_report.txt", "r") as file:
    content = file.read()

story = [Paragraph(content.replace("\n", "<br/>"), styles["Normal"])]

pdf.build(story)

print("PDF Created Successfully")