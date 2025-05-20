import os
import csv
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
import reportlab.rl_config

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
reportlab.rl_config.warnOnMissingFontGlyphs = 0

data = []
page = 1
c = canvas.Canvas(str(page)+".pdf")

with open("Assassin!.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader:
        data.append(row)

rows = len(data)-1

name = 1
course = 2
soc = 3
image = 4
campus = 5

x = 50
y = 700

def write(row, txt, col, x, y,):
    c.drawString(x, y, txt+data[row][col])

for i in range(0,rows):
    row = i+1
    c = canvas.Canvas(str(data[row][campus])+"-"+str(page)+".pdf", pagesize=A4)
    c.setFont('Courier', 18)
    write(row,"Name: ", name, x, y-0)
    write(row,"Course: ", course, x, y-50)
    write(row,"Society: ", soc, x, y-100)
    write(row,"Campus: ", campus, x, y-150)
    c.showPage()
    c.save()
    page = page+1
