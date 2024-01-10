from datetime import datetime

import math
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Создаем объект Canvas с размером страницы A4
pdf_canvas = canvas.Canvas("my_A4.pdf", pagesize=(1500, 1000))

pdfmetrics.registerFont(TTFont('AA-Higherup', 'AA-Higherup.ttf'))  # Замените 'AA-Higherup' на путь к файлу шрифта
pdfmetrics.registerFont(TTFont('Autoproject', 'Autoproject.ttf'))  # Замените 'Autoproject' на путь к файлу шрифта


def circle(circ, center_x, center_y, radius):
    path = circ.beginPath()
    circ.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    circ.setLineWidth(1)  # Ширина линии

    num_faces = max(24, int(radius / 0.25))  # Збільште кількість вузлів
    for i in range(num_faces + 1):
        angle = 2 * math.pi * i / num_faces
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        if i == 0:
            path.moveTo(x, y)
        else:
            path.lineTo(x, y)
    circ.setFillColorRGB(0, 0, 0)

    # Применяем путь на холсте
    circ.drawPath(path, fill=True)
    return circ


current_date = datetime.now().date()
current_time = datetime.now().time()


def table(name, thickness, height_table, width_table, length_table, tubex, tubey, long_circle, rog, rog_tubex,
          rog_tubey, rog_coor):
    """
    :param name: колір та текстура стільниці
    :param thickness:  товщина стільниці
    :param height_table: висота столу
    :param width_table: ширина столу
    :param length_table: довжина столу
    :param tubex: ширина труби основної
    :param tubey: товщина труби основної
    :param long_circle: відстань від краю отворів
    :param rog: довжина рожку
    :param rog_tubex: ширина труби рожка
    :param rog_tubey: товщина труби рожка
    :param rog_coor: відстань до рожка від краю рамки
    :return:
    """
    pass


name = "Дуб острава"

# товщина столешниці
thickness = 36

# Висота столу
height_table = 800

# Ширина столу
width_table = 600

# Довжина столу
length_table = 1400

# Ширина рамки мінус 25мм по краям
widht = width_table - 50

# Висота мінус столешниця
hight = height_table - thickness - 4

# Розмір труби основна
tubex = 80
tubey = 20

# Розмір від краю до отворів
long_circle = 15

# Довжина рожка
rog = 200

# Розмір труби рожка
rog_tubex = 30
rog_tubey = 30

# відстань до рожка
rog_coor = 150

# Внутрішні розміри
det_y = 50
rog_coorx = rog_coor / 2
rogx = rog / 2
widht_tube = widht - tubey * 2
det_widht = widht / 2 - tubey
det_hight = hight / 2
det_tubey = tubey / 2
det_tubex = tubex / 2

pdf_canvas.rect(15, 15, 1470, 970, fill=False)
pdf_canvas.rect(1155, 15, 330, 97, fill=False)
pdf_canvas.rect(1285, 15, 100, 70, fill=False)

pdf_canvas.rect(1285, 85, 200, 27, fill=False)

pdf_canvas.rect(1155, 15, 130, 12, fill=False)
pdf_canvas.rect(1155, 39, 130, 12, fill=False)
pdf_canvas.rect(1155, 63, 130, 12, fill=False)
pdf_canvas.rect(1155, 87, 130, 12, fill=False)
pdf_canvas.rect(1185, 15, 50, 97, fill=False)
pdf_canvas.rect(1265, 15, 20, 97, fill=False)

pdf_canvas.rect(1385, 73, 100, 12, fill=False)
pdf_canvas.rect(1385, 61, 100, 12, fill=False)
pdf_canvas.rect(1418, 61, 33, 24, fill=False)

# Верхня деталь
pdf_canvas.line(105 + det_tubey, det_y - det_tubey + det_hight, 105 + det_tubey, det_y + 50 - det_tubey + det_hight)
pdf_canvas.line(105 + det_tubey + det_widht, det_y - det_tubey + det_hight, 105 + det_tubey + det_widht,
                det_y + 50 - det_tubey + det_hight)
pdf_canvas.line(105 + det_tubey, det_y - det_tubey + det_hight + 40, 105 + det_tubey + det_widht,
                det_y - det_tubey + det_hight + 40)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_tubey, det_y - det_tubey + det_hight, det_widht, det_tubey, fill=True)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(100 + det_widht / 2, det_y - det_tubey + det_hight + 45, f"{widht_tube} мм")

