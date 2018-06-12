from docx import Document
from docx.shared import Inches

document = Document()

p = document.add_paragraph()
r = p.add_run()
r.add_text('Good Morning every body,This is my ')
r.add_picture(r'C:\Users\m4k04\Desktop\workspace\imageDOc\1.png')
r.add_text(' do you like it?')

document.save('demo.docx')
