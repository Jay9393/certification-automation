import PIL
import csv
from PIL import Image, ImageDraw, ImageFont
import os
import datetime
from dateutil.relativedelta import relativedelta

f = open("certification_list.csv", "r")
rdr = csv.reader(f)


def selected_font(font_size):
    return ImageFont.truetype("./Jalnan.ttf", font_size)


id = 0

for line in rdr:
    id += 1
    name = line[0]
    title = line[1]
    date = line[2]
    client = line[3]

    file_name = str(id) + "_" + name + "_수료증.pdf"
    target_image = Image.open("./images/certification.png")
    draw = ImageDraw.Draw(target_image)

    draw.text((593, 296), name, fill="black", font=selected_font(18), align="center")
    draw.text((593, 341), title, fill="black", font=selected_font(18), align="center")
    draw.text((593, 393), date, fill="black", font=selected_font(18), align="center")
    draw.text((528, 501), client, fill="black", font=selected_font(18), align="center")
    draw.text((598, 612), "2022", fill="black", font=selected_font(15), align="center")
    draw.text((691, 612), "8", fill="black", font=selected_font(15), align="center")
    draw.text((737, 612), "19", fill="black", font=selected_font(15), align="center")

    converted_image = target_image.convert("RGB")
    converted_image.save(file_name, "PDF")

f.close()