# Ліва деталь
pdf_canvas.line(70, det_y + det_hight, 120, det_y + det_hight)
pdf_canvas.line(70, det_y, 120, det_y)
pdf_canvas.line(80, det_y, 80, det_y + det_hight)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105, det_y, det_tubey, det_hight, fill=True)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.rotate(90)
pdf_canvas.drawString(det_y + (det_hight / 2) - 20, -75, f"{hight} мм")
pdf_canvas.rotate(-90)

# Права деталь
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_tubey + det_widht, det_y, det_tubey, det_hight, fill=True)

# # Нижня деталь
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_tubey, det_y, det_widht, det_tubey, fill=True)

# деталь з рожками
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_tubey, det_y + 150 + det_hight, det_widht, det_tubex, fill=True)  # широка деталь

pdf_canvas.line(105 + det_widht + det_tubey, det_y + 150 + det_hight + det_tubex,
                105 + det_widht + det_tubey, det_y + 200 + det_hight + det_tubex)  # від краю широкої деталі

pdf_canvas.line(105 + det_widht - rog_coorx, det_y + 180 + det_hight + det_tubex,
                105 + det_widht + det_tubey, det_y + 180 + det_hight + det_tubex)  # від краю широкої деталі до рожка

# від краю широкої до отворів

pdf_canvas.line(105 + det_tubey, det_y + 150 + det_hight,
                30 + det_tubey, det_y + 150 + det_hight)

pdf_canvas.line(355 + det_tubey, det_y + 160 + det_hight,
                30 + det_tubey, det_y + 160 + det_hight)

pdf_canvas.line(40 + det_tubey, det_y + 200 + det_hight,
                40 + det_tubey, det_y + 120 + det_hight)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(50 + det_tubey, det_y + 165 + det_hight, f"{long_circle} мм")

pdf_canvas.line(105 + det_tubey, det_y + 160 + det_hight,
                105 + det_tubey, det_y + 80 + det_hight)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(110 + det_tubey, det_y + 95 + det_hight, f"""100 мм""")
