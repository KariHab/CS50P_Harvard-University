from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=50)

        #we need to create the heading
        self._pdf.cell(w=0, h=60, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

        #we need to create the image
        self._pdf.image("shirtificate.png", w=self._pdf.epw, alt_text="CS50 Shirtificate")
        #we need to create the image with the text in
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

#everything is save
    def save(self, name):
        self._pdf.output(name)


name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")