pdf_canvas.drawString(110 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

pdf_canvas.line(155 + det_tubey, det_y + 160 + det_hight,
                155 + det_tubey, det_y + 80 + det_hight)
pdf_canvas = circle(pdf_canvas, 155 + det_tubey, det_y + 160 + det_hight, 2)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(160 + det_tubey, det_y + 95 + det_hight, f"200 мм")
pdf_canvas.drawString(160 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

pdf_canvas = circle(pdf_canvas, 205 + det_tubey, det_y + 160 + det_hight, 2)

pdf_canvas.line(205 + det_tubey, det_y + 160 + det_hight,
                205 + det_tubey, det_y + 80 + det_hight)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(210 + det_tubey, det_y + 95 + det_hight, f"300 мм")
pdf_canvas.drawString(210 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

pdf_canvas = circle(pdf_canvas, 255 + det_tubey, det_y + 160 + det_hight, 2)

pdf_canvas.line(255 + det_tubey, det_y + 160 + det_hight,
                255 + det_tubey, det_y + 80 + det_hight)

pdf_canvas.line(305 + det_tubey, det_y + 90 + det_hight,
                105 + det_tubey, det_y + 90 + det_hight)

if widht_tube >= 450:
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(260 + det_tubey, det_y + 95 + det_hight, f"400 мм")
    pdf_canvas.drawString(260 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

    pdf_canvas = circle(pdf_canvas, 305 + det_tubey, det_y + 160 + det_hight, 2)

    pdf_canvas.line(305 + det_tubey, det_y + 160 + det_hight,
                    305 + det_tubey, det_y + 80 + det_hight)

if widht_tube >= 550:
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(310 + det_tubey, det_y + 95 + det_hight, f"500 мм")
    pdf_canvas.drawString(310 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

    pdf_canvas.line(355 + det_tubey, det_y + 160 + det_hight,
                    355 + det_tubey, det_y + 80 + det_hight)

    pdf_canvas = circle(pdf_canvas, 355 + det_tubey, det_y + 160 + det_hight, 2)

    pdf_canvas.line(355 + det_tubey, det_y + 90 + det_hight,
                    105 + det_tubey, det_y + 90 + det_hight)

if widht_tube >= 650:
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(360 + det_tubey, det_y + 95 + det_hight, f"700 мм")
    pdf_canvas.drawString(360 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

    pdf_canvas = circle(pdf_canvas, 405 + det_tubey, det_y + 160 + det_hight, 2)

    pdf_canvas.line(405 + det_tubey, det_y + 160 + det_hight,
                    405 + det_tubey, det_y + 80 + det_hight)

    pdf_canvas.line(405 + det_tubey, det_y + 90 + det_hight,
                    105 + det_tubey, det_y + 90 + det_hight)

    pdf_canvas.line(355 + det_tubey, det_y + 160 + det_hight,
                    405 + det_tubey, det_y + 160 + det_hight)

if widht_tube >= 750:
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(410 + det_tubey, det_y + 95 + det_hight, f"800 мм")
    pdf_canvas.drawString(410 + det_tubey, det_y + 70 + det_hight, f"д.5 мм")

    pdf_canvas = circle(pdf_canvas, 455 + det_tubey, det_y + 160 + det_hight, 2)

    pdf_canvas.line(455 + det_tubey, det_y + 160 + det_hight,
                    455 + det_tubey, det_y + 80 + det_hight)

    pdf_canvas.line(455 + det_tubey, det_y + 90 + det_hight,
                    105 + det_tubey, det_y + 90 + det_hight)

    pdf_canvas.line(405 + det_tubey, det_y + 160 + det_hight,
                    455 + det_tubey, det_y + 160 + det_hight)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(100 + det_widht - rog_coorx / 2, det_y + 182 + det_hight + det_tubex, f"{rog_coor} мм")

# Лівий рожок
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_tubey + rog_coorx, det_y + 150 + det_hight + det_tubex, rog_tubex / 2, rogx, fill=True)

# Правий рожок
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(105 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex, rog_tubex / 2, rogx, fill=True)

# Правий рожок отвори

pdf_canvas = circle(pdf_canvas, 105 + det_widht - rog_coorx + rog_tubex / 4, det_y + 100 + det_hight + det_tubex + rogx, 2)
pdf_canvas = circle(pdf_canvas, 105 + det_widht - rog_coorx + rog_tubex / 4, det_y + 125 + det_hight + det_tubex + rogx, 2)

pdf_canvas.line(105 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex,
                245 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex)  # від широкої деталі

pdf_canvas.line(105 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex + rogx,
                245 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex + rogx)  # від краю рожка

pdf_canvas.line(225 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex + rogx,
                225 + det_widht - rog_coorx, det_y + 150 + det_hight + det_tubex)  # від краю рожка до деталі

# Рожки та розміри отворів
pdf_canvas.line(105 + det_tubey + rog_coorx, det_y + 150 + det_hight + det_tubex + rogx,
                105 + det_tubey + rog_coorx, det_y + 200 + det_hight + det_tubex + rogx)

pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 50 + det_hight + det_tubex + rogx,
                105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 200 + det_hight + det_tubex + rogx)

pdf_canvas.line(105 + det_tubey, det_y + 180 + det_hight + det_tubex + rogx,
                105 + det_tubey + rog_coorx + rog_tubex / 2, det_y + 180 + det_hight + det_tubex + rogx)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(105 + det_tubey, det_y + 185 + det_hight + det_tubex + rogx, f"{rog_tubex / 2} мм")

pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 150 + det_hight + det_tubex + rogx,
                85, det_y + 150 + det_hight + det_tubex + rogx)

pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 125 + det_hight + det_tubex + rogx,
                85, det_y + 125 + det_hight + det_tubex + rogx)

pdf_canvas = circle(pdf_canvas, 105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 125 + det_hight + det_tubex + rogx,
                    2)  # отвір лівого рожка

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(95, det_y + 130 + det_hight + det_tubex + rogx, f"50мм д.5мм")

pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 100 + det_hight + det_tubex + rogx,
                85, det_y + 100 + det_hight + det_tubex + rogx)

pdf_canvas = circle(pdf_canvas, 105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 100 + det_hight + det_tubex + rogx,
                    2)  # отвір лівого рожка

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(95, det_y + 105 + det_hight + det_tubex + rogx, f"100мм д.5мм")

pdf_canvas.line(90, det_y + 150 + det_hight + det_tubex + rogx,
                90, det_y + 100 + det_hight + det_tubex + rogx)

if rog >= 200:
    pdf_canvas = circle(pdf_canvas, 105 + det_widht - rog_coorx + rog_tubex / 4, det_y + 75 + det_hight + det_tubex + rogx,
                        2)  # отвір правого рожка

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(95, det_y + 80 + det_hight + det_tubex + rogx, f"150мм д.5мм")

    pdf_canvas = circle(pdf_canvas, 105 + det_tubey + rog_coorx + rog_tubex / 4,
                        det_y + 75 + det_hight + det_tubex + rogx,
                        2)  # отвір лівого рожка

    pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 75 + det_hight + det_tubex + rogx,
                    85, det_y + 75 + det_hight + det_tubex + rogx)

    pdf_canvas.line(90, det_y + 150 + det_hight + det_tubex + rogx,
                    90, det_y + 75 + det_hight + det_tubex + rogx)

if rog >= 250:
    pdf_canvas = circle(pdf_canvas, 105 + det_widht - rog_coorx + rog_tubex / 4, det_y + 50 + det_hight + det_tubex + rogx,
                        2)  # отвір правого рожка

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(95, det_y + 55 + det_hight + det_tubex + rogx, f"200мм д.5мм")

    pdf_canvas = circle(pdf_canvas, 105 + det_tubey + rog_coorx + rog_tubex / 4,
                        det_y + 50 + det_hight + det_tubex + rogx,
                        2)  # отвір лівого рожка

    pdf_canvas.line(105 + det_tubey + rog_coorx + rog_tubex / 4, det_y + 50 + det_hight + det_tubex + rogx,
                    85, det_y + 50 + det_hight + det_tubex + rogx)

    pdf_canvas.line(90, det_y + 150 + det_hight + det_tubex + rogx,
                    90, det_y + 50 + det_hight + det_tubex + rogx)

# Висота рожка та його текст
rozmir = det_y + 230 + det_hight + det_tubex

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.rotate(-90)
pdf_canvas.drawString(-rozmir, 230 + det_widht - rog_coorx, f"{rog} мм")
pdf_canvas.rotate(90)

# Окремі деталі та їх кількість

# широка деталь верхня
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(700, 900, det_widht, det_tubex, fill=True)

pdf_canvas.line(700, 900, 700, 860)
pdf_canvas.line(700 + det_widht, 900, 700 + det_widht, 860)
pdf_canvas.line(700, 870, 700 + det_widht, 870)

# ширина труби
pdf_canvas.line(700, 900, 650, 900)
pdf_canvas.line(700, 900 + det_tubex, 650, 900 + det_tubex)
pdf_canvas.line(660, 890, 660, 920 + det_tubex)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)

pdf_canvas.drawString(665, 905 + det_tubex, f"{tubex} мм")  # розмір ширини

pdf_canvas.drawString(700 + det_widht / 2 - 20, 875, f"{widht_tube} мм")  # розмір довжини

pdf_canvas.drawString(700 + det_widht + 20, 910, f"Кількіть: 2 шт з отворами")
pdf_canvas.drawString(700 + det_widht + 20, 890, f"Труба {tubex} x {tubey} мм")

pdf_canvas = circle(pdf_canvas, 700 + 50, 900 + 10, 2)
pdf_canvas = circle(pdf_canvas, 700 + 100, 900 + 10, 2)
pdf_canvas = circle(pdf_canvas, 700 + 150, 900 + 10, 2)

if widht_tube >= 450:
    pdf_canvas = circle(pdf_canvas, 700 + 200, 900 + 10, 2)

if widht_tube >= 550:
    pdf_canvas = circle(pdf_canvas, 700 + 250, 900 + 10, 2)

if widht_tube >= 650:
    pdf_canvas = circle(pdf_canvas, 700 + 300, 900 + 10, 2)

if widht_tube >= 750:
    pdf_canvas = circle(pdf_canvas, 700 + 350, 900 + 10, 2)

# широка деталь нижня
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(700, 800, det_widht, det_tubex, fill=True)

pdf_canvas.line(700, 800, 700, 760)
pdf_canvas.line(700 + det_widht, 800, 700 + det_widht, 760)
pdf_canvas.line(700, 770, 700 + det_widht, 770)

# ширина труби
pdf_canvas.line(700, 800, 650, 800)
pdf_canvas.line(700, 800 + det_tubex, 650, 800 + det_tubex)
pdf_canvas.line(660, 790, 660, 820 + det_tubex)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)

pdf_canvas.drawString(665, 805 + det_tubex, f"{tubex} мм")  # розмір ширини
pdf_canvas.drawString(700 + det_widht / 2 - 20, 775, f"{widht_tube} мм")
pdf_canvas.drawString(700 + det_widht + 20, 810, f"Кількіть: 2 шт нижні")
pdf_canvas.drawString(700 + det_widht + 20, 790, f"Труба {tubex} x {tubey} мм")

# Бокова деталь
pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(700, 700, det_hight, det_tubex, fill=True)

pdf_canvas.line(700, 700, 700, 660)
pdf_canvas.line(700 + det_hight, 700, 700 + det_hight, 660)
pdf_canvas.line(700, 670, 700 + det_hight, 670)

# ширина труби
pdf_canvas.line(700, 700, 650, 700)
pdf_canvas.line(700, 700 + det_tubex, 650, 700 + det_tubex)
pdf_canvas.line(660, 690, 660, 720 + det_tubex)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)

pdf_canvas.drawString(665, 705 + det_tubex, f"{tubex} мм")  # розмір ширини
pdf_canvas.drawString(700 + det_hight / 2 - 20, 675, f"{hight} мм")
pdf_canvas.drawString(700 + det_hight + 20, 710, f"Кількіть: 4 шт бокові")
pdf_canvas.drawString(700 + det_hight + 20, 690, f"Труба {tubex} x {tubey} мм")

# Рожки

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.rect(700, 600, rogx, rog_tubex / 2, fill=True)

pdf_canvas.line(700, 600, 700, 560)
pdf_canvas.line(700 + rogx, 600, 700 + rogx, 560)
pdf_canvas.line(700, 570, 700 + rogx, 570)

# ширина труби
pdf_canvas.line(700, 600, 650, 600)
pdf_canvas.line(700, 600 + rog_tubex / 2, 650, 600 + rog_tubex / 2)
pdf_canvas.line(660, 590, 660, 610 + rog_tubex)

pdf_canvas = circle(pdf_canvas, 700 + rogx - 25, 600 + rog_tubex / 4, 2)
pdf_canvas = circle(pdf_canvas, 700 + rogx - 50, 600 + rog_tubex / 4, 2)

if rog >= 200:
    pdf_canvas = circle(pdf_canvas, 700 + rogx - 75, 600 + rog_tubex / 4, 2)
if rog >= 250:
    pdf_canvas = circle(pdf_canvas, 700 + rogx - 100, 600 + rog_tubex / 4, 2)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.drawString(700 + rogx / 2 - 10, 575, f"{rog} мм")
pdf_canvas.drawString(665, 605 + rog_tubex / 2, f"{rog_tubex} мм")

pdf_canvas.drawString(700 + rogx + 20, 605, f"Кількіть: 4 шт рожки")
pdf_canvas.drawString(700 + rogx + 20, 585, f"Труба {rog_tubex} x {rog_tubey} мм")

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(800, 502)
path.lineTo(800, 202)
path.lineTo(810, 197)
path.lineTo(810, 497)
path.lineTo(800, 502)
path.lineTo(823, 510)
path.lineTo(833, 505)
path.lineTo(832, 212)
path.lineTo(810, 197)
path.lineTo(810, 497)
path.lineTo(833, 505)
path.lineTo(810, 497)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

# нижня деталь
path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(810, 197)
path.lineTo(1000, 101)
path.lineTo(1001, 111)
path.lineTo(810, 207)
path.lineTo(810, 197)
path.lineTo(810, 207)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(810, 207)
path.lineTo(832, 217)
path.lineTo(1001, 135)
path.lineTo(1001, 111)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(833, 505)
path.lineTo(1024, 411)
path.lineTo(1000, 400)
path.lineTo(810, 497)
path.lineTo(833, 505)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(810, 497)
path.lineTo(1000, 400)
path.lineTo(1000, 390)
path.lineTo(810, 487)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)
pdf_canvas.setLineWidth(1)
path.moveTo(1000, 400)
path.lineTo(1000, 101)
path.lineTo(1010, 96)
path.lineTo(1010, 395.5)
path.lineTo(1000, 400)
path.lineTo(1023, 411.5)
path.lineTo(1032, 407)
path.lineTo(1032, 112)
path.lineTo(1010, 96)
path.lineTo(1010, 395.5)
path.lineTo(1032, 407)
path.lineTo(1010, 395.5)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

# Лівий рожок
path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)
pdf_canvas.setLineWidth(1)
path.moveTo(860, 471)
path.lineTo(795, 444)
path.lineTo(795, 435)
path.lineTo(803, 431)
path.lineTo(803, 440)
path.lineTo(795, 444)
path.lineTo(803, 440)
path.lineTo(868, 467)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)
pdf_canvas.setLineWidth(1)
path.moveTo(868, 467)
path.lineTo(868, 457)
path.lineTo(803, 431)
path.lineTo(803, 440)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

# Правий рожок
path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)
pdf_canvas.setLineWidth(1)
path.moveTo(948, 426.5)
path.lineTo(890, 400)
path.lineTo(890, 391)
path.lineTo(898, 387)
path.lineTo(898, 396)
path.lineTo(890, 400)
path.lineTo(898, 396)
path.lineTo(956, 422)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

path = pdf_canvas.beginPath()
pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
pdf_canvas.setLineWidth(1)  # Ширина линии
path.moveTo(956, 422)
path.lineTo(956, 413)
path.lineTo(898, 387)
path.lineTo(898, 396)

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.drawPath(path, fill=True)

# верхня деталь отвори
pdf_canvas = circle(pdf_canvas, 980, 427, 1)
pdf_canvas = circle(pdf_canvas, 940, 447, 1)
pdf_canvas = circle(pdf_canvas, 900, 467, 1)
pdf_canvas = circle(pdf_canvas, 860, 487, 1)

# рожки отвори правий
pdf_canvas = circle(pdf_canvas, 907, 404, 1)
pdf_canvas = circle(pdf_canvas, 925, 412, 1)
pdf_canvas = circle(pdf_canvas, 943, 420, 1)

# рожки отвори правий
pdf_canvas = circle(pdf_canvas, 812, 448, 1)
pdf_canvas = circle(pdf_canvas, 832, 456, 1)
pdf_canvas = circle(pdf_canvas, 853, 465, 1)

pdf_canvas.line(800, 502, 710, 467)
pdf_canvas.line(800, 202, 710, 163)
pdf_canvas.line(730, 475, 730, 171)

pdf_canvas.setFont("Autoproject", 20)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.rotate(90)
pdf_canvas.drawString(300, -725, f"{hight} мм")
pdf_canvas.rotate(-90)

pdf_canvas.line(823, 510, 910, 543)
pdf_canvas.line(1030, 406, 1105, 443)
pdf_canvas.line(890, 535, 1090, 435)

pdf_canvas.setFont("Autoproject", 20)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.rotate(-28)
pdf_canvas.drawString(615, 895, f"{widht} мм")
pdf_canvas.rotate(28)

# image_path = "1.jpg"

image_path1 = "2.jpeg"
pdf_canvas.drawImage(image_path1, 1160, 150, 200, 400, mask='auto')

pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
pdf_canvas.setLineWidth(2)
pdf_canvas.rect(1160, 150, 200, 400, fill=False)

pdf_canvas.setLineWidth(1)
pdf_canvas.line(1160, 550, 1160, 580)
pdf_canvas.line(1360, 550, 1360, 580)
pdf_canvas.line(1160, 570, 1360, 570)
pdf_canvas.line(1360, 550, 1380, 575)
pdf_canvas.line(1380, 575, 1480, 575)
pdf_canvas.line(1360, 550, 1390, 550)
pdf_canvas.line(1360, 150, 1390, 150)
pdf_canvas.line(1380, 550, 1380, 150)

pdf_canvas.setFont("Autoproject", 18)
pdf_canvas.setFillColor(colors.black)
pdf_canvas.rotate(-90)
pdf_canvas.drawString(-390, 1385, f"{length_table} мм")
pdf_canvas.rotate(90)

pdf_canvas.setFont("Autoproject", 18)  # Устанавливаем шрифт и размер текста
pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
pdf_canvas.drawString(1240, 575, f"{width_table} мм")  # Ширина стільниці
pdf_canvas.drawString(1380, 580, f"Товщина {thickness} мм")  # Товщина столешніци

pdf_canvas.setFont("Autoproject", 22)  # Устанавливаем шрифт и размер текста
pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
pdf_canvas.drawString(1160, 610, f"Стільниця: {name}")  # Назва стільниці

pdf_canvas.setFont("Autoproject", 18)  # Устанавливаем шрифт и размер текста
pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
pdf_canvas.drawString(1292, 92, "Кресленя столу LOFT ")  # Назва
pdf_canvas.drawString(1390, 43, f"{current_date}")  # Дата
pdf_canvas.drawString(1390, 22, f"{str(current_time)[:8]}")  # Час

# Закрываем объект Canvas, сохраняя изменения в файле
pdf_canvas.save()
